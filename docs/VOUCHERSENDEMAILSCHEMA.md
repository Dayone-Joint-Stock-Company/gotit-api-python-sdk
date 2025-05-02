# VOUCHERSENDEMAILSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_link_code** | **str** | Last 8 characters of voucher link | [optional] 
**email** | **str** | Email of user receive voucher | [optional] 
**receiver_nm** | **str** | Email of user receive voucher | [optional] 
**sender_nm** | **str** | Name of sender | [optional] 
**message** | **str** | Message send | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchersendemailschema import VOUCHERSENDEMAILSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERSENDEMAILSCHEMA from a JSON string
vouchersendemailschema_instance = VOUCHERSENDEMAILSCHEMA.from_json(json)
# print the JSON string representation of the object
print(VOUCHERSENDEMAILSCHEMA.to_json())

# convert the object into a dict
vouchersendemailschema_dict = vouchersendemailschema_instance.to_dict()
# create an instance of VOUCHERSENDEMAILSCHEMA from a dict
vouchersendemailschema_from_dict = VOUCHERSENDEMAILSCHEMA.from_dict(vouchersendemailschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


