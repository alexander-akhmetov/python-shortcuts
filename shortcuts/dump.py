from typing import Any, Dict
import plistlib

import toml


class BaseDumper:
    def __init__(self, shortcut: 'shortcuts.shortcut.Shortcut') -> None:
        self.shortcut = shortcut

    def dump(self, file_obj) -> str:
        return file_obj.write(self.dumps())


class PListDumper(BaseDumper):
    def dumps(self) -> str:
        data = {
            'WFWorkflowActions': self.shortcut._get_actions(),
            'WFWorkflowImportQuestions': self.shortcut._get_import_questions(),
            'WFWorkflowClientRelease': self.shortcut.client_release,
            'WFWorkflowClientVersion': self.shortcut.client_version,
            'WFWorkflowTypes': ['NCWidget', 'WatchKit'],  # todo: change me
            'WFWorkflowIcon': self.shortcut._get_icon(),
            'WFWorkflowInputContentItemClasses': self.shortcut._get_input_content_item_classes(),
        }

        return plistlib.dumps(data).decode('utf-8')


class TomlDumper(BaseDumper):
    def dumps(self) -> str:
        data = {
            'action': [self._process_action(a) for a in self.shortcut.actions],
        }
        return toml.dumps(data)

    def _process_action(self, action) -> Dict[str, Any]:
        data = {
            f._attr: action.data[f._attr] for f in action.fields if f._attr in action.data
        }
        data['type'] = action.keyword
        return data
