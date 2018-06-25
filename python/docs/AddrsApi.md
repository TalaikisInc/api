# swagger_client.AddrsApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addrs_delete**](AddrsApi.md#addrs_delete) | **DELETE** /addrs | 
[**addrs_get**](AddrsApi.md#addrs_get) | **GET** /addrs | 
[**addrs_patch**](AddrsApi.md#addrs_patch) | **PATCH** /addrs | 
[**addrs_post**](AddrsApi.md#addrs_post) | **POST** /addrs | 


# **addrs_delete**
> addrs_delete(addr=addr, balance=balance, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddrsApi()
addr = 'addr_example' # str |  (optional)
balance = 'balance_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.addrs_delete(addr=addr, balance=balance, prefer=prefer)
except ApiException as e:
    print("Exception when calling AddrsApi->addrs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**|  | [optional] 
 **balance** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addrs_get**
> Addrs addrs_get(addr=addr, balance=balance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddrsApi()
addr = 'addr_example' # str |  (optional)
balance = 'balance_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.addrs_get(addr=addr, balance=balance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddrsApi->addrs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**|  | [optional] 
 **balance** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**Addrs**](Addrs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addrs_patch**
> addrs_patch(addr=addr, balance=balance, addrs=addrs, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddrsApi()
addr = 'addr_example' # str |  (optional)
balance = 'balance_example' # str |  (optional)
addrs = swagger_client.Addrs() # Addrs | addrs (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.addrs_patch(addr=addr, balance=balance, addrs=addrs, prefer=prefer)
except ApiException as e:
    print("Exception when calling AddrsApi->addrs_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**|  | [optional] 
 **balance** | **str**|  | [optional] 
 **addrs** | [**Addrs**](Addrs.md)| addrs | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addrs_post**
> addrs_post(addrs=addrs, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddrsApi()
addrs = swagger_client.Addrs() # Addrs | addrs (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.addrs_post(addrs=addrs, prefer=prefer)
except ApiException as e:
    print("Exception when calling AddrsApi->addrs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | [**Addrs**](Addrs.md)| addrs | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

