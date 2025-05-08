# CATEGORIESRESPONSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | HTTP response status | [optional] 
**status_code** | **int** | HTTP response status codes | [optional] 
**error** | **str** | Error code | [optional] 
**message** | **str** | Message Error | [optional] 
**data** | [**List[CATEGORIESDETAIL]**](CATEGORIESDETAIL.md) |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.categoriesresponse import CATEGORIESRESPONSE

# TODO update the JSON string below
json = "{}"
# create an instance of CATEGORIESRESPONSE from a JSON string
categoriesresponse_instance = CATEGORIESRESPONSE.from_json(json)
# print the JSON string representation of the object
print(CATEGORIESRESPONSE.to_json())

# convert the object into a dict
categoriesresponse_dict = categoriesresponse_instance.to_dict()
# create an instance of CATEGORIESRESPONSE from a dict
categoriesresponse_from_dict = CATEGORIESRESPONSE.from_dict(categoriesresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


