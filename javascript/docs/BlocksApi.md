# PostgRestApi.BlocksApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blocksDelete**](BlocksApi.md#blocksDelete) | **DELETE** /blocks | 
[**blocksGet**](BlocksApi.md#blocksGet) | **GET** /blocks | 
[**blocksPatch**](BlocksApi.md#blocksPatch) | **PATCH** /blocks | 
[**blocksPost**](BlocksApi.md#blocksPost) | **POST** /blocks | 


<a name="blocksDelete"></a>
# **blocksDelete**
> blocksDelete(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.BlocksApi();

var opts = { 
  'block': "block_example", // String | 
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.blocksDelete(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block** | **String**|  | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

<a name="blocksGet"></a>
# **blocksGet**
> Blocks blocksGet(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.BlocksApi();

var opts = { 
  'block': "block_example", // String | 
  'select': "select_example", // String | Filtering Columns
  'order': "order_example", // String | Ordering
  'range': "range_example", // String | Limiting and Pagination
  'rangeUnit': "items", // String | Limiting and Pagination
  'offset': "offset_example", // String | Limiting and Pagination
  'limit': "limit_example", // String | Limiting and Pagination
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.blocksGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block** | **String**|  | [optional] 
 **select** | **String**| Filtering Columns | [optional] 
 **order** | **String**| Ordering | [optional] 
 **range** | **String**| Limiting and Pagination | [optional] 
 **rangeUnit** | **String**| Limiting and Pagination | [optional] [default to items]
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

<a name="blocksPatch"></a>
# **blocksPatch**
> blocksPatch(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.BlocksApi();

var opts = { 
  'block': "block_example", // String | 
  'blocks': new PostgRestApi.Blocks(), // Blocks | blocks
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.blocksPatch(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block** | **String**|  | [optional] 
 **blocks** | [**Blocks**](Blocks.md)| blocks | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

<a name="blocksPost"></a>
# **blocksPost**
> blocksPost(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.BlocksApi();

var opts = { 
  'blocks': new PostgRestApi.Blocks(), // Blocks | blocks
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.blocksPost(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocks** | [**Blocks**](Blocks.md)| blocks | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

