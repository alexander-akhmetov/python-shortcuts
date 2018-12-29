import plistlib
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, Type

import toml


if TYPE_CHECKING:
    from shortcuts import Shortcut    # noqa
    from shortcuts.actions.base import BaseAction    # noqa


class BaseDumper:
    '''
    Base class to dump shortcuts
    '''

    def __init__(self, shortcut: 'Shortcut') -> None:
        self.shortcut = shortcut

    def dump(self, file_obj: BinaryIO) -> None:
        data = self.dumps()

        if isinstance(data, str):
            data = data.encode('utf-8')    # type: ignore
        file_obj.write(data)    # type: ignore

    def dumps(self) -> str:
        raise NotImplementedError()


class PListDumper(BaseDumper):
    '''
    PListDumper is a class which dumps shortcuts to
    binary plist files supported by Apple Shortcuts app
    '''

    def dump(self, file_obj: BinaryIO) -> None:    # type: ignore
        binary = plistlib.dumps(  # todo: change dumps to binary and remove this
            plistlib.loads(self.dumps().encode('utf-8')),  # type: ignore
            fmt=plistlib.FMT_BINARY,
        )
        file_obj.write(binary)

    def dumps(self) -> str:
        data = {
            'WFWorkflowActions': self.shortcut._get_actions(),
            'WFWorkflowImportQuestions': self.shortcut._get_import_questions(),
            'WFWorkflowClientRelease': self.shortcut.client_release,
            'WFWorkflowClientVersion': self.shortcut.client_version,
            'WFWorkflowTypes': ['NCWidget', 'WatchKit'],    # todo: change me
            'WFWorkflowIcon': self.shortcut._get_icon(),
            'WFWorkflowInputContentItemClasses': self.shortcut._get_input_content_item_classes(),
        }

        return plistlib.dumps(data).decode('utf-8')


class TomlDumper(BaseDumper):
    '''TomlDumper is a class which dumps shortcuts to toml files'''

    def dumps(self) -> str:
        data = {
            'action': [self._process_action(a) for a in self.shortcut.actions],
        }

        return toml.dumps(data)

    def _process_action(self, action: Type['BaseAction']) -> Dict[str, Any]:
        data = {
            f._attr: action.data[f._attr]    # ignore: (mypy/#1465)
            for f in action.fields if f._attr in action.data    # type: ignore
        }
        data['type'] = action.keyword

        return data
