import logging
import plistlib
import uuid
from typing import Any, Dict, List, TextIO, Type

from shortcuts.actions import MenuEndAction, MenuItemAction, MenuStartAction
from shortcuts.actions.base import GroupIDField
from shortcuts.dump import BaseDumper, PListDumper, TomlDumper
from shortcuts.loader import BaseLoader, PListLoader, TomlLoader


logger = logging.getLogger(__name__)


class Shortcut:
    def __init__(self,
                 name: str = '',
                 client_release: str = '2.0',
                 client_version: str = '700',
                 minimal_client_version: int = 411,
                 actions: List = None) -> None:
        self.name = name
        self.client_release = client_release
        self.client_version = client_version
        self.minimal_client_version = minimal_client_version
        self.actions = actions if actions else []

    @classmethod
    def load(cls, file_object: TextIO, file_format: str = 'toml') -> 'Shortcut':
        return cls._get_loader_class(file_format).load(file_object)

    @classmethod
    def loads(cls, string: str, file_format: str = 'toml') -> 'Shortcut':
        return cls._get_loader_class(file_format).loads(string)

    @classmethod
    def _get_loader_class(self, file_format: str) -> Type[BaseLoader]:
        """Based on file_format returns loader class"""
        supported_formats = {
            'plist': PListLoader,
            'shortcut': PListLoader,
            'toml': TomlLoader,
        }
        if file_format in supported_formats:
            logger.debug(f'Loading shortcut from file format: {supported_formats}')
            return supported_formats[file_format]

        raise RuntimeError(f'Unknown file_format: {file_format}')

    def dump(self, file_object: TextIO, file_format: str = 'plist') -> None:
        self._get_dumper_class(file_format)(shortcut=self).dump(file_object)

    def dumps(self, file_format: str = 'plist') -> str:
        return self._get_dumper_class(file_format)(shortcut=self).dumps()

    def _get_dumper_class(self, file_format: str) -> Type[BaseDumper]:
        """Based on file_format returns dumper class"""
        supported_formats = {
            'plist': PListDumper,
            'shortcut': PListDumper,
            'toml': TomlDumper,
        }
        if file_format in supported_formats:
            logger.debug(f'Dumping shortcut to file format: {supported_formats}')
            return supported_formats[file_format]

        raise RuntimeError(f'Unknown file_format: {file_format}')

    def _get_actions(self) -> List[str]:
        """returns list of all actions"""
        self._set_group_ids()
        self._set_menu_items()
        return [a.dump() for a in self.actions]

    def _set_group_ids(self):
        """
        Automatically sets group_id based on WFControlFlowMode param
        Uses list as a stack to hold generated group_ids

        Each cycle or condition (if-else, repeat) in Shortcuts app must have group id.
        Start and end of the cycle must have the same group_id. To do this,
        we use stack to save generated or readed group_id to save it to all actions of the cycle
        """
        ids = []
        for action in self.actions:
            # if action has GroupIDField, we may need to generate it's value automatically
            if not isinstance(getattr(action, 'group_id', None), GroupIDField):
                continue

            control_mode = action.default_fields['WFControlFlowMode']
            if control_mode == 0:
                # 0 means beginning of the group
                group_id = action.data.get('group_id', str(uuid.uuid4()))
                action.data['group_id'] = group_id  # if wasn't defined
                ids.append(group_id)
            elif control_mode == 1:
                # 1 - else, so we don't need to remove group_id from the stack
                # we need to just use the latest one
                action.data['group_id'] = ids[-1]
            elif control_mode == 2:
                # end of the group, we must remove group_id
                try:
                    action.data['group_id'] = ids.pop()
                except IndexError:
                    # if actions are correct, all groups must be compelted
                    # (group complete if it has start and end actions)
                    raise RuntimeError('Incomplete cycle')

    def _set_menu_items(self):
        menus = []
        for action in self.actions:
            if isinstance(action, MenuStartAction):
                action.data['menu_items'] = []
                menus.append(action)
            elif isinstance(action, MenuItemAction):
                menus[-1].data['menu_items'].append(action.data['title'])
            elif isinstance(action, MenuEndAction):
                try:
                    menus.pop()
                except IndexError:
                    raise RuntimeError('Incomplete menu action')

    def _get_import_questions(self) -> List:
        # todo: change me
        return []

    def _get_icon(self) -> Dict[str, Any]:
        # todo: change me
        return {
            'WFWorkflowIconGlyphNumber': 59511,
            'WFWorkflowIconImageData': plistlib.Data(b''),
            'WFWorkflowIconStartColor': 431817727,
        }

    def _get_input_content_item_classes(self) -> List[str]:
        # todo: change me
        return [
            'WFAppStoreAppContentItem',
            'WFArticleContentItem',
            'WFContactContentItem',
            'WFDateContentItem',
            'WFEmailAddressContentItem',
            'WFGenericFileContentItem',
            'WFImageContentItem',
            'WFiTunesProductContentItem',
            'WFLocationContentItem',
            'WFDCMapsLinkContentItem',
            'WFAVAssetContentItem',
            'WFPDFContentItem',
            'WFPhoneNumberContentItem',
            'WFRichTextContentItem',
            'WFSafariWebPageContentItem',
            'WFStringContentItem',
            'WFURLContentItem',
        ]
