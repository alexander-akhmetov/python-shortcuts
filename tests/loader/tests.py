import pytest

from shortcuts.loader import WFTextTokenAttachmentField
from shortcuts.exceptions import UnknownWFTextTokenAttachment


class TestWFTextTokenAttachmentField:
    @pytest.mark.parametrize('data, exp_value', [
        ({'Type': 'Ask'}, '{{ask_when_run}}'),
        ({'Type': 'Clipboard'}, '{{clipboard}}'),
        ({'Type': 'ExtensionInput'}, '{{shortcut_input}}'),
        ({'Type': 'Variable', 'VariableName': 'var'}, 'var'),  # todo: #2
    ])
    def test_field(self, data, exp_value):
        f = WFTextTokenAttachmentField({'Value': data})
        assert f.deserialized_data == exp_value

    @pytest.mark.parametrize('data', [
        {},
        {'Value': {}},
        {'Value': {'Type': 'unknown'}},
    ])
    def test_raises_exception(self, data):
        with pytest.raises(UnknownWFTextTokenAttachment):
            WFTextTokenAttachmentField(data).deserialized_data
