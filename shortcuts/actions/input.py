from shortcuts.actions.base import BaseAction, Field, VariablesField


class AskAction(BaseAction):
    '''Ask for input'''
    itype = 'is.workflow.actions.ask'
    keyword = 'ask'

    question = Field('WFAskActionPrompt')
    input_type = Field('WFInputType', required=False)
    default_answer = VariablesField('WFAskActionDefaultAnswer', required=False)


class GetClipboardAction(BaseAction):
    itype = 'is.workflow.actions.getclipboard'
    keyword = 'get_clipboard'
