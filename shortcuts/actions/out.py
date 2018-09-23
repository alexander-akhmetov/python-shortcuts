from shortcuts.actions.base import BaseAction, Field, VariablesField, BooleanField


class ShowResultAction(BaseAction):
    '''Show result: shows a result'''
    type = 'is.workflow.actions.showresult'
    keyword = 'show_result'

    text = VariablesField('Text')


class ShowAlertAction(BaseAction):
    '''Show alert'''
    type = 'is.workflow.actions.alert'
    keyword = 'alert'

    show_cancel_button = BooleanField('WFAlertActionCancelButtonShown')
    text = Field('WFAlertActionMessage')
    title = Field('WFAlertActionTitle')


class ExitAction(BaseAction):
    '''Exit'''
    type = 'is.workflow.actions.exit'
    keyword = 'exit'


class VibrateAction(BaseAction):
    '''Vibrate'''
    type = 'is.workflow.actions.vibrate'
    keyword = 'vibrate'
