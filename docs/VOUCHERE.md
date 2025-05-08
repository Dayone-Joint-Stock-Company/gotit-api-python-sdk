# VOUCHERE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ref_id** | **str** | TransactionRefId receive from client request | [optional] 
**vouchers** | [**List[VOUCHERESCHEMA]**](VOUCHERESCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchere import VOUCHERE

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERE from a JSON string
vouchere_instance = VOUCHERE.from_json(json)
# print the JSON string representation of the object
print(VOUCHERE.to_json())

# convert the object into a dict
vouchere_dict = vouchere_instance.to_dict()
# create an instance of VOUCHERE from a dict
vouchere_from_dict = VOUCHERE.from_dict(vouchere_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


