# Fields

These fields are available for creating [a new action](/docs/new_action/md).

## Field

Simple text field.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*]

## VariablesField

A text field which supports `{{variables}}` in it.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*]

## GroupIDField

A field which creates group_id automatically if it's not presented.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*]

## ChoiceField

A field that can accept a value out of provided choices.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `choices` - list of available choices for the field
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*

## ArrayField

A field that validates that value is a list.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*

## FloatField

A field that validates that value is a floating point number.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*

## IntegerField

A field that validates that value is a integer number.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*

## BooleanField

A boolean field.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*

## DictionaryField

A field that validates that value is a dictionary.

Params:

* `name` - name of the field in the shortcut's `plist` file (in the `WFWorkflowActionParameters` dictionary)
* `default` [*optional*]
* `required` [*optional, default=True*]
* `capitalize` [*optional, default=False*]
* `help` [*optional, default=''*
