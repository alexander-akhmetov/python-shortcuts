from typing import Dict, Type

from shortcuts import exceptions
from shortcuts.actions.base import BaseAction


class ActionsRegistry:
    def __init__(self):
        """
        _keyword_to_action_map looks simple: Dict[keyword, action]

        but _itype_to_action_map is more complex. Sometimes actions in the Shortcuts app
        have the same itype, but different name and behavior.

        They have different field in parameters, for example 'WFEncodeMode' in is.workflow.actions.base64encode
        can have values "Encode" or "Decode". For python-shortcuts they are different action classes.
        When action class is being registered, ActionsRegistry checks attribute "_additional_identifier_field"
        and based on this stores information.

        So to find proper class ActionsRegistry stores _itype_to_action_map in this format:

        _itype_to_action_map = {
            'some-itype': {
                # simple itype -> class mapping
                'type': 'class',
                'value': FirstAction,
            },
            'another-itype': {
                # more complex situation, the same itype,
                # but different classes defined by WFEncodeMode field
                'type': 'property_based',
                'field': 'WFEncodeMode',
                'value': {
                    'Encode': Base64EncodeAction,
                    'Decode': Base64DecodeAction,
                },
            }
        }

        """
        self._keyword_to_action_map: Dict[str, Type[BaseAction]] = {}
        self._itype_to_action_map = {}

    def register_action(self, action_class: Type[BaseAction]) -> None:
        '''Registers action class in the registry'''
        self._keyword_to_action_map[action_class.keyword] = action_class    # type: ignore

        if action_class._additional_identifier_field:
            self._create_class_field_if_needed(action_class)
            field_value = action_class.default_fields[action_class._additional_identifier_field]
            self._itype_to_action_map[action_class.itype]['value'][field_value] = action_class
            if action_class._default_class:
                self._itype_to_action_map[action_class.itype]['value'][None] = action_class
        else:
            self._itype_to_action_map[action_class.itype] = {
                'type': 'class',
                'value': action_class,
            }

    def _create_class_field_if_needed(self, action_class: Type[BaseAction]) -> None:
        '''creates all necessary fields for itype in _itype_to_action_map'''
        if action_class.itype in self._itype_to_action_map:
            return

        self._itype_to_action_map[action_class.itype] = {
            'type': 'property_based',
            'field': action_class._additional_identifier_field,
            'value': {},
        }

    def get_by_itype(self, itype: str, action_params: Dict) -> Type[BaseAction]:
        '''Returns action class by itype and plist parameters'''
        class_info = self._itype_to_action_map.get(itype)
        if not class_info:
            raise exceptions.UnknownActionError(itype, action_dict=action_params)

        value_type = class_info.get('type')

        if value_type == 'class':
            return class_info['value']
        elif value_type == 'property_based':
            params = action_params.get('WFWorkflowActionParameters', {})
            field_value = params.get(class_info['field'])
            if field_value in class_info['value']:
                return class_info['value'][field_value]

        raise exceptions.UnknownActionError(itype, action_dict=action_params)

    def get_by_keyword(self, keyword: str) -> Type[BaseAction]:
        '''Returns action class by keyword'''
        if keyword not in self._keyword_to_action_map:
            raise exceptions.UnknownActionError(keyword)
        return self._keyword_to_action_map[keyword]

    @property
    def actions(self):
        return [a for _, a in sorted(self._keyword_to_action_map.items())]
