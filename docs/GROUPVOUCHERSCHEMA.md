# GROUPVOUCHERSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_link** | **str** | Link of voucher | [optional] 
**voucher_link_code** | **str** | Last 8 characters of voucher link | [optional] 
**voucher_serial** | **str** | Is a unique code to identify voucher link v and is not valid for use. For example: V1562342ET2 | [optional] 

## Example

```python
from gotit_api_sdk_python.models.groupvoucherschema import GROUPVOUCHERSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of GROUPVOUCHERSCHEMA from a JSON string
groupvoucherschema_instance = GROUPVOUCHERSCHEMA.from_json(json)
# print the JSON string representation of the object
print(GROUPVOUCHERSCHEMA.to_json())

# convert the object into a dict
groupvoucherschema_dict = groupvoucherschema_instance.to_dict()
# create an instance of GROUPVOUCHERSCHEMA from a dict
groupvoucherschema_from_dict = GROUPVOUCHERSCHEMA.from_dict(groupvoucherschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


