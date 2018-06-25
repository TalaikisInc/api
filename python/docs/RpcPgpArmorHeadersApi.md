# swagger_client.RpcPgpArmorHeadersApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_pgp_armor_headers_post**](RpcPgpArmorHeadersApi.md#rpc_pgp_armor_headers_post) | **POST** /rpc/pgp_armor_headers | 


# **rpc_pgp_armor_headers_post**
> rpc_pgp_armor_headers_post(args, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RpcPgpArmorHeadersApi()
args = NULL # object | 
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.rpc_pgp_armor_headers_post(args, prefer=prefer)
except ApiException as e:
    print("Exception when calling RpcPgpArmorHeadersApi->rpc_pgp_armor_headers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | **object**|  | 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

