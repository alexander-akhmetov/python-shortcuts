import logging

from shortcuts.actions.b64 import Base64DecodeAction, Base64EncodeAction
from shortcuts.actions.base import BaseAction
from shortcuts.actions.calculation import CountAction
from shortcuts.actions.conditions import ElseAction, EndIfAction, IfAction
from shortcuts.actions.date import DateAction, DetectDateAction, FormatDateAction, GetTimeBetweenDates
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
from shortcuts.actions.dictionary import (
    DictionaryAction,
    GetDictionaryFromInputAction,
    GetDictionaryValueAction,
    SetDictionaryValueAction,
)
from shortcuts.actions.files import (
    AppendFileAction,
    CreateFolderAction,
    PreviewDocumentAction,
    ReadFileAction,
    SaveFileAction,
)
from shortcuts.actions.input import AskAction, GetClipboardAction
from shortcuts.actions.menu import MenuEndAction, MenuItemAction, MenuStartAction
from shortcuts.actions.messages import SendMessageAction
from shortcuts.actions.numbers import NumberAction
from shortcuts.actions.out import (
    ExitAction,
    NotificationAction,
    SetClipboardAction,
    ShowAlertAction,
    ShowResultAction,
    SpeakTextAction,
    VibrateAction,
)
from shortcuts.actions.photo import CameraAction, GetLastPhotoAction, ImageConvertAction, SelectPhotoAction
from shortcuts.actions.registry import ActionsRegistry
from shortcuts.actions.scripting import (
    ChooseFromListAction,
    ContinueInShortcutAppAction,
    DelayAction,
    GetMyShortcutsAction,
    HashAction,
    NothingAction,
    OpenAppAction,
    RepeatEachEndAction,
    RepeatEachStartAction,
    RepeatEndAction,
    RepeatStartAction,
    RunShortcutAction,
    SetItemNameAction,
    ViewContentGraphAction,
    WaitToReturnAction,
)
from shortcuts.actions.text import (
    ChangeCaseAction,
    CommentAction,
    DetectLanguageAction,
    GetNameOfEmojiAction,
    GetTextFromInputAction,
    ScanQRBarCodeAction,
    ShowDefinitionAction,
    SplitTextAction,
    TextAction,
)
from shortcuts.actions.variables import AppendVariableAction, GetVariableAction, SetVariableAction
from shortcuts.actions.web import (
    ExpandURLAction,
    GetURLAction,
    OpenURLAction,
    URLAction,
    URLDecodeAction,
    URLEncodeAction,
)


# flake8: noqa

logger = logging.getLogger(__name__)

actions_registry = ActionsRegistry()


def _register_actions():
    # register all imported actions in the actions registry
    for _, val in globals().items():
        if isinstance(val, type) and issubclass(val, BaseAction) and val.keyword:
            actions_registry.register_action(val)
    logging.debug(f'Registered actions: {len(actions_registry.actions)}')


_register_actions()
