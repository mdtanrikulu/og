# coding: utf-8

"""
    Yagna Payment API

     Invoicing and Payments is a fundamental area of Yagna Ecosystem functionality. It includes aspects of communication between Requestor, Provider and a selected Payment Platform, which becomes crucial when Activities are executed in the context of negotiated Agreements. Yagna applications must be able to exercise various payment models, and the Invoicing/Payment-related communication is happening in parallel to Activity control communication. To define functional patterns of Requestor/Provider interaction in this area, Payment API is specified.  An important principle of the Yagna Payment API is that the actual payment transactions are hidden behind the Invoice flow. In other words, a Yagna Application on Requestor side isn’t expected to trigger actual payment transactions. Instead it is expected to receive and accept Invoices raised by the Provider - based on Application’s Invoice Accept notifications, the Payment API implementation orchestrates the payment via a configured Payment platform.  **NOTE: This specification is work-in-progress.**   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import payment
from payment.api.provider_api import ProviderApi  # noqa: E501
from src.rest import ApiException


class TestProviderApi(unittest.TestCase):
    """ProviderApi unit test stubs"""

    def setUp(self):
        self.api = payment.api.provider_api.ProviderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_debit_note(self):
        """Test case for cancel_debit_note

        Cancel Debit Note.  # noqa: E501
        """
        pass

    def test_cancel_invoice(self):
        """Test case for cancel_invoice

        Cancel Invoice.  # noqa: E501
        """
        pass

    def test_collect_activity_events(self):
        """Test case for collect_activity_events

        Fetch Requestor command events.  # noqa: E501
        """
        pass

    def test_get_activity_state(self):
        """Test case for get_activity_state

        Get state of specified Activity.  # noqa: E501
        """
        pass

    def test_get_activity_usage(self):
        """Test case for get_activity_usage

        Get usage of specified Activity.  # noqa: E501
        """
        pass

    def test_get_incoming_payment(self):
        """Test case for get_incoming_payment

        Get incoming Payment.  # noqa: E501
        """
        pass

    def test_get_incoming_payments(self):
        """Test case for get_incoming_payments

        Get incoming Payments.  # noqa: E501
        """
        pass

    def test_get_issued_debit_note(self):
        """Test case for get_issued_debit_note

        Get Debit Note.  # noqa: E501
        """
        pass

    def test_get_issued_debit_notes(self):
        """Test case for get_issued_debit_notes

        Get Debit Notes issued by this Provider.  # noqa: E501
        """
        pass

    def test_get_issued_invoice(self):
        """Test case for get_issued_invoice

        Get Invoice.  # noqa: E501
        """
        pass

    def test_get_issued_invoices(self):
        """Test case for get_issued_invoices

        Get Invoices issued by this Provider.  # noqa: E501
        """
        pass

    def test_get_payments_for_issued_debit_note(self):
        """Test case for get_payments_for_issued_debit_note

        Get Payments for Debit Note.  # noqa: E501
        """
        pass

    def test_get_payments_for_issued_invoice(self):
        """Test case for get_payments_for_issued_invoice

        Get Payments for issued Invoice.  # noqa: E501
        """
        pass

    def test_get_provider_debit_note_events(self):
        """Test case for get_provider_debit_note_events

        Get Debit Note events.  # noqa: E501
        """
        pass

    def test_get_provider_invoice_events(self):
        """Test case for get_provider_invoice_events

        Get Invoice events.  # noqa: E501
        """
        pass

    def test_issue_debit_note(self):
        """Test case for issue_debit_note

        Issue a Debit Note.  # noqa: E501
        """
        pass

    def test_issue_invoice(self):
        """Test case for issue_invoice

        Issue an Invoice.  # noqa: E501
        """
        pass

    def test_send_debit_note(self):
        """Test case for send_debit_note

        Send Debit Note to Requestor.  # noqa: E501
        """
        pass

    def test_send_invoice(self):
        """Test case for send_invoice

        Send Invoice to Requestor.  # noqa: E501
        """
        pass

    def test_set_activity_state(self):
        """Test case for set_activity_state

        Set state of specified Activity.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
