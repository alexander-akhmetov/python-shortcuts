# Interface

How to use this package from your python code:

```python

from shortcuts import Shortcut, actions
from shortcuts.utils import convert_plist_to_binary


sc = Shortcut()

sc.actions = [
    actions.TextAction(data={'text': 'Hello, world!'}),
    actions.Base64EncodeAction(),
    actions.SetVariableAction(data={'name': 'var'}),
    actions.ShowResultAction(data={'text': 'Encoded variable: {{var}}'})
]

file_path = 's.shortcut'

with open(file_path, 'w') as f:
    sc.dump(f, file_format='plist')

convert_plist_to_binary(file_path)

```

Now you can upload `s.shortcut` to your phone and open it with Shortcuts app.
