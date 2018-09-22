
# Supported Actions
## ShowAlertAction

Show alert

**keyword**: `alert`
**shortcuts identifier**: `is.workflow.actions.alert`

params:

* show_cancel_button
* text
* title

## AskAction

Ask for input

**keyword**: `ask`
**shortcuts identifier**: `is.workflow.actions.ask`

params:

* default_answer
* input_type
* question

## Base64DecodeAction

Base64 decode

**keyword**: `base64_decode`
**shortcuts identifier**: `is.workflow.actions.base64decode`

## Base64EncodeAction

Base64 encode

**keyword**: `base64_encode`
**shortcuts identifier**: `is.workflow.actions.base64encode`

## CommentAction

Comment: just a comment

**keyword**: `comment`
**shortcuts identifier**: `is.workflow.actions.comment`

params:

* text

## CountAction

Count

**keyword**: `count`
**shortcuts identifier**: `is.workflow.actions.count`

params:

* count

## CreateFolderAction

Create folder

**keyword**: `create_folder`
**shortcuts identifier**: `is.workflow.actions.file.createfolder`

params:

* path

## DateAction

Date

**keyword**: `date`
**shortcuts identifier**: `is.workflow.actions.date`

## GetLastPhotoAction

Get latest photos

**keyword**: `get_last_photo`
**shortcuts identifier**: `is.workflow.actions.getlastphoto`

## GetDictionaryValueAction

Get dictionary value

**keyword**: `get_value_for_key`
**shortcuts identifier**: `is.workflow.actions.getvalueforkey`

params:

* key

## ReadFileAction

Get file

**keyword**: `read_file`
**shortcuts identifier**: `is.workflow.actions.documentpicker.open`

params:

* not_found_error
* path
* show_picker

## SaveFileAction

Save file

**keyword**: `save_file`
**shortcuts identifier**: `is.workflow.actions.documentpicker.save`

params:

* overwrite
* path
* show_picker

## SelectPhotoAction

Select photos

**keyword**: `select_photo`
**shortcuts identifier**: `is.workflow.actions.selectphoto`

## SetVariableAction

Set variable: saves input to a variable with a name=`name`

**keyword**: `set_variable`
**shortcuts identifier**: `is.workflow.actions.setvariable`

params:

* name

## ShowResultAction

Show result: shows a result

**keyword**: `show_result`
**shortcuts identifier**: `is.workflow.actions.showresult`

params:

* text

## CameraAction

Take photo

**keyword**: `take_photo`
**shortcuts identifier**: `is.workflow.actions.takephoto`

## TextAction

Text: returns text as an output

**keyword**: `text`
**shortcuts identifier**: `is.workflow.actions.gettext`

params:

* text

## URLAction

URL: returns url as an output

**keyword**: `url`
**shortcuts identifier**: `is.workflow.actions.url`

params:

* url
