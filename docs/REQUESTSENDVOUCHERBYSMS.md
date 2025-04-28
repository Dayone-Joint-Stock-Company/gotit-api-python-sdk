# REQUESTSENDVOUCHERBYSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_link_code** | **str** |  | 
**phone_no** | **str** |  | 
**receiver_nm** | **str** |  | [optional] 
**sender_nm** | **str** |  | [optional] 

## Example

```python
from gotit_api_sdk_python.models.requestsendvoucherbysms import REQUESTSENDVOUCHERBYSMS

# TODO update the JSON string below
json = "{}"
# create an instance of REQUESTSENDVOUCHERBYSMS from a JSON string
requestsendvoucherbysms_instance = REQUESTSENDVOUCHERBYSMS.from_json(json)
# print the JSON string representation of the object
print(REQUESTSENDVOUCHERBYSMS.to_json())

# convert the object into a dict
requestsendvoucherbysms_dict = requestsendvoucherbysms_instance.to_dict()
# create an instance of REQUESTSENDVOUCHERBYSMS from a dict
requestsendvoucherbysms_from_dict = REQUESTSENDVOUCHERBYSMS.from_dict(requestsendvoucherbysms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


