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
'''


def _build_docs():
    actions_docs = []
    actions = sorted(KEYWORD_TO_ACTION_MAP.items())
    for _, action in actions:
        params = '\n'.join([f'* {f._attr}' for f in action().fields]).strip()
        if params:
            params = f'params:\n\n{params}'
        actions_docs.append(
            ACTION_TEMPLATE.format(
                name=action.__name__,
                doc=action.__doc__ or '',
                keyword=action.keyword,
                identifier=action.type,
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
