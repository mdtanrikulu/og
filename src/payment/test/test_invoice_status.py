# coding: utf-8

"""
    Yagna Payment API

     Invoicing and Payments is a fundamental area of Yagna Ecosystem functionality. It includes aspects of communication between Requestor, Provider and a selected Payment Platform, which becomes crucial when Activities are executed in the context of negotiated Agreements. Yagna applications must be able to exercise various payment models, and the Invoicing/Payment-related communication is happening in parallel to Activity control communication. To define functional patterns of Requestor/Provider interaction in this area, Payment API is specified.  An important principle of the Yagna Payment API is that the actual payment transactions are hidden behind the Invoice flow. In other words, a Yagna Application on Requestor side isn’t expected to trigger actual payment transactions. Instead it is expected to receive and accept Invoices raised by the Provider - based on Application’s Invoice Accept notifications, the Payment API implementation orchestrates the payment via a configured Payment platform.  **NOTE: This specification is work-in-progress.**   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import payment
from payment.models.invoice_status import InvoiceStatus  # noqa: E501
from src.rest import ApiException

class TestInvoiceStatus(unittest.TestCase):
    """InvoiceStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InvoiceStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = payment.models.invoice_status.InvoiceStatus()  # noqa: E501
        if include_optional :
            return InvoiceStatus(
            )
        else :
            return InvoiceStatus(
        )

    def testInvoiceStatus(self):
        """Test InvoiceStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
