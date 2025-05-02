# VOUCHERGSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order Id | [optional] 
**order_name** | **str** | Order name from client request | [optional] 
**group_vouchers** | [**GROUPVOUCHERSCHEMA**](GROUPVOUCHERSCHEMA.md) |  | [optional] 
**vouchers** | [**List[PRODUCTG]**](PRODUCTG.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.vouchergschema import VOUCHERGSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of VOUCHERGSCHEMA from a JSON string
vouchergschema_instance = VOUCHERGSCHEMA.from_json(json)
# print the JSON string representation of the object
print(VOUCHERGSCHEMA.to_json())

# convert the object into a dict
vouchergschema_dict = vouchergschema_instance.to_dict()
# create an instance of VOUCHERGSCHEMA from a dict
vouchergschema_from_dict = VOUCHERGSCHEMA.from_dict(vouchergschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


