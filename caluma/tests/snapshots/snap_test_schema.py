# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_schema_introspect 1"
] = """schema {
  query: Query
  mutation: Mutation
}

input AddFormQuestionInput {
  form: ID!
  question: ID!
  clientMutationId: String
}

type AddFormQuestionPayload {
  form: Form
  clientMutationId: String
}

input AddWorkflowFlowInput {
  workflow: ID!
  tasks: [ID]!
  next: FlowJexl!
  clientMutationId: String
}

type AddWorkflowFlowPayload {
  workflow: Workflow
  clientMutationId: String
}

interface Answer {
  id: ID
  createdAt: DateTime!
  createdByUser: String
  createdByGroup: String
  modifiedAt: DateTime!
  question: Question!
  meta: GenericScalar!
}

type AnswerConnection {
  pageInfo: PageInfo!
  edges: [AnswerEdge]!
  totalCount: Int
}

type AnswerEdge {
  node: Answer
  cursor: String!
}

enum AnswerHierarchyMode {
  DIRECT
  FAMILY
}

enum AnswerLookupMode {
  EXACT
  STARTSWITH
  CONTAINS
  ICONTAINS
  INTERSECTS
  GTE
  GT
  LTE
  LT
}

enum AnswerOrdering {
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

input CancelCaseInput {
  id: ID!
  clientMutationId: String
}

type CancelCasePayload {
  case: Case
  clientMutationId: String
}

type Case implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  closedAt: DateTime
  closedByUser: String
  closedByGroup: String
  workflow: Workflow!
  status: CaseStatus!
  meta: GenericScalar
  document: Document
  workItems(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], status: WorkItemStatusArgument, task: ID, case: ID, createdByUser: String, createdByGroup: String, metaHasKey: String, orderBy: [WorkItemOrdering], addressedGroups: [String], documentHasAnswer: [HasAnswerFilterType], caseDocumentHasAnswer: [HasAnswerFilterType], caseMetaValue: [JSONValueFilterType]): WorkItemConnection
  parentWorkItem: WorkItem
}

type CaseConnection {
  pageInfo: PageInfo!
  edges: [CaseEdge]!
  totalCount: Int
}

type CaseEdge {
  node: Case
  cursor: String!
}

enum CaseOrdering {
  STATUS_ASC
  STATUS_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

enum CaseStatus {
  RUNNING
  COMPLETED
  CANCELED
}

enum CaseStatusArgument {
  RUNNING
  COMPLETED
  CANCELED
}

type ChoiceQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  options(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], slug: String, label: String, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, orderBy: [OptionOrdering]): OptionConnection
  id: ID!
}

type CompleteTaskFormTask implements Task, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  name: String!
  description: String
  type: TaskType!
  meta: GenericScalar!
  addressGroups: GroupJexl
  isArchived: Boolean!
  leadTime: Int
  isMultipleInstance: Boolean!
  form: Form!
  id: ID!
}

input CompleteWorkItemInput {
  id: ID!
  clientMutationId: String
}

type CompleteWorkItemPayload {
  workItem: WorkItem
  clientMutationId: String
}

type CompleteWorkflowFormTask implements Task, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  name: String!
  description: String
  type: TaskType!
  meta: GenericScalar!
  addressGroups: GroupJexl
  isArchived: Boolean!
  leadTime: Int
  isMultipleInstance: Boolean!
  id: ID!
}

input CopyFormInput {
  slug: String!
  name: String!
  description: String
  source: ID!
  isPublished: Boolean
  clientMutationId: String
}

type CopyFormPayload {
  form: Form
  clientMutationId: String
}

input CopyOptionInput {
  slug: String!
  label: String!
  source: ID!
  clientMutationId: String
}

type CopyOptionPayload {
  option: Option
  clientMutationId: String
}

input CopyQuestionInput {
  slug: String!
  label: String!
  source: ID!
  clientMutationId: String
}

type CopyQuestionPayload {
  question: Question
  clientMutationId: String
}

input CreateWorkItemInput {
  case: ID!
  multipleInstanceTask: ID!
  assignedUsers: [String]
  addressedGroups: [String]
  deadline: DateTime
  meta: JSONString
  clientMutationId: String
}

type CreateWorkItemPayload {
  workItem: WorkItem
  clientMutationId: String
}

type DataSource {
  info: String
  name: String!
}

type DataSourceConnection {
  pageInfo: PageInfo!
  edges: [DataSourceEdge]!
  totalCount: Int
}

type DataSourceData {
  label: String!
  slug: String!
}

type DataSourceDataConnection {
  pageInfo: PageInfo!
  edges: [DataSourceDataEdge]!
  totalCount: Int
}

type DataSourceDataEdge {
  node: DataSourceData
  cursor: String!
}

type DataSourceEdge {
  node: DataSource
  cursor: String!
}

scalar Date

type DateAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: Date!
  meta: GenericScalar!
  date: Date
}

type DateQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  id: ID!
}

scalar DateTime

type DjangoDebug {
  sql: [DjangoDebugSQL]
}

type DjangoDebugSQL {
  vendor: String!
  alias: String!
  sql: String
  duration: Float!
  rawSql: String!
  params: String!
  startTime: Float!
  stopTime: Float!
  isSlow: Boolean!
  isSelect: Boolean!
  transId: String
  transStatus: String
  isoLevel: String
  encoding: String
}

type Document implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  form: Form!
  meta: GenericScalar
  answers(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], question: ID, search: String, createdByUser: String, createdByGroup: String, metaHasKey: String, orderBy: [AnswerOrdering], questions: [ID]): AnswerConnection
  case: Case
  workItem: WorkItem
}

type DocumentConnection {
  pageInfo: PageInfo!
  edges: [DocumentEdge]!
  totalCount: Int
}

type DocumentEdge {
  node: Document
  cursor: String!
}

enum DocumentOrdering {
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

type DocumentValidityConnection {
  pageInfo: PageInfo!
  edges: [DocumentValidityEdge]!
  totalCount: Int
}

type DocumentValidityEdge {
  node: ValidationResult
  cursor: String!
}

type DynamicChoiceQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  options(before: String, after: String, first: Int, last: Int): DataSourceDataConnection
  dataSource: String!
  id: ID!
}

type DynamicMultipleChoiceQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  options(before: String, after: String, first: Int, last: Int): DataSourceDataConnection
  dataSource: String!
  id: ID!
}

type File implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  name: String!
  answer: FileAnswer
  uploadUrl: String
  downloadUrl: String
  metadata: GenericScalar
}

type FileAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: File!
  meta: GenericScalar!
  file: File
}

type FileQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  id: ID!
}

type FloatAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: Float!
  meta: GenericScalar!
}

type FloatQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  placeholder: String
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  id: ID!
  minValue: Float
  maxValue: Float
}

type Flow implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  next: FlowJexl!
  tasks: [Task]!
}

type FlowConnection {
  pageInfo: PageInfo!
  edges: [FlowEdge]!
  totalCount: Int
}

type FlowEdge {
  node: Flow
  cursor: String!
}

scalar FlowJexl

type Form implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  name: String!
  description: String
  meta: GenericScalar
  isPublished: Boolean!
  isArchived: Boolean!
  questions(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], slug: String, label: String, isRequired: String, isHidden: String, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, excludeForms: [ID], search: String, orderBy: [QuestionOrdering]): QuestionConnection
  source: Form
  documents(before: String, after: String, first: Int, last: Int): DocumentConnection
  id: ID!
}

type FormConnection {
  pageInfo: PageInfo!
  edges: [FormEdge]!
  totalCount: Int
}

type FormEdge {
  node: Form
  cursor: String!
}

enum FormOrdering {
  NAME_ASC
  NAME_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

type FormQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  subForm: Form
  id: ID!
}

type FormatValidator {
  slug: String!
  name: String!
  regex: String!
  errorMsg: String!
}

type FormatValidatorConnection {
  pageInfo: PageInfo!
  edges: [FormatValidatorEdge]!
  totalCount: Int
}

type FormatValidatorEdge {
  node: FormatValidator
  cursor: String!
}

scalar GenericScalar

scalar GroupJexl

input HasAnswerFilterType {
  question: String!
  value: GenericScalar!
  lookup: AnswerLookupMode
  hierarchy: AnswerHierarchyMode
}

type IntegerAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: Int!
  meta: GenericScalar!
}

type IntegerQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  placeholder: String
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  id: ID!
  maxValue: Int
  minValue: Int
}

enum JSONLookupMode {
  EXACT
  STARTSWITH
  CONTAINS
  ICONTAINS
  GTE
  GT
  LTE
  LT
}

scalar JSONString

input JSONValueFilterType {
  key: String!
  value: GenericScalar!
  lookup: JSONLookupMode
}

type ListAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: [String]!
  meta: GenericScalar!
}

type MultipleChoiceQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  options(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [OptionOrdering], slug: String, label: String, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String): OptionConnection
  staticContent: String
  id: ID!
}

type Mutation {
  saveWorkflow(input: SaveWorkflowInput!): SaveWorkflowPayload
  addWorkflowFlow(input: AddWorkflowFlowInput!): AddWorkflowFlowPayload
  removeFlow(input: RemoveFlowInput!): RemoveFlowPayload
  saveSimpleTask(input: SaveSimpleTaskInput!): SaveSimpleTaskPayload
  saveCompleteWorkflowFormTask(input: SaveCompleteWorkflowFormTaskInput!): SaveCompleteWorkflowFormTaskPayload
  saveCompleteTaskFormTask(input: SaveCompleteTaskFormTaskInput!): SaveCompleteTaskFormTaskPayload
  startCase(input: StartCaseInput!): StartCasePayload @deprecated(reason: "Use SaveCase mutation instead")
  saveCase(input: SaveCaseInput!): SaveCasePayload
  cancelCase(input: CancelCaseInput!): CancelCasePayload
  completeWorkItem(input: CompleteWorkItemInput!): CompleteWorkItemPayload
  saveWorkItem(input: SaveWorkItemInput!): SaveWorkItemPayload
  createWorkItem(input: CreateWorkItemInput!): CreateWorkItemPayload
  saveForm(input: SaveFormInput!): SaveFormPayload
  copyForm(input: CopyFormInput!): CopyFormPayload
  addFormQuestion(input: AddFormQuestionInput!): AddFormQuestionPayload
  removeFormQuestion(input: RemoveFormQuestionInput!): RemoveFormQuestionPayload
  reorderFormQuestions(input: ReorderFormQuestionsInput!): ReorderFormQuestionsPayload
  saveOption(input: SaveOptionInput!): SaveOptionPayload
  copyOption(input: CopyOptionInput!): CopyOptionPayload
  copyQuestion(input: CopyQuestionInput!): CopyQuestionPayload
  saveTextQuestion(input: SaveTextQuestionInput!): SaveTextQuestionPayload
  saveTextareaQuestion(input: SaveTextareaQuestionInput!): SaveTextareaQuestionPayload
  saveDateQuestion(input: SaveDateQuestionInput!): SaveDateQuestionPayload
  saveChoiceQuestion(input: SaveChoiceQuestionInput!): SaveChoiceQuestionPayload
  saveMultipleChoiceQuestion(input: SaveMultipleChoiceQuestionInput!): SaveMultipleChoiceQuestionPayload
  saveDynamicChoiceQuestion(input: SaveDynamicChoiceQuestionInput!): SaveDynamicChoiceQuestionPayload
  saveDynamicMultipleChoiceQuestion(input: SaveDynamicMultipleChoiceQuestionInput!): SaveDynamicMultipleChoiceQuestionPayload
  saveFloatQuestion(input: SaveFloatQuestionInput!): SaveFloatQuestionPayload
  saveIntegerQuestion(input: SaveIntegerQuestionInput!): SaveIntegerQuestionPayload
  saveTableQuestion(input: SaveTableQuestionInput!): SaveTableQuestionPayload
  saveFormQuestion(input: SaveFormQuestionInput!): SaveFormQuestionPayload
  saveFileQuestion(input: SaveFileQuestionInput!): SaveFileQuestionPayload
  saveStaticQuestion(input: SaveStaticQuestionInput!): SaveStaticQuestionPayload
  saveDocument(input: SaveDocumentInput!): SaveDocumentPayload
  saveDocumentStringAnswer(input: SaveDocumentStringAnswerInput!): SaveDocumentStringAnswerPayload
  saveDocumentIntegerAnswer(input: SaveDocumentIntegerAnswerInput!): SaveDocumentIntegerAnswerPayload
  saveDocumentFloatAnswer(input: SaveDocumentFloatAnswerInput!): SaveDocumentFloatAnswerPayload
  saveDocumentDateAnswer(input: SaveDocumentDateAnswerInput!): SaveDocumentDateAnswerPayload
  saveDocumentListAnswer(input: SaveDocumentListAnswerInput!): SaveDocumentListAnswerPayload
  saveDocumentTableAnswer(input: SaveDocumentTableAnswerInput!): SaveDocumentTableAnswerPayload
  saveDocumentFileAnswer(input: SaveDocumentFileAnswerInput!): SaveDocumentFileAnswerPayload
  removeAnswer(input: RemoveAnswerInput!): RemoveAnswerPayload
  removeDocument(input: RemoveDocumentInput!): RemoveDocumentPayload
}

interface Node {
  id: ID!
}

type Option implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isArchived: Boolean!
  meta: GenericScalar
  source: Option
  id: ID!
}

type OptionConnection {
  pageInfo: PageInfo!
  edges: [OptionEdge]!
  totalCount: Int
}

type OptionEdge {
  node: Option
  cursor: String!
}

enum OptionOrdering {
  LABEL_ASC
  LABEL_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type Query {
  allDataSources(before: String, after: String, first: Int, last: Int): DataSourceConnection
  dataSource(name: String, before: String, after: String, first: Int, last: Int): DataSourceDataConnection
  allWorkflows(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, orderBy: [WorkflowOrdering]): WorkflowConnection
  allTasks(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], slug: String, name: String, description: String, type: TaskTypeArgument, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, orderBy: [TaskOrdering]): TaskConnection
  allCases(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], workflow: ID, createdByUser: String, createdByGroup: String, metaHasKey: String, orderBy: [CaseOrdering], documentForm: String, hasAnswer: [HasAnswerFilterType], searchAnswers: SearchAnswerFilterType, status: [CaseStatusArgument], orderByQuestionAnswerValue: String): CaseConnection
  allWorkItems(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], status: WorkItemStatusArgument, orderBy: [WorkItemOrdering], documentHasAnswer: [HasAnswerFilterType], caseDocumentHasAnswer: [HasAnswerFilterType], caseMetaValue: [JSONValueFilterType], task: ID, case: ID, createdByUser: String, createdByGroup: String, metaHasKey: String, addressedGroups: [String]): WorkItemConnection
  allForms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  allQuestions(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [QuestionOrdering], slug: String, label: String, isRequired: String, isHidden: String, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, excludeForms: [ID], search: String): QuestionConnection
  allDocuments(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], form: ID, forms: [ID], search: String, id: ID, createdByUser: String, createdByGroup: String, metaHasKey: String, orderBy: [DocumentOrdering], rootDocument: ID, hasAnswer: [HasAnswerFilterType], searchAnswers: SearchAnswerFilterType): DocumentConnection
  allFormatValidators(before: String, after: String, first: Int, last: Int): FormatValidatorConnection
  documentValidity(id: ID!, before: String, after: String, first: Int, last: Int): DocumentValidityConnection
  node(id: ID!): Node
  _debug: DjangoDebug
}

interface Question {
  id: ID!
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  meta: GenericScalar!
  forms(before: String, after: String, first: Int, last: Int, slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, metaValue: [JSONValueFilterType], search: String, orderBy: [FormOrdering], slugs: [String]): FormConnection
  source: Question
}

type QuestionConnection {
  pageInfo: PageInfo!
  edges: [QuestionEdge]!
  totalCount: Int
}

type QuestionEdge {
  node: Question
  cursor: String!
}

scalar QuestionJexl

enum QuestionOrdering {
  LABEL_ASC
  LABEL_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

input RemoveAnswerInput {
  answer: ID!
  clientMutationId: String
}

type RemoveAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input RemoveDocumentInput {
  document: ID!
  clientMutationId: String
}

type RemoveDocumentPayload {
  document: Document
  clientMutationId: String
}

input RemoveFlowInput {
  flow: ID!
  clientMutationId: String
}

type RemoveFlowPayload {
  flow: Flow
  clientMutationId: String
}

input RemoveFormQuestionInput {
  form: ID!
  question: ID!
  clientMutationId: String
}

type RemoveFormQuestionPayload {
  form: Form
  clientMutationId: String
}

input ReorderFormQuestionsInput {
  form: ID!
  questions: [ID]!
  clientMutationId: String
}

type ReorderFormQuestionsPayload {
  form: Form
  clientMutationId: String
}

input SaveCaseInput {
  id: String
  workflow: ID!
  meta: JSONString
  parentWorkItem: ID
  form: ID
  clientMutationId: String
}

type SaveCasePayload {
  case: Case
  clientMutationId: String
}

input SaveChoiceQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  options: [ID]!
  clientMutationId: String
}

type SaveChoiceQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveCompleteTaskFormTaskInput {
  slug: String!
  name: String!
  description: String
  meta: JSONString
  addressGroups: GroupJexl
  isArchived: Boolean
  leadTime: Int
  isMultipleInstance: Boolean
  form: ID!
  clientMutationId: String
}

type SaveCompleteTaskFormTaskPayload {
  task: Task
  clientMutationId: String
}

input SaveCompleteWorkflowFormTaskInput {
  slug: String!
  name: String!
  description: String
  meta: JSONString
  addressGroups: GroupJexl
  isArchived: Boolean
  leadTime: Int
  isMultipleInstance: Boolean
  clientMutationId: String
}

type SaveCompleteWorkflowFormTaskPayload {
  task: Task
  clientMutationId: String
}

input SaveDateQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  clientMutationId: String
}

type SaveDateQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveDocumentDateAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: Date!
  clientMutationId: String
}

type SaveDocumentDateAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input SaveDocumentFileAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: String!
  valueId: ID
  clientMutationId: String
}

type SaveDocumentFileAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input SaveDocumentFloatAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: Float!
  clientMutationId: String
}

type SaveDocumentFloatAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input SaveDocumentInput {
  id: String
  form: ID!
  meta: JSONString
  clientMutationId: String
}

input SaveDocumentIntegerAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: Int!
  clientMutationId: String
}

type SaveDocumentIntegerAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input SaveDocumentListAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: [String]!
  clientMutationId: String
}

type SaveDocumentListAnswerPayload {
  answer: Answer
  clientMutationId: String
}

type SaveDocumentPayload {
  document: Document
  clientMutationId: String
}

input SaveDocumentStringAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: String!
  clientMutationId: String
}

type SaveDocumentStringAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input SaveDocumentTableAnswerInput {
  question: ID!
  document: ID!
  meta: JSONString
  value: [ID]!
  clientMutationId: String
}

type SaveDocumentTableAnswerPayload {
  answer: Answer
  clientMutationId: String
}

input SaveDynamicChoiceQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  dataSource: String!
  clientMutationId: String
}

type SaveDynamicChoiceQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveDynamicMultipleChoiceQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  dataSource: String!
  clientMutationId: String
}

type SaveDynamicMultipleChoiceQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveFileQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  clientMutationId: String
}

type SaveFileQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveFloatQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  minValue: Float
  maxValue: Float
  placeholder: String
  clientMutationId: String
}

type SaveFloatQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveFormInput {
  slug: String!
  name: String!
  description: String
  meta: JSONString
  isArchived: Boolean
  isPublished: Boolean
  clientMutationId: String
}

type SaveFormPayload {
  form: Form
  clientMutationId: String
}

input SaveFormQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  subForm: ID!
  clientMutationId: String
}

type SaveFormQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveIntegerQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  minValue: Int
  maxValue: Int
  placeholder: String
  clientMutationId: String
}

type SaveIntegerQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveMultipleChoiceQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  options: [ID]!
  clientMutationId: String
}

type SaveMultipleChoiceQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveOptionInput {
  slug: String!
  label: String!
  isArchived: Boolean
  meta: JSONString
  clientMutationId: String
}

type SaveOptionPayload {
  option: Option
  clientMutationId: String
}

input SaveSimpleTaskInput {
  slug: String!
  name: String!
  description: String
  meta: JSONString
  addressGroups: GroupJexl
  isArchived: Boolean
  leadTime: Int
  isMultipleInstance: Boolean
  clientMutationId: String
}

type SaveSimpleTaskPayload {
  task: Task
  clientMutationId: String
}

input SaveStaticQuestionInput {
  label: String!
  slug: String!
  infoText: String
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  staticContent: String
  clientMutationId: String
}

type SaveStaticQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveTableQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  rowForm: ID!
  clientMutationId: String
}

type SaveTableQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveTextQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  maxLength: Int
  placeholder: String
  formatValidators: [String]
  clientMutationId: String
}

type SaveTextQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveTextareaQuestionInput {
  slug: String!
  label: String!
  infoText: String
  isRequired: QuestionJexl
  isHidden: QuestionJexl
  meta: JSONString
  isArchived: Boolean
  maxLength: Int
  placeholder: String
  formatValidators: [String]
  clientMutationId: String
}

type SaveTextareaQuestionPayload {
  question: Question
  clientMutationId: String
}

input SaveWorkItemInput {
  workItem: ID!
  assignedUsers: [String]
  deadline: DateTime
  meta: JSONString
  clientMutationId: String
}

type SaveWorkItemPayload {
  workItem: WorkItem
  clientMutationId: String
}

input SaveWorkflowInput {
  slug: String!
  name: String!
  description: String
  meta: JSONString
  startTasks: [ID]!
  allowAllForms: Boolean
  allowForms: [ID]
  isArchived: Boolean
  isPublished: Boolean
  clientMutationId: String
}

type SaveWorkflowPayload {
  workflow: Workflow
  clientMutationId: String
}

input SearchAnswerFilterType {
  slugs: [String]
  value: GenericScalar!
  lookup: SearchLookupMode
}

enum SearchLookupMode {
  STARTSWITH
  CONTAINS
  TEXT
}

type SimpleTask implements Task, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  name: String!
  description: String
  type: TaskType!
  meta: GenericScalar!
  addressGroups: GroupJexl
  isArchived: Boolean!
  leadTime: Int
  isMultipleInstance: Boolean!
  id: ID!
}

input StartCaseInput {
  workflow: ID!
  meta: JSONString
  parentWorkItem: ID
  form: ID
  clientMutationId: String
}

type StartCasePayload {
  case: Case
  clientMutationId: String
}

type StaticQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  staticContent: String
  dataSource: String
  id: ID!
  isRequired: QuestionJexl!
}

type StringAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: String!
  meta: GenericScalar!
}

type TableAnswer implements Answer, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  question: Question!
  value: [Document]!
  meta: GenericScalar!
  document: Document!
}

type TableQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  infoText: String
  meta: GenericScalar!
  source: Question
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  rowForm: Form
  id: ID!
}

interface Task {
  id: ID!
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  name: String!
  description: String
  isArchived: Boolean!
  addressGroups: GroupJexl
  meta: GenericScalar!
  isMultipleInstance: Boolean!
}

type TaskConnection {
  pageInfo: PageInfo!
  edges: [TaskEdge]!
  totalCount: Int
}

type TaskEdge {
  node: Task
  cursor: String!
}

enum TaskOrdering {
  NAME_ASC
  NAME_DESC
  DESCRIPTION_ASC
  DESCRIPTION_DESC
  TYPE_ASC
  TYPE_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

enum TaskType {
  SIMPLE
  COMPLETE_WORKFLOW_FORM
  COMPLETE_TASK_FORM
}

enum TaskTypeArgument {
  SIMPLE
  COMPLETE_WORKFLOW_FORM
  COMPLETE_TASK_FORM
}

type TextQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  placeholder: String
  infoText: String
  meta: GenericScalar!
  source: Question
  formatValidators(before: String, after: String, first: Int, last: Int): FormatValidatorConnection
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  id: ID!
  maxLength: Int
}

type TextareaQuestion implements Question, Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  label: String!
  isRequired: QuestionJexl!
  isHidden: QuestionJexl!
  isArchived: Boolean!
  placeholder: String
  infoText: String
  meta: GenericScalar!
  source: Question
  formatValidators(before: String, after: String, first: Int, last: Int): FormatValidatorConnection
  forms(before: String, after: String, first: Int, last: Int, metaValue: [JSONValueFilterType], orderBy: [FormOrdering], slug: String, name: String, description: String, isPublished: Boolean, isArchived: Boolean, createdByUser: String, createdByGroup: String, metaHasKey: String, search: String, slugs: [String]): FormConnection
  id: ID!
  maxLength: Int
}

type ValidationEntry {
  slug: String!
  errorMsg: String!
}

type ValidationResult {
  id: ID
  isValid: Boolean
  errors: [ValidationEntry]
}

type WorkItem implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  id: ID!
  closedAt: DateTime
  closedByUser: String
  closedByGroup: String
  deadline: DateTime
  task: Task!
  status: WorkItemStatus!
  meta: GenericScalar
  addressedGroups: [String]!
  assignedUsers: [String]!
  case: Case!
  childCase: Case
  document: Document
}

type WorkItemConnection {
  pageInfo: PageInfo!
  edges: [WorkItemEdge]!
  totalCount: Int
}

type WorkItemEdge {
  node: WorkItem
  cursor: String!
}

enum WorkItemOrdering {
  STATUS_ASC
  STATUS_DESC
  DEADLINE_ASC
  DEADLINE_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}

enum WorkItemStatus {
  READY
  COMPLETED
  CANCELED
}

enum WorkItemStatusArgument {
  READY
  COMPLETED
  CANCELED
}

type Workflow implements Node {
  createdAt: DateTime!
  modifiedAt: DateTime!
  createdByUser: String
  createdByGroup: String
  slug: String!
  name: String!
  description: String
  meta: GenericScalar
  isPublished: Boolean!
  isArchived: Boolean!
  startTasks: [Task]!
  allowAllForms: Boolean!
  allowForms(before: String, after: String, first: Int, last: Int): FormConnection
  id: ID!
  tasks: [Task]!
  flows(before: String, after: String, first: Int, last: Int, task: ID, createdByUser: String, createdByGroup: String): FlowConnection
}

type WorkflowConnection {
  pageInfo: PageInfo!
  edges: [WorkflowEdge]!
  totalCount: Int
}

type WorkflowEdge {
  node: Workflow
  cursor: String!
}

enum WorkflowOrdering {
  NAME_ASC
  NAME_DESC
  DESCRIPTION_ASC
  DESCRIPTION_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  MODIFIED_AT_ASC
  MODIFIED_AT_DESC
  CREATED_BY_USER_ASC
  CREATED_BY_USER_DESC
  CREATED_BY_GROUP_ASC
  CREATED_BY_GROUP_DESC
  META_TEST_KEY_ASC
  META_TEST_KEY_DESC
  META_FOOBAR_ASC
  META_FOOBAR_DESC
}
"""
