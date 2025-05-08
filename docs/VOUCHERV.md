# VOUCHERV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_name** | **str** | Order name from client request | [optional] 
**vouchers** | [**List[VOUCHERVSCHEMA]**](VOUCHERVSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.voucherv import VOUCHERV

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERV from a JSON string
voucherv_instance = VOUCHERV.from_json(json)
# print the JSON string representation of the object
print(VOUCHERV.to_json())

# convert the object into a dict
voucherv_dict = voucherv_instance.to_dict()
# create an instance of VOUCHERV from a dict
voucherv_from_dict = VOUCHERV.from_dict(voucherv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


