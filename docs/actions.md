
# Supported Actions

This is a list of all actions supported by **python-shortcuts**.

Legend:

* *keyword*: This keyword you can use in `toml` files to describe action
* *shortcuts identifier*: (*itype*) this identifier will be used to generate an action in a shortcut

System variables:

* `{{ask_when_run}}` - ask the user for an input when the shortcut is running.

----

### ShowAlertAction

Show alert

**keyword**: `alert`
**shortcuts identifier**: `is.workflow.actions.alert`

params:

* show_cancel_button (*required*)
* text (*required*)
* title (*required*)

### AskAction

Ask for input

**keyword**: `ask`
**shortcuts identifier**: `is.workflow.actions.ask`

params:

* default_answer (*variables support*)
* input_type ()
* question (*required*)

### Base64DecodeAction

Base64 decode

**keyword**: `base64_decode`
**shortcuts identifier**: `is.workflow.actions.base64encode`

### Base64EncodeAction

Base64 encode

**keyword**: `base64_encode`
**shortcuts identifier**: `is.workflow.actions.base64encode`

### CommentAction

Comment: just a comment

**keyword**: `comment`
**shortcuts identifier**: `is.workflow.actions.comment`

params:

* text (*required*)

### ContinueInShortcutAppAction

Continue in shortcut app

**keyword**: `continue_in_shortcut_app`
**shortcuts identifier**: `is.workflow.actions.handoff`

### ImageConvertAction

Image convert

**keyword**: `convert_image`
**shortcuts identifier**: `is.workflow.actions.image.convert`

params:

* compression_quality (*required*)
* format (*required*)
* preserve_metadata (*required*)

### CountAction

Count

**keyword**: `count`
**shortcuts identifier**: `is.workflow.actions.count`

params:

* count (*required*)

### CreateFolderAction

Create folder

**keyword**: `create_folder`
**shortcuts identifier**: `is.workflow.actions.file.createfolder`

params:

* path (*required*, *variables support*)

### DateAction

Date

**keyword**: `date`
**shortcuts identifier**: `is.workflow.actions.date`

params:

* default_answer (*variables support*)

### DelayAction

Delay

**keyword**: `delay`
**shortcuts identifier**: `is.workflow.actions.delay`

params:

* time (*required*)

### DictionaryAction

Dictionary

**keyword**: `dictionary`
**shortcuts identifier**: `is.workflow.actions.dictionary`

params:

* items (*required*)

### ElseAction

Else

**keyword**: `else`
**shortcuts identifier**: `is.workflow.actions.conditional`

params:

* group_id ()

### MenuEndAction

End menu

**keyword**: `end_menu`
**shortcuts identifier**: `is.workflow.actions.choosefrommenu`

params:

* group_id ()

### EndIfAction

EndIf: end a condition

**keyword**: `endif`
**shortcuts identifier**: `is.workflow.actions.conditional`

params:

* group_id ()

### ExitAction

Exit

**keyword**: `exit`
**shortcuts identifier**: `is.workflow.actions.exit`

### FormatDateAction

Format date

**keyword**: `format_date`
**shortcuts identifier**: `is.workflow.actions.format.date`

params:

* format (*required*)

### GetBatteryLevelAction

Get battery level

**keyword**: `get_battery_level`
**shortcuts identifier**: `is.workflow.actions.getbatterylevel`

### GetDeviceDetailsAction

Get device details

**keyword**: `get_device_details`
**shortcuts identifier**: `is.workflow.actions.getdevicedetails`

params:

* detail (*required*)  | _choices_:

  * "Device Name"

  * "Device Model"

  * "System Version"

  * "Screen Width"

  * "Screen Height"

  * "Current Volume"

  * "Current Brightness"

### GetIPAddressAction

Get current IP address

**keyword**: `get_ip_address`
**shortcuts identifier**: `is.workflow.actions.getipaddress`

params:

* address_type (*required*)  | _choices_:

  * "IPv4"

  * "IPv6"
* source (*required*)  | _choices_:

  * "Local"

  * "Global"

### GetLastPhotoAction

Get latest photos

**keyword**: `get_last_photo`
**shortcuts identifier**: `is.workflow.actions.getlastphoto`

### GetURLAction

Get URL

**keyword**: `get_url`
**shortcuts identifier**: `is.workflow.actions.downloadurl`

params:

* advanced ()
* form ()
* headers ()
* json ()
* method ()

### GetDictionaryValueAction

Get dictionary value

**keyword**: `get_value_for_key`
**shortcuts identifier**: `is.workflow.actions.getvalueforkey`

params:

* key (*required*)

### GetVariableAction

Get variable: returns variable with name=`name` in the output

**keyword**: `get_variable`
**shortcuts identifier**: `is.workflow.actions.getvariable`

params:

* name (*required*)

### IfAction

If

**keyword**: `if`
**shortcuts identifier**: `is.workflow.actions.conditional`

params:

* compare_with (*required*)
* condition (*required*)  | _choices_:

  * "Equals"

  * "Contains"
* group_id ()

### MenuItemAction


    Menu item

    You must specify the title for the item.
    After this action write all actions which you want to be executed when a user selects this option in the menu.
    

**keyword**: `menu_item`
**shortcuts identifier**: `is.workflow.actions.choosefrommenu`

params:

* group_id ()
* title (*required*)

### NothingAction

Nothing

**keyword**: `nothing`
**shortcuts identifier**: `is.workflow.actions.nothing`

### PreviewDocumentAction

Preview document

**keyword**: `preview`
**shortcuts identifier**: `is.workflow.actions.previewdocument`

### ReadFileAction

Get file

**keyword**: `read_file`
**shortcuts identifier**: `is.workflow.actions.documentpicker.open`

params:

* not_found_error (*required*)
* path (*required*, *variables support*)
* show_picker (*required*)

### RepeatEndAction

Repeat

**keyword**: `repeat_end`
**shortcuts identifier**: `is.workflow.actions.repeat.count`

params:

* group_id ()

### RepeatStartAction

Repeat

**keyword**: `repeat_start`
**shortcuts identifier**: `is.workflow.actions.repeat.count`

params:

* count (*required*)
* group_id ()

### SaveFileAction

Save file

**keyword**: `save_file`
**shortcuts identifier**: `is.workflow.actions.documentpicker.save`

params:

* overwrite (*required*)
* path (*required*, *variables support*)
* show_picker (*required*)

### SelectPhotoAction

Select photos

**keyword**: `select_photo`
**shortcuts identifier**: `is.workflow.actions.selectphoto`

### SendMessageAction

Send Message

**keyword**: `send_message`
**shortcuts identifier**: `is.workflow.actions.sendmessage`

params:

* recepients (*required*, *variables support*)
* text (*required*, *variables support*)

### SetAirplaneModeAction

Set airplane mode

**keyword**: `set_airplane_mode`
**shortcuts identifier**: `is.workflow.actions.airplanemode.set`

params:

* on (*required*)

### SetBluetoothAction

Set bluetooth

**keyword**: `set_bluetooth`
**shortcuts identifier**: `is.workflow.actions.bluetooth.set`

params:

* on (*required*)

### SetBrightnessAction

Set brightness

**keyword**: `set_brightness`
**shortcuts identifier**: `is.workflow.actions.setbrightness`

params:

* level (*required*)

### SetDoNotDisturbAction

Set Do Not Disturb

**keyword**: `set_do_not_disturb`
**shortcuts identifier**: `is.workflow.actions.dnd.set`

params:

* enabled (*required*)

### SetItemNameAction

Set item name

**keyword**: `set_item_name`
**shortcuts identifier**: `is.workflow.actions.setitemname`

### SetLowPowerModeAction

Set Low Power mode

**keyword**: `set_low_power_mode`
**shortcuts identifier**: `is.workflow.actions.lowpowermode.set`

params:

* on (*required*)

### SetMobileDataAction

Set mobile data

**keyword**: `set_mobile_data`
**shortcuts identifier**: `is.workflow.actions.cellulardata.set`

params:

* on (*required*)

### SetTorchAction

Set Torch

**keyword**: `set_torch`
**shortcuts identifier**: `is.workflow.actions.flashlight`

params:

* mode (*required*)  | _choices_:

  * "Off"

  * "On"

  * "Toggle"

### SetVariableAction

Set variable: saves input to a variable with a name=`name`

**keyword**: `set_variable`
**shortcuts identifier**: `is.workflow.actions.setvariable`

params:

* name (*required*)

### SetVolumeAction

Set volume

**keyword**: `set_volume`
**shortcuts identifier**: `is.workflow.actions.setvolume`

params:

* level (*required*)

### SetWiFiAction

Set WiFi

**keyword**: `set_wifi`
**shortcuts identifier**: `is.workflow.actions.wifi.set`

params:

* on (*required*)

### ShowResultAction

Show result: shows a result

**keyword**: `show_result`
**shortcuts identifier**: `is.workflow.actions.showresult`

params:

* text (*required*, *variables support*)

### MenuStartAction


    Start menu

    To build a menu, you have to write at least three actions:
        * Start menu
        * Menu item
        * End menu

    So the menu with two items will look like:

        ```
        Start menu

        Menu item title=1
            ... some actions...

        Menu item title=2
            ...other actions...

        End menu
        ```

    As in other actions which have `group_id` field, you don't need to specify it, it will be generated automatically.
    

**keyword**: `start_menu`
**shortcuts identifier**: `is.workflow.actions.choosefrommenu`

params:

* group_id ()
* menu_items (*required*)

### CameraAction

Take photo

**keyword**: `take_photo`
**shortcuts identifier**: `is.workflow.actions.takephoto`

### TextAction

Text: returns text as an output

**keyword**: `text`
**shortcuts identifier**: `is.workflow.actions.gettext`

params:

* text (*required*, *variables support*)

### URLAction

URL: returns url as an output

**keyword**: `url`
**shortcuts identifier**: `is.workflow.actions.url`

params:

* url (*required*)

### VibrateAction

Vibrate

**keyword**: `vibrate`
**shortcuts identifier**: `is.workflow.actions.vibrate`

### ViewContentGraphAction

View content graph

**keyword**: `view_content_graph`
**shortcuts identifier**: `is.workflow.actions.viewresult`

### WaitToReturnAction

Wait to return

**keyword**: `wait_to_return`
**shortcuts identifier**: `is.workflow.actions.waittoreturn`
