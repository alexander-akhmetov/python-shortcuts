class ShortcutsException(Exception):
    '''Base exception for shortcuts'''


class UnknownActionError(ShortcutsException):
    '''Action is not supported'''


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
