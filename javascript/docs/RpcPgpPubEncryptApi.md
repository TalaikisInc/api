# PostgRestApi.RpcPgpPubEncryptApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpcPgpPubEncryptPost**](RpcPgpPubEncryptApi.md#rpcPgpPubEncryptPost) | **POST** /rpc/pgp_pub_encrypt | 


<a name="rpcPgpPubEncryptPost"></a>
# **rpcPgpPubEncryptPost**
> rpcPgpPubEncryptPost(args, opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.RpcPgpPubEncryptApi();

var args = null; // Object | 

var opts = { 
  'prefer': "prefer_example" // String | Preference
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.rpcPgpPubEncryptPost(args, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **args** | **Object**|  | 
 **prefer** | **String**| Preference | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json, text/csv
 - **Accept**: application/json, application/vnd.pgrst.object+json

