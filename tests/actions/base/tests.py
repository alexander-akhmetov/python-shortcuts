import pytest

from shortcuts.actions.base import (
    BaseAction,
    BooleanField,
    ChoiceField,
    FloatField,
    IntegerField,
    ArrayField,
    VariablesField,
)


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


class TestArrayField:
    def test_field(self):
        f = ArrayField('t')

        assert f.process_value(['1', '2']) == ['1', '2']

        with pytest.raises(ValueError):
            f.process_value('value')


class TestActionWithAskWhenRunField:
    def test_action(self):
        identifier = 'my.identifier'
        field_name = 'WFSomeField'

        class MyAction(BaseAction):
            itype = identifier

            my_field = VariablesField(field_name)

        action = MyAction(data={'my_field': '{{ask_when_run}}'})

        dump = action.dump()
        exp_dump = {
            'WFWorkflowActionIdentifier': identifier,
            'WFWorkflowActionParameters': {
                field_name: {
                    'WFSerializationType': 'WFTextTokenAttachment',
                    'Value': {
                        'Type': 'Ask',
                    },
                },
            },
        }
        assert dump == exp_dump


class TestVariablesField:
    @pytest.mark.parametrize('variable, exp_data', [
        (
            '{{var}}',
            {'attachmentsByRange': {'{0, 1}': {'Type': 'Variable', 'VariableName': 'var'}}, 'string': '￼'},
        ),
        (
            '{{var1}} + {{var2}}',
            {
                'attachmentsByRange': {
                    '{0, 1}': {'Type': 'Variable', 'VariableName': 'var1'},
                    '{3, 1}': {'Type': 'Variable', 'VariableName': 'var2'},
                },
                'string': '￼ + ￼',
            },
        ),
    ])
    def test_field_with_variables(self, variable, exp_data):
        f = VariablesField('')

        exp_data = {
            'Value': exp_data,
            'WFSerializationType': 'WFTextTokenString',
        }

        assert f.process_value(variable) == exp_data

    @pytest.mark.parametrize('variable, exp_data', [
        (
            '{{clipboard}}',
            {'Type': 'Clipboard'},
        ),
    ])
    def test_field_with_variables_with_token_only(self, variable, exp_data):
        f = VariablesField('')

        exp_data = {
            'Value': exp_data,
            'WFSerializationType': 'WFTextTokenAttachment',
        }

        assert f.process_value(variable) == exp_data
