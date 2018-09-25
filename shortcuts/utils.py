import json
import os.path
import uuid
from urllib.parse import urlparse
from urllib.request import urlopen


def download_shortcut(url):
    shortcut_id = _get_shortcut_uuid(url)
    shortcut_info = _get_shortcut_info(shortcut_id)
    download_url = shortcut_info['fields']['shortcut']['value']['downloadURL']
    response = _make_request(download_url)
    return response.read()


def _get_shortcut_uuid(url):
    '''
    Public url: https://www.icloud.com/shortcuts/{uuid}/
    '''
    if not url.startswith('https://www.icloud.com/shortcuts/'):
        raise ValueError('Not a shortcut URL!')

    parsed_url = urlparse(url)
    splitted_path = os.path.split(parsed_url.path)
    if splitted_path:
        shortcut_id = splitted_path[-1]
        try:
            uuid.UUID(shortcut_id)  # just for validation, raises an error if it's not a valid UUID
        except ValueError:
            raise ValueError(f'Can not find shortcut id in "{url}"')
        return shortcut_id


def _get_shortcut_info(shortcut_id):
    url = f'https://www.icloud.com/shortcuts/api/records/{shortcut_id}/'
    response = _make_request(url)
    return json.loads(response.read())


def _make_request(url):
    response = urlopen(url)

    if response.status != 200:
        raise RuntimeError(f'Can not get shortcut information from API: response code {response.status}')

    return response
