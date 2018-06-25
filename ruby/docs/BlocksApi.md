# SwaggerClient::BlocksApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blocks_delete**](BlocksApi.md#blocks_delete) | **DELETE** /blocks | 
[**blocks_get**](BlocksApi.md#blocks_get) | **GET** /blocks | 
[**blocks_patch**](BlocksApi.md#blocks_patch) | **PATCH** /blocks | 
[**blocks_post**](BlocksApi.md#blocks_post) | **POST** /blocks | 


# **blocks_delete**
> blocks_delete(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::BlocksApi.new

opts = { 
  block: "block_example", # String | 
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.blocks_delete(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling BlocksApi->blocks_delete: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block** | **String**|  | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **blocks_get**
> Blocks blocks_get(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::BlocksApi.new

opts = { 
  block: "block_example", # String | 
  select: "select_example", # String | Filtering Columns
  order: "order_example", # String | Ordering
  range: "range_example", # String | Limiting and Pagination
  range_unit: "items", # String | Limiting and Pagination
  offset: "offset_example", # String | Limiting and Pagination
  limit: "limit_example", # String | Limiting and Pagination
  prefer: "prefer_example" # String | Preference
}

begin
  result = api_instance.blocks_get(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling BlocksApi->blocks_get: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block** | **String**|  | [optional] 
 **select** | **String**| Filtering Columns | [optional] 
 **order** | **String**| Ordering | [optional] 
 **range** | **String**| Limiting and Pagination | [optional] 
 **range_unit** | **String**| Limiting and Pagination | [optional] [default to items]
 **offset** | **String**| Limiting and Pagination | [optional] 
 **limit** | **String**| Limiting and Pagination | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

[**Blocks**](Blocks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **blocks_patch**
> blocks_patch(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::BlocksApi.new

opts = { 
  block: "block_example", # String | 
  blocks: SwaggerClient::Blocks.new, # Blocks | blocks
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.blocks_patch(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling BlocksApi->blocks_patch: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block** | **String**|  | [optional] 
 **blocks** | [**Blocks**](Blocks.md)| blocks | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



# **blocks_post**
> blocks_post(opts)



### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::BlocksApi.new

opts = { 
  blocks: SwaggerClient::Blocks.new, # Blocks | blocks
  prefer: "prefer_example" # String | Preference
}

begin
  api_instance.blocks_post(opts)
rescue SwaggerClient::ApiError => e
  puts "Exception when calling BlocksApi->blocks_post: #{e}"
end
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocks** | [**Blocks**](Blocks.md)| blocks | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv



