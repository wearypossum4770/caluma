import graphene
from django.shortcuts import get_object_or_404
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphql_relay import from_global_id
from pyjexl.jexl import JEXL
from rest_framework import exceptions

from . import models, serializers
from ..mutation import SerializerMutation, UserDefinedPrimaryKeyMixin


class FlowJexl(graphene.String):
    """Flow jexl represents a jexl expression returning a task_specification slug."""

    pass


class Flow(DjangoObjectType):
    class Meta:
        model = models.Flow
        filter_fields = ("task_specification",)
        only_fields = ("task_specification", "next")
        interfaces = (relay.Node,)


class WorkflowSpecification(DjangoObjectType):
    flows = DjangoFilterConnectionField(Flow)

    class Meta:
        model = models.WorkflowSpecification
        filter_fields = ("slug", "name", "description", "is_published", "is_archived")
        interfaces = (relay.Node,)


class TaskSpecification(DjangoObjectType):
    class Meta:
        model = models.TaskSpecification
        filter_fields = ("slug", "name", "description", "type", "is_archived")
        interfaces = (relay.Node,)


class SaveWorkflowSpecification(UserDefinedPrimaryKeyMixin, SerializerMutation):
    class Meta:
        serializer_class = serializers.WorkflowSpecificationSerializer


class PublishWorkflowSpecification(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    workflow_specification = graphene.Field(WorkflowSpecification)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        _, workflow_specification_id = from_global_id(input["id"])
        workflow_specification = get_object_or_404(
            models.WorkflowSpecification, pk=workflow_specification_id
        )

        # TODO: validate workflow specification

        workflow_specification.is_published = True
        workflow_specification.save(update_fields=["is_published"])

        return PublishWorkflowSpecification(
            workflow_specification=workflow_specification
        )


class ArchiveWorkflowSpecification(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    workflow_specification = graphene.Field(WorkflowSpecification)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        _, workflow_specification_id = from_global_id(input["id"])
        workflow_specification = get_object_or_404(
            models.WorkflowSpecification, pk=workflow_specification_id
        )
        workflow_specification.is_archived = True
        workflow_specification.save(update_fields=["is_archived"])
        return ArchiveWorkflowSpecification(
            workflow_specification=workflow_specification
        )


class AddWorkflowSpecificationFlow(relay.ClientIDMutation):
    class Input:
        workflow_specification = graphene.ID(required=True)
        task_specification = graphene.ID(required=True)
        # TODO: add scalar type for jexl
        next = FlowJexl(required=True)

    workflow_specification = graphene.Field(WorkflowSpecification)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        _, workflow_specification_id = from_global_id(input["workflow_specification"])
        workflow_specification = get_object_or_404(
            models.WorkflowSpecification, pk=workflow_specification_id
        )
        workflow_specification.validate_editable()

        _, task_specification_id = from_global_id(input["task_specification"])
        task_specification = get_object_or_404(
            models.TaskSpecification, pk=task_specification_id
        )

        jexl = JEXL()
        # TODO: define transforms e.g. answer, task etc.
        errors = list(jexl.validate(input["next"]))
        if errors:
            raise exceptions.ValidationError(errors)

        models.Flow.objects.create(
            workflow_specification=workflow_specification,
            task_specification=task_specification,
            next=input["next"],
        )

        return AddWorkflowSpecificationFlow(
            workflow_specification=workflow_specification
        )


class RemoveWorkflowSpecificationFlow(relay.ClientIDMutation):
    class Input:
        workflow_specification = graphene.ID(required=True)
        task_specification = graphene.ID(required=True)

    workflow_specification = graphene.Field(WorkflowSpecification)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        _, workflow_specification_id = from_global_id(input["workflow_specification"])
        workflow_specification = get_object_or_404(
            models.WorkflowSpecification, pk=workflow_specification_id
        )
        workflow_specification.validate_editable()

        _, task_specification_id = from_global_id(input["task_specification"])
        task_specification = get_object_or_404(
            models.TaskSpecification, pk=task_specification_id
        )

        models.Flow.objects.filter(
            task_specification=task_specification,
            workflow_specification=workflow_specification,
        ).delete()

        return RemoveWorkflowSpecificationFlow(
            workflow_specification=workflow_specification
        )


class SaveTaskSpecification(UserDefinedPrimaryKeyMixin, SerializerMutation):
    class Meta:
        serializer_class = serializers.TaskSpecificationSerializer


class ArchiveTaskSpecification(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    task_specification = graphene.Field(TaskSpecification)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        _, task_specification_id = from_global_id(input["id"])
        task_specification = get_object_or_404(
            models.TaskSpecification, pk=task_specification_id
        )
        task_specification.is_archived = True
        task_specification.save(update_fields=["is_archived"])
        return ArchiveTaskSpecification(task_specification=task_specification)


class Mutation(object):
    save_workflow_specification = SaveWorkflowSpecification().Field()
    publish_workflow_specification = PublishWorkflowSpecification().Field()
    archive_workflow_specification = ArchiveWorkflowSpecification().Field()
    add_workflow_specification_flow = AddWorkflowSpecificationFlow().Field()
    remove_workflow_specification_flow = RemoveWorkflowSpecificationFlow().Field()

    save_task_specification = SaveTaskSpecification().Field()
    archive_task_specification = ArchiveTaskSpecification().Field()


class Query(object):
    all_workflow_specifications = DjangoFilterConnectionField(WorkflowSpecification)
    all_task_specifications = DjangoFilterConnectionField(TaskSpecification)
