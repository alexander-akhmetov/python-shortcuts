# Actions

Sometimes (in the current state of the library - very often, honestly :) ), when you are trying to convert a shortcut to a toml file with this command you will see an error if the action is not supported by the library:

```bash
$ shortcuts myshortcut.shortcut myshortcut.toml

RuntimeError:

        Unknown shortcut action: is.workflow.actions.gettext

        Please, check documentation to add new shortcut action, or create an issue:
        Docs: https://github.com/alexander-akhmetov/python-shortcuts/tree/master/docs/new_action.md

        https://github.com/alexander-akhmetov/python-shortcuts/

        Action dictionary:

        {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.gettext',
            'WFWorkflowActionParameters': {'WFTextActionText': 'some text'},
        }
```

So, how to fix this?
You can create a new action somewhere class in the `src/actions/` directory
and import it in the `shortcuts/actions/__init__.py`:

```python
from actions.base import BaseAction, Field


class GetTextAction(BaseAction):
    itype = 'is.workflow.actions.gettext'
    keyword = 'get_text'

    text = Field('WFTextActionText', help='Text to show')
```

* `itype` - `WFWorkflowActionIdentifier` from shortcut's plist
* `keyword` - keyword for the action to be used in toml files

Every parameter from `WFWorkflowActionParameters` must be presented as a `Field` attribute of the action class.
If this parameter is not required, you can pass `required=False` to the `Field`.

That's all, now this action is supported by the library, and you can convert your shortcut:

```bash
$ shortcuts myshortcut.shortcut myshortcut.toml
$ cat myshortcut.toml

[[action]]
type = "get_text"
text = "some text"
```

And now, you need to do only one last thing. Please, send a pull request :)

## VariablesField

If the field supports variables, instead of `Field` you can use `VariablesField`:

```python
from actions.base import BaseAction, VariablesField


class GetTextAction(BaseAction):
    itype = 'is.workflow.actions.gettext'
    keyword = 'get_text'

    text = VariablesField('WFTextActionText', help='Text to show')
```

And then you can pass text data with `{{variable}}` inside.
