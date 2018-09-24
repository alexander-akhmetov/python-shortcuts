# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
