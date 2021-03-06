# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.rbac_authorization_v1_api import RbacAuthorizationV1Api


class TestRbacAuthorizationV1Api(unittest.TestCase):
    """ RbacAuthorizationV1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.rbac_authorization_v1_api.RbacAuthorizationV1Api()

    def tearDown(self):
        pass

    def test_create_cluster_role(self):
        """
        Test case for create_cluster_role

        
        """
        pass

    def test_create_cluster_role_binding(self):
        """
        Test case for create_cluster_role_binding

        
        """
        pass

    def test_create_namespaced_role(self):
        """
        Test case for create_namespaced_role

        
        """
        pass

    def test_create_namespaced_role_binding(self):
        """
        Test case for create_namespaced_role_binding

        
        """
        pass

    def test_delete_cluster_role(self):
        """
        Test case for delete_cluster_role

        
        """
        pass

    def test_delete_cluster_role_binding(self):
        """
        Test case for delete_cluster_role_binding

        
        """
        pass

    def test_delete_collection_cluster_role(self):
        """
        Test case for delete_collection_cluster_role

        
        """
        pass

    def test_delete_collection_cluster_role_binding(self):
        """
        Test case for delete_collection_cluster_role_binding

        
        """
        pass

    def test_delete_collection_namespaced_role(self):
        """
        Test case for delete_collection_namespaced_role

        
        """
        pass

    def test_delete_collection_namespaced_role_binding(self):
        """
        Test case for delete_collection_namespaced_role_binding

        
        """
        pass

    def test_delete_namespaced_role(self):
        """
        Test case for delete_namespaced_role

        
        """
        pass

    def test_delete_namespaced_role_binding(self):
        """
        Test case for delete_namespaced_role_binding

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_cluster_role(self):
        """
        Test case for list_cluster_role

        
        """
        pass

    def test_list_cluster_role_binding(self):
        """
        Test case for list_cluster_role_binding

        
        """
        pass

    def test_list_namespaced_role(self):
        """
        Test case for list_namespaced_role

        
        """
        pass

    def test_list_namespaced_role_binding(self):
        """
        Test case for list_namespaced_role_binding

        
        """
        pass

    def test_list_role_binding_for_all_namespaces(self):
        """
        Test case for list_role_binding_for_all_namespaces

        
        """
        pass

    def test_list_role_for_all_namespaces(self):
        """
        Test case for list_role_for_all_namespaces

        
        """
        pass

    def test_patch_cluster_role(self):
        """
        Test case for patch_cluster_role

        
        """
        pass

    def test_patch_cluster_role_binding(self):
        """
        Test case for patch_cluster_role_binding

        
        """
        pass

    def test_patch_namespaced_role(self):
        """
        Test case for patch_namespaced_role

        
        """
        pass

    def test_patch_namespaced_role_binding(self):
        """
        Test case for patch_namespaced_role_binding

        
        """
        pass

    def test_read_cluster_role(self):
        """
        Test case for read_cluster_role

        
        """
        pass

    def test_read_cluster_role_binding(self):
        """
        Test case for read_cluster_role_binding

        
        """
        pass

    def test_read_namespaced_role(self):
        """
        Test case for read_namespaced_role

        
        """
        pass

    def test_read_namespaced_role_binding(self):
        """
        Test case for read_namespaced_role_binding

        
        """
        pass

    def test_replace_cluster_role(self):
        """
        Test case for replace_cluster_role

        
        """
        pass

    def test_replace_cluster_role_binding(self):
        """
        Test case for replace_cluster_role_binding

        
        """
        pass

    def test_replace_namespaced_role(self):
        """
        Test case for replace_namespaced_role

        
        """
        pass

    def test_replace_namespaced_role_binding(self):
        """
        Test case for replace_namespaced_role_binding

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
