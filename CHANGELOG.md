# Changelog

## [0.11.0] 05.03.2019

- Added dockerized cli tool

- New actions:
  - Choose From List
  - Open App

## [0.10.0] 26.10.2018

- Added new example: database [ShortcutDB](/examples/ShortcutDB.md). Get version with auto update feature and read documentation on [the website](https://shortcutdb.aleks.sh)

- Added system variables:
  - `shortcut_input`
  - `clipboard`
  - `current_date`

- New actions:
  - AppendFileAction
  - GetDictionaryFromInputAction
  - RunShortcut
  - GetMyShortcutsAction
  - GetTimeBetweenDates
  - DetectDateAction
  - OpenURLAction

- `IfAction` now supports variables in the parameter `compare_with`.

## [0.9.1] 27.09.2018

- Now raises `UnknownWFTextTokenAttachment` error when loader can't load field with unknown token attachment type.

## [0.9.0] 27.09.2018

- Added [fields documentation](/docs/fields.md)
- New actions:
  - RepeatEachStartAction
  - RepeatEachEndAction
  - ChangeCaseAction
  - SplitTextAction
  - GetClipboardAction
  - NumberAction
  - HashAction
  - SetClipboardAction
  - SetDictionaryValueAction
  - URLEncodeAction
  - URLDecodeAction
  - AppendVariableAction
  - ShowDefinitionAction
  - ScanQRBarCode
  - GetTextFromInputAction
  - GetNameOfEmoji
  - DetectLanguageAction
  - ExpandURLAction

## [0.8.1] - 26.09.2018

- Save shortcut from URL without deserializing if output format is plist

## [0.8.0] - 25.09.2018

- New example: [shields.toml](/examples/shields.toml)
- New action: SpeakTextAction
- Added `default=True` to field `SetLowPowerModeAction.on`.
- Removed `plutil` requirement
- Added ability to download shortcuts with `shortcuts` cli directly from iCloud

## [0.7.0] - 25.09.2018

- New actions:
  - SendMessageAction
  - MenuStartAction
  - MenuItemAction
  - MenuEndAction
- New examples in the `/examples/` directory:
  - `send_photo.toml`: how to use `menu`, send photo with `send message` action and how to use `{{ask_when_run}}`
- Updated documentation about supported actions `/docs/actions.md`
- Supported `{{ask_when_run}}` system variable (read more about this in `/docs/actions.md`)

## [0.6.0] - 24.09.2018

- New actions:
  - GetBatteryLevelAction
  - GetIPAddressAction
  - GetDeviceDetailsAction
  - SetAirplaneModeAction
  - SetBluetoothAction
  - SetBrightnessAction
  - SetMobileDataAction
  - SetDoNotDisturbAction
  - SetTorchAction
  - SetLowPowerModeAction
  - SetVolumeAction
  - SetWiFiAction
  - NothingAction
  - SetItemNameAction
  - ViewContentGraphAction
  - ContinueInShortcutAppAction
  - DelayAction
  - WaitToReturnAction
  - RepeatStartAction
  - RepeatEndAction
- Renamed `type` to `itype` for action classes (class attribute *only*).
- Removed `required=True` from `group_id` fields, now conditional group sets automatically.
- Package name changed to `shortcuts`: `pip install shortcuts` (old name will be working too as an alias).

## [0.5.2] - 23.09.2018

- Fixed installation from pypi: returned back `toml` dependency

## [0.5.1] - 23.09.2018

- Fixed base64decode action

## [0.5.0] - 23.09.2018

- Fixed POST form data with GetURLAction

## [0.4.0] - 23.09.2018

- Added version inormation to the CLI tool

## [0.3.0] - 23.09.2018

- Added BooleanField
- Added DictionaryAction (only text items for now)
- Added GetURLAction (simple support, only json and headers)
- Added ExitAction
- Added VibrateAction
- Added FormatDateAction
- Added PreviewDocumentAction
- Added ImageConvertAction
- Added GetVariableAction

## [0.2.3] - 22.09.2018

- Fixed cli (`shortcuts`)

## [0.2.0] - 22.09.2018

- Working convertation toml <-> shortcut

## [0.1.0] - 22.09.2018

- It's alive!
