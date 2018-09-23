from shortcuts.actions.base import BaseAction, BooleanField, Field, VariablesField


class URLAction(BaseAction):
    '''URL: returns url as an output'''
    type = 'is.workflow.actions.url'
    keyword = 'url'

    url = Field('WFURLActionURL')


# {'Value': {'WFDictionaryFieldValueItems': [{'WFItemType': 0,
# 'WFKey': {'Value': {'attachmentsByRange': {},
#                     'string': 'test_header'},
#         'WFSerializationType': 'WFTextTokenString'},
# 'WFValue': {'Value': {'attachmentsByRange': {},
#                     'string': 'header_value'},
#             'WFSerializationType': 'WFTextTokenString'}}]},
# 'WFSerializationType': 'WFDictionaryFieldValue'},

class HeaderField(VariablesField):
    def process_value(self, value):
        return {
            'Value': {
                'WFDictionaryFieldValueItems': [self._process_single_value(v) for v in value],
            },
            'WFSerializationType': 'WFTextTokenString',
        }

    def _process_single_value(self, value):
        key = super().process_value(value['key'])
        value = super().process_value(value['value'])
        return {
            'Value': {
                'WFDictionaryFieldValueItems': [
                    {
                        'WFItemType': 0,
                        'WFKey': key,
                        'WFValue': value,
                    }
                ],
            },
            'WFSerializationType': 'WFTextTokenString',
        }


class DownloadURLAction(BaseAction):
    '''Download URL'''
    type = 'is.workflow.actions.downloadurl'
    keyword = 'download_url'

    advanced = BooleanField('Advanced')
    method = Field('WFHTTPMethod')
