# VOUCHERESCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_link** | **str** | Voucher of link e | [optional] 
**voucher_cover_link** | **str** | Voucher cover of link e | [optional] 
**voucher_serial** | **str** | Voucher serial of link e | [optional] 
**value** | **str** | Voucher value of link e | [optional] 
**expired_date** | **str** | Expiry date of voucher link Format: &#39;YYYY-MM-DD&#39; | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchereschema import VOUCHERESCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERESCHEMA from a JSON string
vouchereschema_instance = VOUCHERESCHEMA.from_json(json)
# print the JSON string representation of the object
print(VOUCHERESCHEMA.to_json())

# convert the object into a dict
vouchereschema_dict = vouchereschema_instance.to_dict()
# create an instance of VOUCHERESCHEMA from a dict
vouchereschema_from_dict = VOUCHERESCHEMA.from_dict(vouchereschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


