# VOUCHERG


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_name** | **str** | Order name from client request | [optional] 
**vouchers** | [**List[VOUCHERGSCHEMA]**](VOUCHERGSCHEMA.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.voucherg import VOUCHERG

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERG from a JSON string
voucherg_instance = VOUCHERG.from_json(json)
# print the JSON string representation of the object
print(VOUCHERG.to_json())

# convert the object into a dict
voucherg_dict = voucherg_instance.to_dict()
# create an instance of VOUCHERG from a dict
voucherg_from_dict = VOUCHERG.from_dict(voucherg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


