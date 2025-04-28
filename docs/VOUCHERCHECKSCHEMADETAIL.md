# VOUCHERCHECKSCHEMADETAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ref_id** | **str** | TransactionRefId receive from client request | [optional] 
**voucher_code** | **str** | Voucher code. Contains 10 numbers, unique and not duplicated with any other voucher. For some brands that do not use Got It code but use integerernal code (Big C, Mobile World), the system returns the integerernal code. | [optional] 
**voucher_link** | **str** | Link of voucher | [optional] 
**voucher_cover_link** | **str** | Cover link of voucher. | [optional] 
**voucher_serial** | **str** | Is a unique code to identify voucher link v and is not valid for use. For example: V1562342ET2 | [optional] 
**group_link** | **str** | https://e-stg.gotit.vn/gLsZaFRN | [optional] 
**group_voucher_serial** | **str** | E2V2RML6F52 | [optional] 
**group_cover_link** | **str** | https://e-stg.gotit.vn/gLsZaFRN | [optional] 
**voucher_link_code** | **str** | Last 8 characters of voucher link | [optional] 
**voucher_image_link** | **str** | Link of voucher image. To display vouchers as images | [optional] 
**expiry_date** | **str** | Voucher expiration date | [optional] 
**state_code** | **int** | State Code | [optional] 
**state_text** | **str** | State Text | [optional] 
**used_store** | [**List[STORESSCHEMA]**](STORESSCHEMA.md) |  | [optional] 
**used_time** | **str** | Used Time | [optional] 
**used_brand** | **str** | State Text | [optional] 
**product** | [**PRODUCTV**](PRODUCTV.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vouchercheckschemadetail import VOUCHERCHECKSCHEMADETAIL

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERCHECKSCHEMADETAIL from a JSON string
vouchercheckschemadetail_instance = VOUCHERCHECKSCHEMADETAIL.from_json(json)
# print the JSON string representation of the object
print(VOUCHERCHECKSCHEMADETAIL.to_json())

# convert the object into a dict
vouchercheckschemadetail_dict = vouchercheckschemadetail_instance.to_dict()
# create an instance of VOUCHERCHECKSCHEMADETAIL from a dict
vouchercheckschemadetail_from_dict = VOUCHERCHECKSCHEMADETAIL.from_dict(vouchercheckschemadetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


