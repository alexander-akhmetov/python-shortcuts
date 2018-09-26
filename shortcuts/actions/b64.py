from shortcuts.actions.base import BaseAction


class Base64EncodeAction(BaseAction):
    '''Base64 encode'''
    itype = 'is.workflow.actions.base64encode'
    keyword = 'base64_encode'

    _additional_identifier_field = 'WFEncodeMode'
    _default_class = True

    default_fields = {
        'WFEncodeMode': 'Encode',
    }


class Base64DecodeAction(BaseAction):
    '''Base64 decode'''
    itype = 'is.workflow.actions.base64encode'
    keyword = 'base64_decode'

    _additional_identifier_field = 'WFEncodeMode'

    default_fields = {
        'WFEncodeMode': 'Decode',
    }
