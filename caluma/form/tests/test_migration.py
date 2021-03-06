from uuid import uuid4

from django.db import connection
from django.db.migrations.executor import MigrationExecutor


def test_migrate_to_flat_answers(transactional_db):
    executor = MigrationExecutor(connection)
    app = "form"
    migrate_from = [(app, "0017_auto_20190619_1320")]
    migrate_to = [(app, "0019_remove_answer_value_document")]

    executor.migrate(migrate_from)
    old_apps = executor.loader.project_state(migrate_from).apps

    # Create some old data. Can't use factories here

    Document = old_apps.get_model(app, "Document")
    Form = old_apps.get_model(app, "Form")
    Answer = old_apps.get_model(app, "Answer")
    Question = old_apps.get_model(app, "Question")
    FormQuestion = old_apps.get_model(app, "FormQuestion")

    main_form = Form.objects.create(slug="main-form")
    sub_form = Form.objects.create(slug="sub-form")

    main_form_question = Question.objects.create(
        type="form", sub_form=sub_form, slug="main-form-question"
    )
    FormQuestion.objects.create(form=main_form, question=main_form_question)

    main_text_question = Question.objects.create(type="text", slug="main-text-question")
    FormQuestion.objects.create(form=main_form, question=main_text_question)

    sub_text_question = Question.objects.create(type="text", slug="sub_1_question_1")
    FormQuestion.objects.create(form=sub_form, question=sub_text_question)

    # we need to set a temporary family, because the signals are not available
    main_document = Document.objects.create(form=main_form, family=uuid4())
    # then we set the correct family
    main_document.family = main_document.pk
    main_document.save()

    sub_document = Document.objects.create(form=sub_form, family=main_document.pk)
    sub_answer = Answer.objects.create(
        value="lorem ipsum", question=sub_text_question, document=sub_document
    )
    Answer.objects.create(
        value_document=sub_document, question=main_form_question, document=main_document
    )

    text_answer = Answer.objects.create(
        value="dolor sit", question=main_text_question, document=main_document
    )

    assert not sub_answer.document == main_document
    assert text_answer.document == main_document

    # Migrate forwards.
    executor.loader.build_graph()  # reload.
    executor.migrate(migrate_to)
    new_apps = executor.loader.project_state(migrate_to).apps

    # Test the new data.
    Answer = new_apps.get_model(app, "Answer")

    sub_answer = Answer.objects.get(value="lorem ipsum")
    text_answer = Answer.objects.get(value="dolor sit")

    assert Answer.objects.filter(question__type="form").count() == 0
    assert sub_answer.document.pk == main_document.pk
    assert text_answer.document.pk == main_document.pk
