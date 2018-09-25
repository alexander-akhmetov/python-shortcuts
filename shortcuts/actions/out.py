from shortcuts.actions.base import BaseAction, BooleanField, Field, VariablesField


class ShowResultAction(BaseAction):
    '''Show result: shows a result'''
    itype = 'is.workflow.actions.showresult'
    keyword = 'show_result'

    text = VariablesField('Text')


class ShowAlertAction(BaseAction):
    '''Show alert'''
    itype = 'is.workflow.actions.alert'
    keyword = 'alert'

    show_cancel_button = BooleanField('WFAlertActionCancelButtonShown', default=True)
    text = Field('WFAlertActionMessage')
    title = Field('WFAlertActionTitle')


class ExitAction(BaseAction):
    '''Exit'''
    itype = 'is.workflow.actions.exit'
    keyword = 'exit'


class VibrateAction(BaseAction):
    '''Vibrate'''
    itype = 'is.workflow.actions.vibrate'
    keyword = 'vibrate'
