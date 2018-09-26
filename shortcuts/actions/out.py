from shortcuts.actions.base import BaseAction, BooleanField, ChoiceField, Field, FloatField, VariablesField


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
    text = VariablesField('WFAlertActionMessage')
    title = VariablesField('WFAlertActionTitle')


class NotificationAction(BaseAction):
    '''Show notification'''
    itype = 'is.workflow.actions.notification'
    keyword = 'notification'

    play_sound = BooleanField('WFNotificationActionSound', default=True)
    text = VariablesField('WFNotificationActionBody')
    title = VariablesField('WFNotificationActionTitle')


class ExitAction(BaseAction):
    '''Exit'''
    itype = 'is.workflow.actions.exit'
    keyword = 'exit'


class VibrateAction(BaseAction):
    '''Vibrate'''
    itype = 'is.workflow.actions.vibrate'
    keyword = 'vibrate'


SPEAK_LANGUAGE_CHOICES = (
    'Čeština (Česko)',
    'Dansk (Danmark)',
    'Deutsch (Deutschland)',
    'English (Australia)',
    'English (Ireland)',
    'English (South Africa)',
    'English (United Kingdom)',
    'English (United States)',
    'Español (España)',
    'Español (México)',
)


class SpeakTextAction(BaseAction):
    '''Speak text'''
    itype = 'is.workflow.actions.speaktext'
    keyword = 'speak_text'

    language = ChoiceField('WFSpeakTextLanguage', choices=SPEAK_LANGUAGE_CHOICES)
    pitch = FloatField('WFSpeakTextPitch', default=0.95)
    rate = FloatField('WFSpeakTextRate', default=0.44)
    wait_until_finished = BooleanField('WFSpeakTextWait', default=True)


class SetClipboardAction(BaseAction):
    itype = 'is.workflow.actions.setclipboard'
    keyword = 'set_clipboard'

    local_only = BooleanField('WFLocalOnly', required=False)
    expiration_date = Field('WFExpirationDate', required=False)
