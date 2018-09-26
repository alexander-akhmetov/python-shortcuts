import json
import os.path
import uuid
from typing import Dict
from urllib.parse import urlparse
from urllib.request import urlopen

from shortcuts import exceptions


def download_shortcut(url: str) -> str:
    shortcut_id = _get_shortcut_uuid(url)
    shortcut_info = _get_shortcut_info(shortcut_id)
    download_url = shortcut_info['fields']['shortcut']['value']['downloadURL']
    response = _make_request(download_url)
    return response.read()


def _get_shortcut_uuid(url: str) -> str:
    '''
    Public url: https://www.icloud.com/shortcuts/{uuid}/
    '''
    if not is_shortcut_url(url):
        raise exceptions.InvalidShortcutURLError('Not a shortcut URL!')

    parsed_url = urlparse(url)
    splitted_path = os.path.split(parsed_url.path)
    if splitted_path:
        shortcut_id = splitted_path[-1]
        try:
            uuid.UUID(shortcut_id)  # just for validation, raises an error if it's not a valid UUID
        except ValueError:
            raise exceptions.InvalidShortcutURLError(f'Can not find shortcut id in "{url}"')
        return shortcut_id


def is_shortcut_url(url: str) -> bool:
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ('www.icloud.com', 'icloud.com'):
        return False
    if not parsed_url.path.startswith('/shortcuts/'):
        return False

    return True


def _get_shortcut_info(shortcut_id: str) -> Dict:
    url = f'https://www.icloud.com/shortcuts/api/records/{shortcut_id}/'
    response = _make_request(url)
    return json.loads(response.read())


def _make_request(url: str):
    response = urlopen(url)

    if response.status != 200:  # type: ignore
        raise RuntimeError(f'Can not get shortcut information from API: response code {response.status}')  # type: ignore

    return response
