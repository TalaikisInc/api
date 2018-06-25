# PostgRestApi.RpcPgpPubDecryptByteaApi

All URIs are relative to *http://0.0.0.0:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpcPgpPubDecryptByteaPost**](RpcPgpPubDecryptByteaApi.md#rpcPgpPubDecryptByteaPost) | **POST** /rpc/pgp_pub_decrypt_bytea | 


<a name="rpcPgpPubDecryptByteaPost"></a>
# **rpcPgpPubDecryptByteaPost**
> rpcPgpPubDecryptByteaPost(args, opts)



### Example
```javascript
var PostgRestApi = require('postg_rest_api');

var apiInstance = new PostgRestApi.RpcPgpPubDecryptByteaApi();

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
apiInstance.rpcPgpPubDecryptByteaPost(args, opts, callback);
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

