from shortcuts.actions.base import BaseAction, VariablesField


class SendMessageAction(BaseAction):
    '''Send Message'''
    itype = 'is.workflow.actions.sendmessage'
    keyword = 'send_message'

    recepients = VariablesField('WFSendMessageActionRecipients')
    text = VariablesField('WFSendMessageContent')

    default_fields = {
        'IntentAppIdentifier': 'com.apple.MobileSMS',
    }
