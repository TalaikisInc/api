# PostgRestApi.ContractsApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contractsDelete**](ContractsApi.md#contractsDelete) | **DELETE** /contracts | 
[**contractsGet**](ContractsApi.md#contractsGet) | **GET** /contracts | 
[**contractsPatch**](ContractsApi.md#contractsPatch) | **PATCH** /contracts | 
[**contractsPost**](ContractsApi.md#contractsPost) | **POST** /contracts | 


<a name="contractsDelete"></a>
# **contractsDelete**
> contractsDelete(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.ContractsApi();

var opts = { 
  'addr': "addr_example", // String | 
  'bytecode': "bytecode_example", // String | 
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
apiInstance.contractsDelete(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **String**|  | [optional] 
 **bytecode** | **String**|  | [optional] 
 **balance** | **String**|  | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

<a name="contractsGet"></a>
# **contractsGet**
> Contracts contractsGet(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.ContractsApi();

var opts = { 
  'addr': "addr_example", // String | 
  'bytecode': "bytecode_example", // String | 
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
apiInstance.contractsGet(opts, callback);
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
 **rangeUnit** | **String**| Limiting and Pagination | [optional] [default to items]
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

<a name="contractsPatch"></a>
# **contractsPatch**
> contractsPatch(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.ContractsApi();

var opts = { 
  'addr': "addr_example", // String | 
  'bytecode': "bytecode_example", // String | 
  'balance': "balance_example", // String | 
  'contracts': new PostgRestApi.Contracts(), // Contracts | contracts
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.contractsPatch(opts, callback);
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

<a name="contractsPost"></a>
# **contractsPost**
> contractsPost(opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.ContractsApi();

var opts = { 
  'contracts': new PostgRestApi.Contracts(), // Contracts | contracts
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.contractsPost(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contracts** | [**Contracts**](Contracts.md)| contracts | [optional] 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json, text/csv

