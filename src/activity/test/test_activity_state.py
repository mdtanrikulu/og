# coding: utf-8

"""
    Yagna Activity API

    It conforms with capability level 1 of the [Activity API specification](https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import activity
from activity.models.activity_state import ActivityState  # noqa: E501
from src.rest import ApiException

class TestActivityState(unittest.TestCase):
    """ActivityState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActivityState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = activity.models.activity_state.ActivityState()  # noqa: E501
        if include_optional :
            return ActivityState(
                state = [
                    'New'
                    ], 
                reason = '0', 
                error_message = '0'
            )
        else :
            return ActivityState(
                state = [
                    'New'
                    ],
        )

    def testActivityState(self):
        """Test ActivityState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
