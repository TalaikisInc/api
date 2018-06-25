# SwaggerClient::ContractsApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_delete**](ContractsApi.md#contracts_delete) | **DELETE** /contracts | 
[**contracts_get**](ContractsApi.md#contracts_get) | **GET** /contracts | 
[**contracts_patch**](ContractsApi.md#contracts_patch) | **PATCH** /contracts | 
[**contracts_post**](ContractsApi.md#contracts_post) | **POST** /contracts | 


# **contracts_delete**
> contracts_delete(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::ContractsApi.new

opts = { 
  addr: "addr_example", # String | 
  bytecode: "bytecode_example", # String | 
  balance: "balance_example", # String | 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.contracts_delete(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling ContractsApi->contracts_delete: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **bytecode** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **contracts_get**
> Contracts contracts_get(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::ContractsApi.new

opts = { 
  addr: "addr_example", # String | 
  bytecode: "bytecode_example", # String | 
  balance: "balance_example", # String | 
  select: "select_example", # String | Filtering Columns
  order: "order_example", # String | Ordering
  range: "range_example", # String | Limiting and Pagination
  range_unit: "items", # String | Limiting and Pagination
  offset: "offset_example", # String | Limiting and Pagination
  limit: "limit_example", # String | Limiting and Pagination
  prefer: "prefer_example" # String | Preference
}

begin
  result = api_instance.contracts_get(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling ContractsApi->contracts_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **bytecode** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **select** | **String**| Filtering Columns | [optional] 
 **order** | **String**| Ordering | [optional] 
 **range** | **String**| Limiting and Pagination | [optional] 
 **range_unit** | **String**| Limiting and Pagination | [optional] [default to items]
 **offset** | **String**| Limiting and Pagination | [optional] 
 **limit** | **String**| Limiting and Pagination | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

[**Contracts**](Contracts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **contracts_patch**
> contracts_patch(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::ContractsApi.new

opts = { 
  addr: "addr_example", # String | 
  bytecode: "bytecode_example", # String | 
  balance: "balance_example", # String | 
  contracts: SwaggerClient::Contracts.new, # Contracts | contracts
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.contracts_patch(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling ContractsApi->contracts_patch: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **bytecode** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **contracts** | [**Contracts**](Contracts.md)| contracts | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **contracts_post**
> contracts_post(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::ContractsApi.new

opts = { 
  contracts: SwaggerClient::Contracts.new, # Contracts | contracts
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.contracts_post(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling ContractsApi->contracts_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contracts** | [**Contracts**](Contracts.md)| contracts | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



