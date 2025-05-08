# USAGEMETHODSCHEMA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of method used &#39;AT_STORE&#39;: at the store &#39;HOTLINE&#39;: via hot line number &#39;WEBSITE&#39;: via website &#39;FORM&#39;: via order form &#39;BUY_IN_WEBVIEW&#39;: via web &#39;BUY_IN_APP&#39;: via App | [optional] 
**title** | **str** | Method title | [optional] 
**description** | **str** | Description of the method | [optional] 
**order** | **int** | Number | [optional] 
**link** | **str** | Link to the usage method | [optional] 
**phone_1** | **str** | Phone number 1 | [optional] 
**phone_2** | **str** | Phone number 2 | [optional] 

## Example

```python
from gotit_api_python_sdk.models.usagemethodschema import USAGEMETHODSCHEMA

# TODO update the JSON string below
json = "{}"
# create an instance of USAGEMETHODSCHEMA from a JSON string
usagemethodschema_instance = USAGEMETHODSCHEMA.from_json(json)
# print the JSON string representation of the object
print(USAGEMETHODSCHEMA.to_json())

# convert the object into a dict
usagemethodschema_dict = usagemethodschema_instance.to_dict()
# create an instance of USAGEMETHODSCHEMA from a dict
usagemethodschema_from_dict = USAGEMETHODSCHEMA.from_dict(usagemethodschema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


