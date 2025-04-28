# PRODUCTSVOUCHERCHECK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | Product Id | [optional] 
**product_nm** | **str** | Product Name | [optional] 
**product_img** | **str** | Link product image | [optional] 
**brand_id** | **int** | Brand id | [optional] 
**brand_nm** | **str** | Brand name | [optional] 
**brand_service_guide** | **str** |  | [optional] 
**price** | [**PRODUCTPRICESCHEMA**](PRODUCTPRICESCHEMA.md) |  | [optional] 
**product_desc** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**store_list** | [**List[STOREPRODUCTSCHEMA]**](STOREPRODUCTSCHEMA.md) |  | [optional] 
**total_store** | **int** |  | [optional] 
**store_pagination** | [**STOREPAGINGSCHEMA**](STOREPAGINGSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.productsvouchercheck import PRODUCTSVOUCHERCHECK

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTSVOUCHERCHECK from a JSON string
productsvouchercheck_instance = PRODUCTSVOUCHERCHECK.from_json(json)
# print the JSON string representation of the object
print(PRODUCTSVOUCHERCHECK.to_json())

# convert the object into a dict
productsvouchercheck_dict = productsvouchercheck_instance.to_dict()
# create an instance of PRODUCTSVOUCHERCHECK from a dict
productsvouchercheck_from_dict = PRODUCTSVOUCHERCHECK.from_dict(productsvouchercheck_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


