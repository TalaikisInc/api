# coding: utf-8

"""
    PostgREST API

    standard public schema  # noqa: E501

    OpenAPI spec version: 0.5.0.0 (d8896be)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BlocksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def blocks_delete(self, **kwargs):  # noqa: E501
        """blocks_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :param str block:
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.blocks_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.blocks_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def blocks_delete_with_http_info(self, **kwargs):  # noqa: E501
        """blocks_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str block:
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block', 'prefer']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'block' in params:
            query_params.append(('block', params['block']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_get(self, **kwargs):  # noqa: E501
        """blocks_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str block:
        :param str select: Filtering Columns
        :param str order: Ordering
        :param str range: Limiting and Pagination
        :param str range_unit: Limiting and Pagination
        :param str offset: Limiting and Pagination
        :param str limit: Limiting and Pagination
        :param str prefer: Preference
        :return: Blocks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.blocks_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.blocks_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def blocks_get_with_http_info(self, **kwargs):  # noqa: E501
        """blocks_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str block:
        :param str select: Filtering Columns
        :param str order: Ordering
        :param str range: Limiting and Pagination
        :param str range_unit: Limiting and Pagination
        :param str offset: Limiting and Pagination
        :param str limit: Limiting and Pagination
        :param str prefer: Preference
        :return: Blocks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block', 'select', 'order', 'range', 'range_unit', 'offset', 'limit', 'prefer']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'block' in params:
            query_params.append(('block', params['block']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501
        if 'range_unit' in params:
            header_params['Range-Unit'] = params['range_unit']  # noqa: E501
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Blocks',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_patch(self, **kwargs):  # noqa: E501
        """blocks_patch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_patch(async=True)
        >>> result = thread.get()

        :param async bool
        :param str block:
        :param Blocks blocks: blocks
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.blocks_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.blocks_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def blocks_patch_with_http_info(self, **kwargs):  # noqa: E501
        """blocks_patch  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_patch_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str block:
        :param Blocks blocks: blocks
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block', 'blocks', 'prefer']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_patch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'block' in params:
            query_params.append(('block', params['block']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'blocks' in params:
            body_params = params['blocks']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def blocks_post(self, **kwargs):  # noqa: E501
        """blocks_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param Blocks blocks: blocks
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.blocks_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.blocks_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def blocks_post_with_http_info(self, **kwargs):  # noqa: E501
        """blocks_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.blocks_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param Blocks blocks: blocks
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['blocks', 'prefer']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method blocks_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'blocks' in params:
            body_params = params['blocks']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
