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

from gotit_api_python_sdk.models.groupvoucherschema import GROUPVOUCHERSCHEMA

class TestGROUPVOUCHERSCHEMA(unittest.TestCase):
    """GROUPVOUCHERSCHEMA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GROUPVOUCHERSCHEMA:
        """Test GROUPVOUCHERSCHEMA
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GROUPVOUCHERSCHEMA`
        """
        model = GROUPVOUCHERSCHEMA()
        if include_optional:
            return GROUPVOUCHERSCHEMA(
                voucher_link = 'https://g-stg.gotit.vn/63jCvmpE',
                voucher_link_code = '63jCvmpE',
                voucher_serial = 'G4LAMN9BS64'
            )
        else:
            return GROUPVOUCHERSCHEMA(
        )
        """

    def testGROUPVOUCHERSCHEMA(self):
        """Test GROUPVOUCHERSCHEMA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
