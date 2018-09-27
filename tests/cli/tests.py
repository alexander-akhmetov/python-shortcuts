import pytest

from shortcuts import FMT_SHORTCUT, FMT_TOML
from shortcuts.cli import _get_format


class Test_get_format:
    @pytest.mark.parametrize('filepath,exp_format', [
        ('file.shortcut', FMT_SHORTCUT),
        ('file.plist', FMT_SHORTCUT),
        ('file.toml', FMT_TOML),
        ('https://icloud.com/shortcuts/some-id/', 'url'),
    ])
    def test_for_url(self, filepath, exp_format):
        assert _get_format(filepath) == exp_format

    def test_raises(self):
        with pytest.raises(RuntimeError):
            _get_format('abc')
