# VOUCHERCHECKSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ref_id** | **str** | TransactionRefId receive from client request | [optional] 
**vouchers** | [**List[VOUCHERCHECKSCHEMADETAIL]**](VOUCHERCHECKSCHEMADETAIL.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchercheckschema import VOUCHERCHECKSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERCHECKSCHEMA from a JSON string
vouchercheckschema_instance = VOUCHERCHECKSCHEMA.from_json(json)
# print the JSON string representation of the object
print(VOUCHERCHECKSCHEMA.to_json())

# convert the object into a dict
vouchercheckschema_dict = vouchercheckschema_instance.to_dict()
# create an instance of VOUCHERCHECKSCHEMA from a dict
vouchercheckschema_from_dict = VOUCHERCHECKSCHEMA.from_dict(vouchercheckschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


