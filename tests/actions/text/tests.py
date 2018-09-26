import pytest

from shortcuts.actions import SplitTextAction, ChangeCaseAction
from shortcuts.actions.text import SPLIT_SEPARATOR_CHOICES, CASE_CHOICES

from tests.conftest import ActionTomlLoadsMixin


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
