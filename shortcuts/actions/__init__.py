import types
from typing import Dict, Type

from shortcuts.actions.b64 import Base64DecodeAction, Base64EncodeAction
from shortcuts.actions.base import BaseAction
from shortcuts.actions.calculation import CountAction
from shortcuts.actions.conditions import ElseAction, EndIfAction, IfAction
from shortcuts.actions.date import DateAction, FormatDateAction
from shortcuts.actions.device import (
    GetBatteryLevelAction,
    GetDeviceDetailsAction,
    GetIPAddressAction,
    SetAirplaneModeAction,
    SetBluetoothAction,
    SetBrightnessAction,
    SetDoNotDisturbAction,
    SetLowPowerModeAction,
    SetMobileDataAction,
    SetTorchAction,
    SetVolumeAction,
    SetWiFiAction,
)
from shortcuts.actions.dictionary import DictionaryAction, GetDictionaryValueAction
from shortcuts.actions.files import CreateFolderAction, PreviewDocumentAction, ReadFileAction, SaveFileAction
from shortcuts.actions.input import AskAction
from shortcuts.actions.out import ExitAction, ShowAlertAction, ShowResultAction, VibrateAction
from shortcuts.actions.photo import CameraAction, GetLastPhotoAction, ImageConvertAction, SelectPhotoAction
from shortcuts.actions.scripting import (
    ContinueInShortcutAppAction,
    DelayAction,
    NothingAction,
    RepeatEndAction,
    RepeatStartAction,
    SetItemNameAction,
    ViewContentGraphAction,
    WaitToReturnAction,
)
from shortcuts.actions.text import CommentAction, TextAction
from shortcuts.actions.variables import GetVariableAction, SetVariableAction
from shortcuts.actions.web import GetURLAction, URLAction


# flake8: noqa


KEYWORD_TO_ACTION_MAP: Dict[str, Type[BaseAction]] = {}
ITYPE_TO_ACTION_MAP: Dict[str, Type[BaseAction]] = {}


def _create_maps():
    # from all imported actions above it
    # creates two maps: KEYWORD_TO_ACTION_MAP and ITYPE_TO_ACTION_MAP
    # which the library uses to find action classes by keyword or type
    for name, val in globals().items():
        if isinstance(val, type) and issubclass(val, base.BaseAction) and val.keyword:
            KEYWORD_TO_ACTION_MAP[val.keyword] = val
            ITYPE_TO_ACTION_MAP[val.itype] = val


_create_maps()
