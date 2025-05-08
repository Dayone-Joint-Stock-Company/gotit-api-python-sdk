# STORESSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **int** | Store Id | [optional] 
**store_nm** | **str** | Store Name | [optional] 
**store_addr** | **str** | Store Address | [optional] 
**store_em** | **str** | Store Email | [optional] 
**store_ph** | **str** | Store Phone | [optional] 
**lat** | **float** | Lat location on Google maps | [optional] 
**long** | **float** | Long location on Google maps | [optional] 
**brand_nm** | **str** | Brand Name | [optional] 
**district_id** | **int** | District code (Got It identifier) | [optional] 
**district_nm** | **str** | District name | [optional] 
**city_id** | **int** | City code (Got It identifier) | [optional] 
**city_nm** | **str** | City name | [optional] 

## Example

```python
from gotit_api_python_sdk.models.storesschema import STORESSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of STORESSCHEMA from a JSON string
storesschema_instance = STORESSCHEMA.from_json(json)
# print the JSON string representation of the object
print(STORESSCHEMA.to_json())

# convert the object into a dict
storesschema_dict = storesschema_instance.to_dict()
# create an instance of STORESSCHEMA from a dict
storesschema_from_dict = STORESSCHEMA.from_dict(storesschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


