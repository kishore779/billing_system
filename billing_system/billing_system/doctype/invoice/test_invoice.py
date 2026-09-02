# Copyright (c) 2026, kishore and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestInvoice(IntegrationTestCase):
	"""
	Integration tests for Invoice.
	Use this class for testing interactions between multiple components.
	"""

	def test_total_amount(self):
		customer = frappe.get_doc({
			"doctype" :"Customer",
			"first_name" : "Test Customer",
			"email" : "test@gmail.com"
			}).insert(ignore_permissions=True)
		ex_invoice = frappe.get_doc({
			"doctype" :"Invoice",
			"customer" : customer.name,
			"purchased_products" : [
				{"item_name" : "PRO-0002", "quantity" : 1},
				{"item_name" : "PRO-0004", "quantity" : 1}
			],
			"amount_paid" : 10000
		})
		ex_invoice.insert(ignore_permissions=True)


		self.assertEqual(ex_invoice.grand_total, 126000)
