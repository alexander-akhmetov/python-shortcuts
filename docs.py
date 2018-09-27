'''
Generates documentation for all available actions in the shortcuts.actions module
'''

import argparse

from shortcuts.actions import actions_registry
from shortcuts.actions.base import VariablesField


DOC_TEMPLATE = '''
# Supported Actions

This is a list of all actions supported by **python-shortcuts**.

Legend:

* *keyword*: This keyword you can use in `toml` files to describe action
* *shortcuts identifier*: (*itype*) this identifier will be used to generate an action in a shortcut

System variables:

* `{{{{ask_when_run}}}}` - ask the user for an input when the shortcut is running.

----

{actions}
'''


def _build_docs():
    actions_docs = []
    actions_docs = [_build_action_doc(a) for a in actions_registry.actions]
    return DOC_TEMPLATE.format(actions='\n\n'.join(actions_docs))


ACTION_TEMPLATE = '''
### {name}

{doc}

**keyword**: `{keyword}`
**shortcuts identifier**: `{identifier}`

{params}
'''


def _build_action_doc(action):
    params = '\n'.join([_build_params_doc(f) for f in action().fields]).strip()
    params = f'params:\n\n{params}' if params else ''

    doc = ''
    if action.__doc__:
        # remove spaces from the beginning of _each_ line
        doc = '\n'.join([l.strip() for l in action.__doc__.splitlines()])

    return ACTION_TEMPLATE.format(
        name=action.__name__,
        doc=doc,
        keyword=action.keyword,
        identifier=action.itype,
        params=params,
    ).strip()


PARAM_TEMPLATE = '* {name} {opts}'


def _build_params_doc(field):
    properties = ', '.join(_get_field_properties(field))
    opts = f'({properties})'

    choices = getattr(field, 'choices', None)
    if choices:
        opts += f' {field.help} | _choices_:\n'
        opts += '\n'.join([f'\n  * `{choice}`' for choice in choices])
    return PARAM_TEMPLATE.format(
        name=field._attr,
        opts=opts,
        help=field.help,
    ).strip()


def _get_field_properties(field):
    properties = []
    if field.required:
        properties.append('*required*')
    if field.default:
        properties.append(f'default={field.default}')
    if isinstance(field, VariablesField):
        properties.append('*variables support*')
    return properties


def main():
    parser = argparse.ArgumentParser(description='Actions documentation generator')
    parser.add_argument('output', help='output file')
    args = parser.parse_args()

    doc = _build_docs()

    with open(args.output, 'w') as f:
        f.write(doc)


if __name__ == '__main__':
    main()
