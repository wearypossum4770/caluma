import graphene
from graphene.relay import Node
from graphene_django.converter import convert_django_field, convert_field_to_string
from localized_fields.fields import LocalizedField

from .document import schema as document_schema
from .form import schema as form_schema
from .workflow import schema as workflow_schema

convert_django_field.register(LocalizedField, convert_field_to_string)


class Mutation(
    form_schema.Mutation,
    document_schema.Mutation,
    workflow_schema.Mutation,
    graphene.ObjectType,
):
    pass


class Query(
    form_schema.Query, document_schema.Query, workflow_schema.Query, graphene.ObjectType
):
    node = Node.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    types=[
        document_schema.StringAnswer,
        document_schema.ListAnswer,
        document_schema.IntegerAnswer,
        document_schema.FloatAnswer,
    ],
)
