import pytest

from shortcuts.actions import SplitTextAction, ChangeCaseAction, DetectLanguageAction, ScanQRBarCodeAction, GetNameOfEmojiAction, GetTextFromInputAction, ShowDefinitionAction
from shortcuts.actions.text import SPLIT_SEPARATOR_CHOICES, CASE_CHOICES

from tests.conftest import ActionTomlLoadsMixin, SimpleBaseDumpsLoadsTest


class TestSplitTextAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = SplitTextAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.text.split',
            'WFWorkflowActionParameters': {
                'WFTextSeparator': 'New Lines',
            }
        }
        assert action.dump() == exp_dump

    def test_dumps_with_custom_separator(self):
        action = SplitTextAction(data={
            'custom_separator': ';',
            'separator_type': 'Custom',
        })
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.text.split',
            'WFWorkflowActionParameters': {
                'WFTextSeparator': 'Custom',
                'WFTextCustomSeparator': ';',
            }
        }
        assert action.dump() == exp_dump

    @pytest.mark.parametrize('separator', [
        *SPLIT_SEPARATOR_CHOICES,
    ])
    def test_dumps_with_choices(self, separator):
        action = SplitTextAction(data={'separator_type': separator})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.text.split',
            'WFWorkflowActionParameters': {
                'WFTextSeparator': separator,
            }
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "split_text"
        '''
        self._assert_toml_loads(toml, SplitTextAction, {})

    def test_choices(self):
        exp_choices = (
            'New Lines',
            'Spaces',
            'Every Character',
            'Custom',
        )
        assert SPLIT_SEPARATOR_CHOICES == exp_choices


class TestChangeCaseAction(ActionTomlLoadsMixin):
    @pytest.mark.parametrize('case_type', [
        *CASE_CHOICES,
    ])
    def test_dumps_with_choices(self, case_type):
        action = ChangeCaseAction(data={'case_type': case_type})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.text.changecase',
            'WFWorkflowActionParameters': {
                'WFCaseType': case_type,
            }
        }
        assert action.dump() == exp_dump

    @pytest.mark.parametrize('case_type', [
        *CASE_CHOICES,
    ])
    def test_loads_toml(self, case_type):
        toml = f'''
        [[action]]
        type = "change_case"
        case_type = "{case_type}"
        '''
        self._assert_toml_loads(toml, ChangeCaseAction, {'case_type': case_type})

    def test_choices(self):
        exp_choices = (
            'UPPERCASE',
            'lowercase',
            'Capitalize Every Word',
            'Capitalize with Title Case',
            'Capitalize with sentence case.',
            'cApItAlIzE wItH aLtErNaTiNg CaSe.',
        )
        assert CASE_CHOICES == exp_choices


class TestGetNameOfEmojiAction(SimpleBaseDumpsLoadsTest):
    action_class = GetNameOfEmojiAction
    itype = 'is.workflow.actions.getnameofemoji'
    toml = '[[action]]\ntype = "get_name_of_emoji"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.getnameofemoji</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''


class TestScanQRBarCodeAction(SimpleBaseDumpsLoadsTest):
    action_class = ScanQRBarCodeAction
    itype = 'is.workflow.actions.scanbarcode'
    toml = '[[action]]\ntype = "scan_barcode"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.scanbarcode</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''


class TestDetectLanguageAction(SimpleBaseDumpsLoadsTest):
    action_class = DetectLanguageAction
    itype = 'is.workflow.actions.detectlanguage'
    toml = '[[action]]\ntype = "detect_language"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.detectlanguage</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''


class TestGetTextFromInputAction(SimpleBaseDumpsLoadsTest):
    action_class = GetTextFromInputAction
    itype = 'is.workflow.actions.detect.text'
    toml = '[[action]]\ntype = "get_text_from_input"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.detect.text</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''


class TestShowDefinitionAction(SimpleBaseDumpsLoadsTest):
    action_class = ShowDefinitionAction
    itype = 'is.workflow.actions.showdefinition'
    toml = '[[action]]\ntype = "show_definition"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.showdefinition</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''
