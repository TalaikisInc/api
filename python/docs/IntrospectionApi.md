# swagger_client.IntrospectionApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](IntrospectionApi.md#root_get) | **GET** / | OpenAPI description (this document)


# **root_get**
> root_get()

OpenAPI description (this document)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntrospectionApi()

try:
    # OpenAPI description (this document)
    api_instance.root_get()
except ApiException as e:
    print("Exception when calling IntrospectionApi->root_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/openapi+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

