from shortcuts.actions.base import BaseAction, Field


class AskAction(BaseAction):
    '''Ask for input'''
    type = 'is.workflow.actions.ask'
    keyword = 'ask'

    question = Field('WFAskActionPrompt')
    input_type = Field('WFInputType', required=False)
    default_answer = Field('WFAskActionDefaultAnswer', required=False)
