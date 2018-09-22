from shortcuts.actions.base import BaseAction, Field, VariablesField


class ShowResultAction(BaseAction):
    '''Show result: shows a result'''
    type = 'is.workflow.actions.showresult'
    keyword = 'show_result'

    text = VariablesField('Text')


class ShowAlertAction(BaseAction):
    '''Show alert'''
    type = 'is.workflow.actions.alert'
    keyword = 'alert'

    show_cancel_button = Field('WFAlertActionCancelButtonShown')
    text = Field('WFAlertActionMessage')
    title = Field('WFAlertActionTitle')
