import pytest

from shortcuts.actions.base import BaseAction, BooleanField


class TestBaseAction:
    def test_get_parameters(self):
        base_action = BaseAction()
        base_action.type = '123'
        dump = base_action.dumps()

        exp_dump = {
            'WFWorkflowActionIdentifier': base_action.type,
            'WFWorkflowActionParameters': {},
        }
        assert dump == exp_dump


class TestBooleanField:
    def test_boolean_field(self):
        f = BooleanField('test')

        assert f.process_value(True) is True
        assert f.process_value(False) is False
        assert f.process_value('False') is False
        assert f.process_value('True') is True

        with pytest.raises(ValueError):
            f.process_value('wrong value')
