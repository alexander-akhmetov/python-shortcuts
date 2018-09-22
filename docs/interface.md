# Interface

How to use this package from your python code:

```python

from shortcuts import Shortcut
from shortcuts.actions.base64 import Base64EncodeAction
from shortcuts.actions.variables import SetVariableAction
from shortcuts.actions.text import TextAction
from shortcuts.actions.out import ShowResultAction
from shortcuts.utils import convert_plist_to_binary


sc = Shortcut()

sc.actions = [
    TextAction(data={'text': 'Hello, world!'}),
    Base64EncodeAction(),
    SetVariableAction(data={'name': 'var'}),
    ShowResultAction(data={'text': 'Encoded variable: {{var}}'})
]

file_path = 's.shortcut'

with open(file_path, 'w') as f:
    sc.dump(f, file_format='plist')

convert_plist_to_binary(file_path)

```

Now you can upload `s.shortcut` to your phone and open it with Shortcuts app.
