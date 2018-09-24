import pytest

from shortcuts.actions.base import BaseAction, BooleanField, ChoiceField, FloatField, IntegerField


class TestBaseAction:
    def test_get_parameters(self):
        base_action = BaseAction()
        base_action.itype = '123'
        dump = base_action.dump()

        exp_dump = {
            'WFWorkflowActionIdentifier': base_action.itype,
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


class TestChoiceField:
    def test_choice_field(self):
        choices = ('first', 'second')
        f = ChoiceField('test', choices=choices)

        assert f.process_value('first') == 'first'
        assert f.process_value('second') == 'second'

        with pytest.raises(ValueError):
            assert f.process_value('third')

    def test_choice_field_with_capitalization(self):
        choices = ('First', )
        f = ChoiceField('test', choices=choices, capitalize=True)

        assert f.process_value('first') == 'First'


class TestFloatField:
    def test_field(self):
        f = FloatField('t')

        assert f.process_value(4.4) == 4.4
        assert f.process_value('15.0') == 15.0
        assert type(f.process_value(4)) is float

        with pytest.raises(ValueError):
            f.process_value('asd')


class TestIntegerField:
    def test_field(self):
        f = IntegerField('t')

        assert f.process_value(4.4) == 4
        assert f.process_value('15') == 15
        assert type(f.process_value(4.4)) is int

        with pytest.raises(ValueError):
            f.process_value('asd')
