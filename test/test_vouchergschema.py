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

from gotit_api_python_sdk.models.vouchergschema import VOUCHERGSCHEMA

class TestVOUCHERGSCHEMA(unittest.TestCase):
    """VOUCHERGSCHEMA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VOUCHERGSCHEMA:
        """Test VOUCHERGSCHEMA
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VOUCHERGSCHEMA`
        """
        model = VOUCHERGSCHEMA()
        if include_optional:
            return VOUCHERGSCHEMA(
                order_id = 274694,
                order_name = '20230615001-mWG2',
                group_vouchers = gotit_api_python_sdk.models.group_voucher_schema.GROUP_VOUCHER_SCHEMA(
                    voucher_link = 'https://g-stg.gotit.vn/63jCvmpE', 
                    voucher_link_code = '63jCvmpE', 
                    voucher_serial = 'G4LAMN9BS64', ),
                vouchers = [
                    gotit_api_python_sdk.models.product_g.PRODUCT_G(
                        product_image = 'https://img-stg.gotit.vn/compress/580x580/2023/10/1697689521_VQLZQ.png', 
                        link = 'https://v-stg.gotit.vn/CavXeYy4', 
                        code = '2630bec5', 
                        serial = 'V92Z57VNFGH', 
                        product_id = 2478, 
                        price_id = 10260, 
                        value = 100000, 
                        expired_date = '2023-12-30', 
                        partner = gotit_api_python_sdk.models.vendor_schema.VENDOR_SCHEMA(
                            expiry = '2024-01-08', 
                            vendor = 'SPE', ), )
                    ]
            )
        else:
            return VOUCHERGSCHEMA(
        )
        """

    def testVOUCHERGSCHEMA(self):
        """Test VOUCHERGSCHEMA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
