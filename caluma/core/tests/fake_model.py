import uuid

from django.contrib.postgres.operations import HStoreExtension
from django.db import connection, migrations, models
from django.db.migrations.executor import MigrationExecutor


def define_fake_model(fields={}, model_base=models.Model, options={}):
    name = str(uuid.uuid4()).replace("-", "")[:8]

    meta_options = {"app_label": "core"}
    meta_options.update(options)

    attributes = {
        "__module__": __name__,
        "__name__": name,
        "Meta": type("Meta", (object,), meta_options),
    }

    attributes.update(fields)
    return type(name, (model_base,), attributes)


def get_fake_model(fields={}, model_base=models.Model, options={}):
    """Create fake model to use during unit tests."""

    model = define_fake_model(fields, model_base, options)

    class TestProject:
        def clone(self, *_args, **_kwargs):
            return self

    class TestMigration(migrations.Migration):
        operations = [HStoreExtension()]

    with connection.schema_editor() as schema_editor:
        migration_executor = MigrationExecutor(schema_editor.connection)
        migration_executor.apply_migration(
            TestProject(), TestMigration("caluma_extra", "core")
        )

        schema_editor.create_model(model)

    return model
