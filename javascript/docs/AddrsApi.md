# PostgRestApi.AddrsApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addrsDelete**](AddrsApi.md#addrsDelete) | **DELETE** /addrs | 
[**addrsGet**](AddrsApi.md#addrsGet) | **GET** /addrs | 
[**addrsPatch**](AddrsApi.md#addrsPatch) | **PATCH** /addrs | 
[**addrsPost**](AddrsApi.md#addrsPost) | **POST** /addrs | 


<a name="addrsDelete"></a>
# **addrsDelete**
> addrsDelete(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.AddrsApi();

var opts = { 
  'addr': "addr_example", // String | 
  'balance': "balance_example", // String | 
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.addrsDelete(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

<a name="addrsGet"></a>
# **addrsGet**
> Addrs addrsGet(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.AddrsApi();

var opts = { 
  'addr': "addr_example", // String | 
  'balance': "balance_example", // String | 
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
apiInstance.addrsGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **select** | **String**| Filtering Columns | [optional] 
 **order** | **String**| Ordering | [optional] 
 **range** | **String**| Limiting and Pagination | [optional] 
 **rangeUnit** | **String**| Limiting and Pagination | [optional] [default to items]
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

<a name="addrsPatch"></a>
# **addrsPatch**
> addrsPatch(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.AddrsApi();

var opts = { 
  'addr': "addr_example", // String | 
  'balance': "balance_example", // String | 
  'addrs': new PostgRestApi.Addrs(), // Addrs | addrs
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.addrsPatch(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **addrs** | [**Addrs**](Addrs.md)| addrs | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

<a name="addrsPost"></a>
# **addrsPost**
> addrsPost(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.AddrsApi();

var opts = { 
  'addrs': new PostgRestApi.Addrs(), // Addrs | addrs
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.addrsPost(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | [**Addrs**](Addrs.md)| addrs | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

