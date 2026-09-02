# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Payment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		customer: DF.Data | None
		invoice: DF.Link | None
		outstanding_amount: DF.Currency
		payment_date: DF.Date | None
		payment_method: DF.Literal["UPI", "Cash", "Bank_transfer", "C"]
		reciept: DF.Attach | None
		yet_to_pay: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Payment"

	def has_permission(self, user=None):
		roles = frappe.get_roles()

		if not "Administrator" or "Sale User" or self.customer == frappe.get_value("Customer", {"email" : frappe.session.user}, "name"):
			frappe.throw("You are not allowed to access this page")

	