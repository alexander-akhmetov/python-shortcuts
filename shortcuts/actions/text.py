from shortcuts.actions.base import BaseAction, VariablesField, Field


class CommentAction(BaseAction):
    '''Comment: just a comment'''
    type = 'is.workflow.actions.comment'
    keyword = 'comment'

    text = Field('WFCommentActionText', help='Text to show in the comment')


class TextAction(BaseAction):
    '''Text: returns text as an output'''
    type = 'is.workflow.actions.gettext'
    keyword = 'text'

    text = VariablesField('WFTextActionText', help='Output of this action')
