# PRODUCTG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_image** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**price_id** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**expired_date** | **str** |  | [optional] 
**partner** | [**VENDORSCHEMA**](VENDORSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.productg import PRODUCTG

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTG from a JSON string
productg_instance = PRODUCTG.from_json(json)
# print the JSON string representation of the object
print(PRODUCTG.to_json())

# convert the object into a dict
productg_dict = productg_instance.to_dict()
# create an instance of PRODUCTG from a dict
productg_from_dict = PRODUCTG.from_dict(productg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


