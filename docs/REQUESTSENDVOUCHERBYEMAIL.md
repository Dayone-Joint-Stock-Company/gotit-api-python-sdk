# REQUESTSENDVOUCHERBYEMAIL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher_link_code** | **str** |  | 
**email** | **str** |  | 
**receiver_nm** | **str** |  | [optional] 
**sender_nm** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from gotit_api_python_sdk.models.requestsendvoucherbyemail import REQUESTSENDVOUCHERBYEMAIL

# TODO update the JSON string below
json = "{}"
# create an instance of REQUESTSENDVOUCHERBYEMAIL from a JSON string
requestsendvoucherbyemail_instance = REQUESTSENDVOUCHERBYEMAIL.from_json(json)
# print the JSON string representation of the object
print(REQUESTSENDVOUCHERBYEMAIL.to_json())

# convert the object into a dict
requestsendvoucherbyemail_dict = requestsendvoucherbyemail_instance.to_dict()
# create an instance of REQUESTSENDVOUCHERBYEMAIL from a dict
requestsendvoucherbyemail_from_dict = REQUESTSENDVOUCHERBYEMAIL.from_dict(requestsendvoucherbyemail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


