# SwaggerClient::IntrospectionApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](IntrospectionApi.md#root_get) | **GET** / | OpenAPI description (this document)


# **root_get**
> root_get

OpenAPI description (this document)

### Example
```ruby
# load the gem
require 'swagger_client'

api_instance = SwaggerClient::IntrospectionApi.new

begin
  #OpenAPI description (this document)
  api_instance.root_get
rescue SwaggerClient::ApiError => e
  puts "Exception when calling IntrospectionApi->root_get: #{e}"
end
```

### Parameters
This endpoint does not need any parameter.

### Return type

nil (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/openapi+json, application/json



