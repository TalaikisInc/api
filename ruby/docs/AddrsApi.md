# SwaggerClient::AddrsApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addrs_delete**](AddrsApi.md#addrs_delete) | **DELETE** /addrs | 
[**addrs_get**](AddrsApi.md#addrs_get) | **GET** /addrs | 
[**addrs_patch**](AddrsApi.md#addrs_patch) | **PATCH** /addrs | 
[**addrs_post**](AddrsApi.md#addrs_post) | **POST** /addrs | 


# **addrs_delete**
> addrs_delete(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::AddrsApi.new

opts = { 
  addr: "addr_example", # String | 
  balance: "balance_example", # String | 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.addrs_delete(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling AddrsApi->addrs_delete: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **addrs_get**
> Addrs addrs_get(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::AddrsApi.new

opts = { 
  addr: "addr_example", # String | 
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
  result = api_instance.addrs_get(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling AddrsApi->addrs_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **select** | **String**| Filtering Columns | [optional] 
 **order** | **String**| Ordering | [optional] 
 **range** | **String**| Limiting and Pagination | [optional] 
 **range_unit** | **String**| Limiting and Pagination | [optional] [default to items]
 **offset** | **String**| Limiting and Pagination | [optional] 
 **limit** | **String**| Limiting and Pagination | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

[**Addrs**](Addrs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **addrs_patch**
> addrs_patch(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::AddrsApi.new

opts = { 
  addr: "addr_example", # String | 
  balance: "balance_example", # String | 
  addrs: SwaggerClient::Addrs.new, # Addrs | addrs
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.addrs_patch(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling AddrsApi->addrs_patch: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **addrs** | [**Addrs**](Addrs.md)| addrs | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **addrs_post**
> addrs_post(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::AddrsApi.new

opts = { 
  addrs: SwaggerClient::Addrs.new, # Addrs | addrs
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.addrs_post(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling AddrsApi->addrs_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | [**Addrs**](Addrs.md)| addrs | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



