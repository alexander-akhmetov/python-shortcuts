from shortcuts.actions import (
    base,
    base64,
    calculation,
    date,
    dictionary,
    files,
    input,
    photo,
    text,
    out,
    variables,
    web,
)


KEYWORD_TO_ACTION_MAP = {}
TYPE_TO_ACTION_MAP = {}


def _create_map():
    modules = (
        base,
        base64,
        calculation,
        date,
        dictionary,
        files,
        input,
        photo,
        text,
        out,
        variables,
        web,
    )
    for module in modules:
        _parse_module(module)


def _parse_module(module):
    for name, cls in module.__dict__.items():
        if isinstance(cls, type) and issubclass(cls, base.BaseAction) and cls.keyword:
            KEYWORD_TO_ACTION_MAP[cls.keyword] = cls
            TYPE_TO_ACTION_MAP[cls.type] = cls


_create_map()
