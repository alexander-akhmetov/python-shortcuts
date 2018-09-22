from shortcuts.actions.base import BaseAction


class Base64EncodeAction(BaseAction):
    '''Base64 encode'''
    type = 'is.workflow.actions.base64encode'
    keyword = 'base64_encode'

    default_fields = {
        'WFEncodeMode': 'Encode',
    }


class Base64DecodeAction(BaseAction):
    '''Base64 decode'''
    type = 'is.workflow.actions.base64decode'
    keyword = 'base64_decode'

    default_fields = {
        'WFEncodeMode': 'Decode',
    }
