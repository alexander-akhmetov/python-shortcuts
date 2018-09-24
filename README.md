# WIP: python-shortcuts

[![Build Status](https://travis-ci.org/alexander-akhmetov/python-shortcuts.svg?branch=master)](https://travis-ci.org/alexander-akhmetov/python-shortcuts)
[![PyPI](https://img.shields.io/pypi/v/shortcuts.svg)](https://pypi.python.org/pypi/shortcuts)

🍏 + 🐍 = ❤️

**python-shortcuts** is a library to create [Siri Shortcuts](https://support.apple.com/en-ae/guide/shortcuts/welcome/ios) on your laptop with your favourite text editor.
It uses [toml](https://github.com/toml-lang/toml) to represent shortcuts.

The library is in a very early development state (PR welcome!), so it does not support all actions from Shortcuts app.

* [Toml tutorial](docs/tutorial.md)
* [Python tutorial](docs/python_tutorial.md)
* [How to add a new action](docs/new_action.md)
* [Supported actions](docs/actions.md)
* [Examples](examples/)
* [Changelog](CHANGELOG.md)
* [Documentation](docs/)

## Why

I wanted to convert my shortcut to a file in human-readable format. :)

From the code below this library can create a working shortcut:

```toml
[[action]]
type = "ask"
question = "What is your name?"

[[action]]
type = "set_variable"
name = "name"

[[action]]
type = "show_result"
text = "Hello, {{name}}!"
```

Or the same with Python:

```python
from shortcuts import Shortcut, actions


sc = Shortcut()

sc.actions = [
    actions.AskAction(data={'question': 'What is your name?'}),
    actions.SetVariableAction(data={'name': 'name'}),
    actions.ShowResultAction(data={'text': 'Hello, {{name}}!'})
]
```

## How to use

### Requirements

This library requires `plutil` tool, which should be installed on MacOS by default.
On Linux, you should be able to use `plistutil` instead.

### Installation

```bash
pip install shortcuts
```

### Usage

### shortcut → toml

If you need to convert existing shortcut to a toml file, at first you need to export it.
Go into Shortcuts app, open the shortcut and share it. Choose "Share as file" and use this file with this library.

Convert shortcut file to `toml`:
```bash
shortcuts what_is_your_name.shortcut what_is_your_name.toml
```

### toml → shortcut

Convert a `toml` file to a shortcut file.
After you will need to open the file with iOS Shortcuts app.

```bash
shortcuts examples/what_is_your_name.toml what_is_your_name.shortcut
```

More examples of `toml` files you can find [here](examples/).
And [read the tutorial](docs/tutorial.md)! :)

## Development

### Tests

Run tests:

```bash
tox
```

### TODO

* ☐ Conditionals with auto-group_id: if-else, menu
* ☐ Nested fields: dict/array/etc
* ☐ Support variables in every field which support them in Shortcuts app
* ☐ Workflow types: widget, etc.
* ☐ Import questions
* ☐ Document all actions
* ☐ Support magic variables
* ☐ Support all current actions from Shortcuts app
