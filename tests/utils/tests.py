import json

import mock
import pytest


from shortcuts.utils import _make_request, is_shortcut_url, _get_shortcut_uuid, download_shortcut
from shortcuts.exceptions import InvalidShortcutURLError


class Test__make_request:
    def test_make_request_should_call_urllib(self):
        mocked_urlopen = mock.Mock()
        mocked_urlopen.return_value.status = 200
        url = 'https://google.com'

        with mock.patch('shortcuts.utils.urlopen', mocked_urlopen):
            response = _make_request(url)

        mocked_urlopen.assert_called_once_with(url)
        assert response == mocked_urlopen()

    def test_make_request_should_raise_exception_for_non_200_status(self):
        mocked_urllib = mock.Mock()
        mocked_urllib.return_value.status = 500

        with mock.patch('shortcuts.utils.urlopen', mocked_urllib):
            with pytest.raises(RuntimeError):
                _make_request('')


class Test__is_shortcut_url:
    @pytest.mark.parametrize('url,exp_result', [
        ('https://www.icloud.com/shortcuts/', True),
        ('https://icloud.com/shortcuts/', True),
        ('http://icloud.com/shortcuts/', True),
        ('https://icloud.com/', False),  # not shortcuts
        ('https://google.com/shortcuts/', False),  # not shortcuts
        ('', False),
        (None, False),
    ])
    def test_is_shortcut_url(self, url, exp_result):
        assert is_shortcut_url(url) is exp_result


class Test__get_shortcut_uuid:
    @pytest.mark.parametrize('url,exp_uuid', [
        ('https://www.icloud.com/shortcuts/288f4b6c-11bd-4c2b-bb08-5bfa7504bca5', '288f4b6c-11bd-4c2b-bb08-5bfa7504bca5'),
        ('https://icloud.com/shortcuts/288f4b6c-11bd-4c2b-bb08-5bfa7504bca5', '288f4b6c-11bd-4c2b-bb08-5bfa7504bca5'),
    ])
    def test_uuid(self, url, exp_uuid):
        assert _get_shortcut_uuid(url) == exp_uuid

    @pytest.mark.parametrize('url', [
        'https://yandex.ru',
        'https://icloud.com',
        '',
        'abc',
        None,
        'https://www.icloud.com/shortcuts/abc',
        'https://icloud.com/shortcuts/123'
    ])
    def test_exception_with_invalid_url(self, url):
        with pytest.raises(InvalidShortcutURLError):
            _get_shortcut_uuid(url)


class Test__download_shortcut:
    def test_should_return_shortcut_content(self):
        shortcut_id = '288f4b6c-11bd-4c2b-bb08-5bfa7504bca5'

        api_url = f'https://www.icloud.com/shortcuts/api/records/{shortcut_id}/'
        url = f'https://icloud.com/shortcuts/{shortcut_id}'
        download_url = 'some-url'
        exp_content = 'shortcut content'
        shortcut_info = {
            'fields': {
                'shortcut': {
                    'value': {
                        'downloadURL': download_url,
                    },
                },
            },
        }

        def _urlopen(url):
            mocked_response = mock.Mock()
            mocked_response.status = 200
            if url == api_url:
                mocked_response.read.return_value = json.dumps(shortcut_info)
            elif url == download_url:
                mocked_response.read.return_value = exp_content

            return mocked_response

        with mock.patch('shortcuts.utils.urlopen', _urlopen):
            response = download_shortcut(url)

        assert response == exp_content
