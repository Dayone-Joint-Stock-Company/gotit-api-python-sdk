# PRODUCTSDEFAULTLINKG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_image** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**price_id** | **str** |  | [optional] 
**value** | **int** |  | [optional] 
**expired_date** | **str** |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.productsdefaultlinkg import PRODUCTSDEFAULTLINKG

# TODO update the JSON string below
json = "{}"
# create an instance of PRODUCTSDEFAULTLINKG from a JSON string
productsdefaultlinkg_instance = PRODUCTSDEFAULTLINKG.from_json(json)
# print the JSON string representation of the object
print(PRODUCTSDEFAULTLINKG.to_json())

# convert the object into a dict
productsdefaultlinkg_dict = productsdefaultlinkg_instance.to_dict()
# create an instance of PRODUCTSDEFAULTLINKG from a dict
productsdefaultlinkg_from_dict = PRODUCTSDEFAULTLINKG.from_dict(productsdefaultlinkg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


