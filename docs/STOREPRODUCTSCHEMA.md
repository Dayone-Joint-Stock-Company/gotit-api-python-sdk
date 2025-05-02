# STOREPRODUCTSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **int** | Store Id | [optional] 
**store_nm** | **str** | Store Name | [optional] 
**store_addr** | **str** | Store Address | [optional] 
**lat** | **float** | Lat location on Google maps | [optional] 
**long** | **float** | Long location on Google maps | [optional] 
**phone** | **str** | Store Phone | [optional] 
**city_id** | **int** | City code (Got It identifier) | [optional] 
**city** | **str** | City name | [optional] 
**dist_id** | **int** | District code (Got It identifier) | [optional] 
**district** | **str** | District name | [optional] 

## Example

```python
from gotit_api_python_sdk.models.storeproductschema import STOREPRODUCTSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of STOREPRODUCTSCHEMA from a JSON string
storeproductschema_instance = STOREPRODUCTSCHEMA.from_json(json)
# print the JSON string representation of the object
print(STOREPRODUCTSCHEMA.to_json())

# convert the object into a dict
storeproductschema_dict = storeproductschema_instance.to_dict()
# create an instance of STOREPRODUCTSCHEMA from a dict
storeproductschema_from_dict = STOREPRODUCTSCHEMA.from_dict(storeproductschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


