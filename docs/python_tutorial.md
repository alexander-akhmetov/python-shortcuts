# Python tutorial

You need to [install](/README.md#installation) **shortcuts** first.

---

How to use this package from your python code:

```python

from shortcuts import Shortcut, actions, FMT_SHORTCUT

sc = Shortcut()

sc.actions = [
    actions.TextAction(data={'text': 'Hello, world!'}),
    actions.Base64EncodeAction(),
    actions.SetVariableAction(data={'name': 'var'}),
    actions.ShowResultAction(data={'text': 'Encoded variable: {{var}}'})
]

file_path = 's.shortcut'

with open(file_path, 'wb') as f:
    sc.dump(f, file_format=FMT_SHORTCUT)
```

Now you can upload `s.shortcut` to your phone and open it with Shortcuts app.

Description of all supported actions you can find here: [/docs/actions.md](/docs/actions.md).
