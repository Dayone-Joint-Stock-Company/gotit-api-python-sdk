# VOUCHERVSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ref_id** | **str** | TransactionRefId receive from client request | [optional] 
**voucher_code** | **str** | Voucher code. Contains 10 numbers, unique and not duplicated with any other voucher. For some brands that do not use Got It code but use integerernal code (Big C, Mobile World), the system returns the integerernal code. | [optional] 
**voucher_link** | **str** | Link of voucher | [optional] 
**voucher_link_code** | **str** | Last 8 characters of voucher link | [optional] 
**voucher_image_link** | **str** | Link of voucher image. To display vouchers as images | [optional] 
**voucher_cover_link** | **str** | Cover link of voucher. | [optional] 
**voucher_cover_link_code** | **str** | Last 8 characters of voucher cover link | [optional] 
**voucher_serial** | **str** | Is a unique code to identify voucher link v and is not valid for use. For example: V1562342ET2 | [optional] 
**expiry_date** | **str** | Voucher expiration date | [optional] 
**product** | [**VOUCHERVSCHEMAProduct**](VOUCHERVSCHEMAProduct.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchervschema import VOUCHERVSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERVSCHEMA from a JSON string
vouchervschema_instance = VOUCHERVSCHEMA.from_json(json)
# print the JSON string representation of the object
print(VOUCHERVSCHEMA.to_json())

# convert the object into a dict
vouchervschema_dict = vouchervschema_instance.to_dict()
# create an instance of VOUCHERVSCHEMA from a dict
vouchervschema_from_dict = VOUCHERVSCHEMA.from_dict(vouchervschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


