# swagger_client.ContractsApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_delete**](ContractsApi.md#contracts_delete) | **DELETE** /contracts | 
[**contracts_get**](ContractsApi.md#contracts_get) | **GET** /contracts | 
[**contracts_patch**](ContractsApi.md#contracts_patch) | **PATCH** /contracts | 
[**contracts_post**](ContractsApi.md#contracts_post) | **POST** /contracts | 


# **contracts_delete**
> contracts_delete(addr=addr, bytecode=bytecode, balance=balance, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
addr = 'addr_example' # str |  (optional)
bytecode = 'bytecode_example' # str |  (optional)
balance = 'balance_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.contracts_delete(addr=addr, bytecode=bytecode, balance=balance, prefer=prefer)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**|  | [optional] 
 **bytecode** | **str**|  | [optional] 
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

# **contracts_get**
> Contracts contracts_get(addr=addr, bytecode=bytecode, balance=balance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
addr = 'addr_example' # str |  (optional)
bytecode = 'bytecode_example' # str |  (optional)
balance = 'balance_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.contracts_get(addr=addr, bytecode=bytecode, balance=balance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**|  | [optional] 
 **bytecode** | **str**|  | [optional] 
 **balance** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**Contracts**](Contracts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_patch**
> contracts_patch(addr=addr, bytecode=bytecode, balance=balance, contracts=contracts, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
addr = 'addr_example' # str |  (optional)
bytecode = 'bytecode_example' # str |  (optional)
balance = 'balance_example' # str |  (optional)
contracts = swagger_client.Contracts() # Contracts | contracts (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.contracts_patch(addr=addr, bytecode=bytecode, balance=balance, contracts=contracts, prefer=prefer)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**|  | [optional] 
 **bytecode** | **str**|  | [optional] 
 **balance** | **str**|  | [optional] 
 **contracts** | [**Contracts**](Contracts.md)| contracts | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts_post**
> contracts_post(contracts=contracts, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractsApi()
contracts = swagger_client.Contracts() # Contracts | contracts (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.contracts_post(contracts=contracts, prefer=prefer)
except ApiException as e:
    print("Exception when calling ContractsApi->contracts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contracts** | [**Contracts**](Contracts.md)| contracts | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

