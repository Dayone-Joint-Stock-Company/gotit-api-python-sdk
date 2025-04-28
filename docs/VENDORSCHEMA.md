# VENDORSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.vendorschema import VENDORSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VENDORSCHEMA from a JSON string
vendorschema_instance = VENDORSCHEMA.from_json(json)
# print the JSON string representation of the object
print(VENDORSCHEMA.to_json())

# convert the object into a dict
vendorschema_dict = vendorschema_instance.to_dict()
# create an instance of VENDORSCHEMA from a dict
vendorschema_from_dict = VENDORSCHEMA.from_dict(vendorschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


