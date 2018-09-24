import argparse

from shortcuts.actions import KEYWORD_TO_ACTION_MAP


DOC_TEMPLATE = '''
# Supported Actions
{actions}
'''


ACTION_TEMPLATE = '''
## {name}

{doc}

**keyword**: `{keyword}`
**shortcuts identifier**: `{identifier}`

{params}
'''  # todo: choices


PARAM_TEMPLATE = '* {name} {opts}'


def _build_docs():
    actions_docs = []
    actions = sorted(KEYWORD_TO_ACTION_MAP.items())
    for _, action in actions:
        params = []
        for field in action().fields:
            choices = getattr(field, 'choices', None)
            if choices:
                opts = '  | _choices_:\n'
                opts += '\n'.join([f'\n  * "{choice}"' for choice in choices])
            else:
                opts = ''
            params.append(PARAM_TEMPLATE.format(name=field._attr, opts=opts))
        params = '\n'.join(params).strip()
        if params:
            params = f'params:\n\n{params}'
        actions_docs.append(
            ACTION_TEMPLATE.format(
                name=action.__name__,
                doc=action.__doc__ or '',
                keyword=action.keyword,
                identifier=action.itype,
                params=params,
            ).strip()
        )

    return DOC_TEMPLATE.format(actions='\n\n'.join(actions_docs))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Actions documentation generator')
    parser.add_argument('output', help='output file')
    args = parser.parse_args()

    doc = _build_docs()

    with open(args.output, 'w') as f:
        f.write(doc)
