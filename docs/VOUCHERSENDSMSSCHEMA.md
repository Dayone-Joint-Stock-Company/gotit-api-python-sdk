# VOUCHERSENDSMSSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_link_code** | **str** | Last 8 characters of voucher link | [optional] 
**phone_no** | **str** | Phone of user receive voucher | [optional] 
**receiver_nm** | **str** | Email of user receive voucher | [optional] 
**sender_nm** | **str** | Name of sender | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchersendsmsschema import VOUCHERSENDSMSSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERSENDSMSSCHEMA from a JSON string
vouchersendsmsschema_instance = VOUCHERSENDSMSSCHEMA.from_json(json)
# print the JSON string representation of the object
print(VOUCHERSENDSMSSCHEMA.to_json())

# convert the object into a dict
vouchersendsmsschema_dict = vouchersendsmsschema_instance.to_dict()
# create an instance of VOUCHERSENDSMSSCHEMA from a dict
vouchersendsmsschema_from_dict = VOUCHERSENDSMSSCHEMA.from_dict(vouchersendsmsschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


