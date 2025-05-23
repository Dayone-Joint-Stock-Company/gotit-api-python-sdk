# coding: utf-8

"""
    Sample API

    Technical document APIs for API Version 4.

    The version of the OpenAPI document: 4.0.0
    Contact: quang.huynh@gotit.vn
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gotit_api_python_sdk.api.categories_api import CategoriesApi


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CategoriesApi()

    def tearDown(self) -> None:
        pass

    def test_get_category_by_product(self) -> None:
        """Test case for get_category_by_product

        Get category by product
        """
        pass

    def test_get_list_of_categories(self) -> None:
        """Test case for get_list_of_categories

        Get lists category
        """
        pass


if __name__ == '__main__':
    unittest.main()
