import plistlib
import logging
from typing import List, Dict, Union

from shortcuts.loader import TomlLoader, PListLoader
from shortcuts.dump import PListDumper, TomlDumper


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
    def load(cls, file_object, file_format: str = 'toml') -> 'Shortcut':
        return cls._get_loader_class(file_format)().load(file_object)

    @classmethod
    def loads(cls, string, file_format: str = 'toml') -> 'Shortcut':
        return cls._get_loader_class(file_format)().loads(string)

    @classmethod
    def _get_loader_class(self, file_format: str) -> Union[PListDumper, TomlDumper]:
        supported_formats = {
            'plist': PListLoader,
            'toml': TomlLoader,
        }
        if file_format in supported_formats:
            logger.debug(f'Loading shortcut from file format: {supported_formats}')
            return supported_formats[file_format]

        raise RuntimeError(f'Unknown file_format: {file_format}')

    def dump(self, file_object, file_format: str = 'plist') -> None:
        return self._get_dumper_class(file_format)(shortcut=self).dump(file_object)

    def dumps(self, file_format: str = 'plist') -> None:
        return self._get_dumper_class(file_format)(shortcut=self).dumps()

    def _get_dumper_class(self, file_format: str) -> Union[PListDumper, TomlDumper]:
        supported_formats = {
            'plist': PListDumper,
            'toml': TomlDumper,
        }
        if file_format in supported_formats:
            logger.debug(f'Dumping shortcut to file format: {supported_formats}')
            return supported_formats[file_format]

        raise RuntimeError(f'Unknown file_format: {file_format}')

    def _get_actions(self) -> List:
        return [a.dumps() for a in self.actions]

    def _get_import_questions(self) -> List:
        # todo: change me
        return []

    def _get_icon(self) -> Dict:
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
