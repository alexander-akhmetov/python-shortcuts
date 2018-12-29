class ShortcutsException(Exception):
    '''Base exception for shortcuts'''


class UnknownActionError(ShortcutsException):
    '''Action is not supported'''

    def __init__(self, itype, action_dict=None):
        message = f'''
            Unknown shortcut action: "{itype}"

            Please, check documentation to add new shortcut action, or create an issue:
            Docs: https://github.com/alexander-akhmetov/python-shortcuts/tree/master/docs/new_action.md

            https://github.com/alexander-akhmetov/python-shortcuts/
        '''
        if action_dict:
            message += f'''
            Action dictionary:

            {action_dict}
            '''
        super().__init__(message)


class UnknownWFTextTokenAttachment(ShortcutsException):
    '''Unknown WFTextTokenAttachment type'''


class UnknownWFEncodeModeError(ShortcutsException):
    '''Unknown value of the WFEncodeMode field'''


class UnknownVariableError(ShortcutsException):
    '''Unknown variable'''


class UnknownSerializationType(ShortcutsException):
    '''Unknown serialization type'''


class IncompleteCycleError(ShortcutsException):
    '''Incomplete cycle error'''


class InvalidShortcutURLError(ShortcutsException, ValueError):
    '''Invalid shortcut URL'''
