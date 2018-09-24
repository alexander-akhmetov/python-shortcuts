from shortcuts.actions import (
    GetBatteryLevelAction,
    GetIPAddressAction,
    GetDeviceDetailsAction,
    SetAirplaneModeAction,
    SetBluetoothAction,
    SetLowPowerModeAction,
    SetMobileDataAction,
    SetWiFiAction,
    SetTorchAction,
    SetDoNotDisturbAction,
    SetBrightnessAction,
    SetVolumeAction,
)

from tests.conftest import ActionTomlLoadsMixin


class TestGetBatteryLevelAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = GetBatteryLevelAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.getbatterylevel',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "get_battery_level"
        '''
        self._assert_toml_loads(toml, GetBatteryLevelAction, {})


class TestGetIPAddressAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = GetIPAddressAction(data={'source': 'Global', 'address_type': 'IPv6'})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.getipaddress',
            'WFWorkflowActionParameters': {
                'WFIPAddressTypeOption': 'IPv6',
                'WFIPAddressSourceOption': 'Global',
            },
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "get_ip_address"
        source = "Local"
        address_type = "IPv4"
        '''
        self._assert_toml_loads(toml, GetIPAddressAction, {'source': 'Local', 'address_type': 'IPv4'})


class TestGetDeviceDetailsAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = GetDeviceDetailsAction(data={'detail': 'Device Name'})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.getdevicedetails',
            'WFWorkflowActionParameters': {'WFDeviceDetail': 'Device Name'},
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        details = (
            'Device Name', 'Device Model', 'System Version',
            'Screen Width', 'Screen Height', 'Current Volume',
            'Current Brightness',
        )
        for detail_name in details:
            toml = f'''
            [[action]]
            type = "get_device_details"
            detail = "{detail_name}"
            '''
            self._assert_toml_loads(toml, GetDeviceDetailsAction, {'detail': detail_name})


class TestBooleanSwitchAction(ActionTomlLoadsMixin):
    def _assert_dump(self, cls, expected_id):
        for mode in (True, False):
            action = cls(data={'on': mode})
            exp_dump = {
                'WFWorkflowActionIdentifier': expected_id,
                'WFWorkflowActionParameters': {'OnValue': mode},
            }
            assert action.dump() == exp_dump

    def _assert_loads_toml(self, cls, keyword):
        for mode in (True, False):
            toml = f'''
            [[action]]
            type = "{keyword}"
            on = {str(mode).lower()}
            '''
            self._assert_toml_loads(toml, cls, {'on': mode})


class TestSetAirplaneModeAction(TestBooleanSwitchAction):
    def test_dumps(self):
        self._assert_dump(SetAirplaneModeAction, 'is.workflow.actions.airplanemode.set')

    def test_loads_toml(self):
        self._assert_loads_toml(SetAirplaneModeAction, 'set_airplane_mode')


class TestSetBluetoothAction(TestBooleanSwitchAction):
    def test_dumps(self):
        self._assert_dump(SetBluetoothAction, 'is.workflow.actions.bluetooth.set')

    def test_loads_toml(self):
        self._assert_loads_toml(SetBluetoothAction, 'set_bluetooth')


class TestSetMobileDataAction(TestBooleanSwitchAction):
    def test_dumps(self):
        self._assert_dump(SetMobileDataAction, 'is.workflow.actions.cellulardata.set')

    def test_loads_toml(self):
        self._assert_loads_toml(SetMobileDataAction, 'set_mobile_data')


class TestSetLowPowerModeAction(TestBooleanSwitchAction):
    def test_dumps(self):
        self._assert_dump(SetLowPowerModeAction, 'is.workflow.actions.lowpowermode.set')

    def test_loads_toml(self):
        self._assert_loads_toml(SetLowPowerModeAction, 'set_low_power_mode')


class TestSetWiFiAction(TestBooleanSwitchAction):
    def test_dumps(self):
        self._assert_dump(SetWiFiAction, 'is.workflow.actions.wifi.set')

    def test_loads_toml(self):
        self._assert_loads_toml(SetWiFiAction, 'set_wifi')


class TestSetTorchAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        for mode in ('Off', 'On', 'Toggle'):
            action = SetTorchAction(data={'mode': mode})
            exp_dump = {
                'WFWorkflowActionIdentifier': 'is.workflow.actions.flashlight',
                'WFWorkflowActionParameters': {'WFFlashlightSetting': mode},
            }
            assert action.dump() == exp_dump

    def test_loads_toml(self):
        modes = ('Off', 'On', 'Toggle')
        for mode in modes:
            toml = f'''
            [[action]]
            type = "set_torch"
            mode = "{mode}"
            '''
            self._assert_toml_loads(toml, SetTorchAction, {'mode': mode})


class TestSetDoNotDisturbAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        for mode in (True, False):
            action = SetDoNotDisturbAction(data={'enabled': mode})
            exp_dump = {
                'WFWorkflowActionIdentifier': 'is.workflow.actions.dnd.set',
                'WFWorkflowActionParameters': {'Enabled': mode, 'AssertionType': 'Turned Off'},
            }
            assert action.dump() == exp_dump

    def test_loads_toml(self):
        for mode in (True, False):
            toml = f'''
            [[action]]
            type = "set_do_not_disturb"
            enabled = {str(mode).lower()}
            '''
            self._assert_toml_loads(toml, SetDoNotDisturbAction, {'enabled': mode})


class TestSetVolumeAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        level = 87.56
        action = SetVolumeAction(data={'level': level})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.setvolume',
            'WFWorkflowActionParameters': {'WFVolume': level},
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "set_volume"
        level = 51.10
        '''
        self._assert_toml_loads(toml, SetVolumeAction, {'level': 51.10})


class TestSetBrightnessAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        level = 87.56
        action = SetBrightnessAction(data={'level': level})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.setbrightness',
            'WFWorkflowActionParameters': {'WFBrightness': level},
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "set_brightness"
        level = 55.21
        '''
        self._assert_toml_loads(toml, SetBrightnessAction, {'level': 55.21})
