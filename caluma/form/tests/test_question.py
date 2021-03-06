import pytest

from ...core.tests import (
    extract_global_id_input_fields,
    extract_serializer_input_fields,
)
from .. import models, serializers


@pytest.mark.parametrize(
    "question__type,question__configuration,question__data_source,question__format_validators",
    [
        (models.Question.TYPE_INTEGER, {"max_value": 10, "min_value": 0}, None, []),
        (models.Question.TYPE_FLOAT, {"max_value": 1.0, "min_value": 0.0}, None, []),
        (models.Question.TYPE_FLOAT, {}, None, []),
        (models.Question.TYPE_DATE, {}, None, []),
        (models.Question.TYPE_TEXT, {"max_length": 10}, None, ["email"]),
        (models.Question.TYPE_TEXTAREA, {"max_length": 10}, None, []),
        (models.Question.TYPE_CHOICE, {}, None, []),
        (models.Question.TYPE_MULTIPLE_CHOICE, {}, None, []),
        (models.Question.TYPE_FORM, {}, None, []),
        (models.Question.TYPE_FILE, {}, None, []),
        (models.Question.TYPE_DYNAMIC_CHOICE, {}, "MyDataSource", []),
        (models.Question.TYPE_DYNAMIC_MULTIPLE_CHOICE, {}, "MyDataSource", []),
        (models.Question.TYPE_STATIC, {}, None, []),
    ],
)
def test_query_all_questions(
    schema_executor,
    db,
    snapshot,
    question,
    form,
    form_question_factory,
    question_option,
    data_source_settings,
):
    form_question_factory.create(form=form)

    query = """
        query AllQuestionsQuery($search: String, $forms: [ID]) {
          allQuestions(isArchived: false, search: $search, excludeForms: $forms) {
            totalCount
            edges {
              node {
                id
                __typename
                slug
                label
                meta
                infoText
                ... on TextQuestion {
                  maxLength
                  placeholder
                  formatValidators {
                    edges {
                      node {
                        slug
                        name
                        regex
                        errorMsg
                      }
                    }
                  }
                }
                ... on TextareaQuestion {
                  maxLength
                  placeholder
                  formatValidators {
                    edges {
                      node {
                        slug
                        name
                        regex
                        errorMsg
                      }
                    }
                  }
                }
                ... on FloatQuestion {
                  floatMinValue: minValue
                  floatMaxValue: maxValue
                  placeholder
                }
                ... on IntegerQuestion {
                  integerMinValue: minValue
                  integerMaxValue: maxValue
                  placeholder
                }
                ... on MultipleChoiceQuestion {
                  options {
                    totalCount
                    edges {
                      node {
                        slug
                      }
                    }
                  }
                }
                ... on ChoiceQuestion {
                  options {
                    totalCount
                    edges {
                      node {
                        slug
                      }
                    }
                  }
                }
                ... on DynamicMultipleChoiceQuestion {
                  options {
                    edges {
                      node {
                        slug
                        label
                      }
                    }
                  }
                }
                ... on DynamicChoiceQuestion {
                  options {
                    edges {
                      node {
                        slug
                        label
                      }
                    }
                  }
                }
                ... on FormQuestion {
                  subForm {
                    slug
                  }
                }
                ... on StaticQuestion {
                  staticContent
                }
              }
            }
          }
        }
    """

    result = schema_executor(
        query,
        variables={
            "search": question.label,
            "forms": [extract_global_id_input_fields(form)["id"]],
        },
    )

    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("question__meta", [{"meta": "set"}])
def test_copy_question(
    db, snapshot, question, question_option_factory, schema_executor
):
    question_option_factory.create_batch(5, question=question)
    query = """
        mutation CopyQuestion($input: CopyQuestionInput!) {
          copyQuestion(input: $input) {
            question {
              slug
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": {
            "source": question.pk,
            "slug": "new-question",
            "label": "Test Question",
        }
    }
    result = schema_executor(query, variables=inp)

    assert not result.errors

    question_slug = result.data["copyQuestion"]["question"]["slug"]
    assert question_slug == "new-question"
    new_question = models.Question.objects.get(pk=question_slug)
    assert new_question.label == "Test Question"
    assert new_question.meta == question.meta
    assert new_question.type == question.type
    assert new_question.configuration == question.configuration
    assert new_question.row_form == question.row_form
    assert new_question.is_hidden == question.is_hidden
    assert new_question.is_required == question.is_required
    assert new_question.source == question
    assert list(
        models.QuestionOption.objects.filter(question=new_question).values("option")
    ) == list(models.QuestionOption.objects.filter(question=question).values("option"))


@pytest.mark.parametrize(
    "mutation",
    [
        "SaveTextQuestion",
        "SaveTextareaQuestion",
        "SaveIntegerQuestion",
        "SaveFloatQuestion",
        "SaveDateQuestion",
        "SaveFileQuestion",
    ],
)
@pytest.mark.parametrize(
    "question__is_required,success", (("true", True), ("true|invalid", False))
)
def test_save_question(db, snapshot, question, mutation, schema_executor, success):
    mutation_func = mutation[0].lower() + mutation[1:]
    query = f"""
        mutation {mutation}($input: {mutation}Input!) {{
          {mutation_func}(input: $input) {{
            question {{
              id
              slug
              label
              meta
              __typename
            }}
            clientMutationId
          }}
        }}
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveQuestionSerializer, question
        )
    }
    result = schema_executor(query, variables=inp)

    assert not bool(result.errors) == success
    if success:
        snapshot.assert_match(result.data)


@pytest.mark.parametrize(
    "question__type,question__configuration,question__format_validators,success",
    [
        (models.Question.TYPE_TEXT, {"max_length": 10}, [], True),
        (models.Question.TYPE_TEXT, {"max_length": 10}, ["email"], True),
        (models.Question.TYPE_TEXT, {"max_length": 10}, ["notavalidator"], False),
    ],
)
def test_save_text_question(db, question, schema_executor, success):
    query = """
        mutation SaveTextQuestion($input: SaveTextQuestionInput!) {
          saveTextQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on TextQuestion {
                maxLength
                formatValidators {
                  edges {
                    node {
                      slug
                      name
                      regex
                      errorMsg
                    }
                  }
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveTextQuestionSerializer, question
        )
    }
    result = schema_executor(query, variables=inp)
    assert not bool(result.errors) == success
    if success:
        assert result.data["saveTextQuestion"]["question"]["maxLength"] == 10
        if question.format_validators:
            assert (
                result.data["saveTextQuestion"]["question"]["formatValidators"][
                    "edges"
                ][0]["node"]["slug"]
                == "email"
            )


@pytest.mark.parametrize(
    "question__type,question__configuration",
    [(models.Question.TYPE_TEXTAREA, {"max_length": 10})],
)
def test_save_textarea_question(db, question, schema_executor):
    query = """
        mutation SaveTextareaQuestion($input: SaveTextareaQuestionInput!) {
          saveTextareaQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on TextareaQuestion {
                maxLength
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveTextareaQuestionSerializer, question
        )
    }
    result = schema_executor(query, variables=inp)
    assert not result.errors
    assert result.data["saveTextareaQuestion"]["question"]["maxLength"] == 10


@pytest.mark.parametrize(
    "question__type,question__configuration,success",
    [
        (models.Question.TYPE_FLOAT, {"max_value": 10.0, "min_value": 0.0}, True),
        (models.Question.TYPE_FLOAT, {"max_value": 1.0, "min_value": 10.0}, False),
    ],
)
def test_save_float_question(db, snapshot, question, schema_executor, success):
    query = """
        mutation SaveFloatQuestion($input: SaveFloatQuestionInput!) {
          saveFloatQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on FloatQuestion {
                minValue
                maxValue
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveFloatQuestionSerializer, question
        )
    }
    result = schema_executor(query, variables=inp)
    assert not bool(result.errors) == success
    if success:
        snapshot.assert_match(result.data)


@pytest.mark.parametrize(
    "question__type,question__configuration,success",
    [
        (models.Question.TYPE_INTEGER, {"max_value": 10, "min_value": 0}, True),
        (models.Question.TYPE_INTEGER, {"max_value": 1, "min_value": 10}, False),
    ],
)
def test_save_integer_question(db, snapshot, question, success, schema_executor):
    query = """
        mutation SaveIntegerQuestion($input: SaveIntegerQuestionInput!) {
          saveIntegerQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on FloatQuestion {
                minValue
                maxValue
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveIntegerQuestionSerializer, question
        )
    }
    result = schema_executor(query, variables=inp)
    assert not bool(result.errors) == success
    if success:
        snapshot.assert_match(result.data)


@pytest.mark.parametrize("question__type", [models.Question.TYPE_MULTIPLE_CHOICE])
def test_save_multiple_choice_question(
    db, snapshot, question, question_option_factory, schema_executor
):
    question_option_factory.create_batch(2, question=question)

    option_ids = question.options.order_by("-slug").values_list("slug", flat=True)

    query = """
        mutation SaveMultipleChoiceQuestion($input: SaveMultipleChoiceQuestionInput!) {
          saveMultipleChoiceQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on MultipleChoiceQuestion {
                options {
                  edges {
                    node {
                      slug
                      label
                    }
                  }
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveMultipleChoiceQuestionSerializer, question
        )
    }
    inp["input"]["options"] = option_ids
    result = schema_executor(query, variables=inp)
    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("question__type", [models.Question.TYPE_CHOICE])
def test_save_choice_question(db, snapshot, question, question_option, schema_executor):
    query = """
        mutation SaveChoiceQuestion($input: SaveChoiceQuestionInput!) {
          saveChoiceQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on ChoiceQuestion {
                options {
                  edges {
                    node {
                      slug
                      label
                    }
                  }
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveChoiceQuestionSerializer, question
        )
    }
    question.delete()  # test creation
    result = schema_executor(query, variables=inp)
    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("delete", [True, False])
@pytest.mark.parametrize(
    "question__type",
    [models.Question.TYPE_DYNAMIC_CHOICE, models.Question.TYPE_DYNAMIC_MULTIPLE_CHOICE],
)
def test_save_dynamic_choice_question(
    db, snapshot, question, delete, schema_executor, data_source_settings
):
    query = """
        mutation SaveDynamicChoiceQuestion($input: SaveDynamicChoiceQuestionInput!) {
          saveDynamicChoiceQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on DynamicChoiceQuestion {
                options {
                  edges {
                    node {
                      slug
                      label
                    }
                  }
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveDynamicChoiceQuestionSerializer, question
        )
    }
    if delete:
        question.delete()  # test creation
    result = schema_executor(query, variables=inp)
    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("delete", [True, False])
@pytest.mark.parametrize(
    "question__type", [models.Question.TYPE_DYNAMIC_MULTIPLE_CHOICE]
)
def test_save_dynamic_multiple_choice_question(
    db,
    snapshot,
    question,
    delete,
    question_option_factory,
    schema_executor,
    data_source_settings,
):
    query = """
        mutation SaveDynamicMultipleChoiceQuestion($input: SaveDynamicMultipleChoiceQuestionInput!) {
          saveDynamicMultipleChoiceQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on DynamicMultipleChoiceQuestion {
                options {
                  edges {
                    node {
                      slug
                      label
                    }
                  }
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveDynamicMultipleChoiceQuestionSerializer, question
        )
    }
    if delete:
        question.delete()  # test creation
    result = schema_executor(query, variables=inp)
    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("question__type", [models.Question.TYPE_TABLE])
def test_save_table_question(db, snapshot, question, question_option, schema_executor):
    query = """
        mutation SaveTableQuestion($input: SaveTableQuestionInput!) {
          saveTableQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on TableQuestion {
                rowForm {
                  slug
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveTableQuestionSerializer, question
        )
    }
    question.delete()  # test creation
    result = schema_executor(query, variables=inp)
    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("question__type", [models.Question.TYPE_FORM])
def test_save_form_question(db, snapshot, question, question_option, schema_executor):
    query = """
        mutation SaveFormQuestion($input: SaveFormQuestionInput!) {
          saveFormQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on FormQuestion {
                subForm {
                  slug
                }
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveFormQuestionSerializer, question
        )
    }
    question.delete()  # test creation
    result = schema_executor(query, variables=inp)
    assert not result.errors
    snapshot.assert_match(result.data)


@pytest.mark.parametrize("question__type", [models.Question.TYPE_STATIC])
def test_save_static_question(db, snapshot, question, schema_executor):
    query = """
        mutation SaveStaticQuestion($input: SaveStaticQuestionInput!) {
          saveStaticQuestion(input: $input) {
            question {
              id
              slug
              label
              meta
              __typename
              ... on StaticQuestion {
                staticContent
              }
            }
            clientMutationId
          }
        }
    """

    inp = {
        "input": extract_serializer_input_fields(
            serializers.SaveStaticQuestionSerializer, question
        )
    }
    result = schema_executor(query, variables=inp)
    assert not bool(result.errors)
    snapshot.assert_match(result.data)
