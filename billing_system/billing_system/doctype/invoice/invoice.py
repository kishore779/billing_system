# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt
from functools import cached_property
import frappe
from frappe.model.document import Document
from frappe.utils import add_days, getdate, today


class Invoice(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from billing_system.billing_system.doctype.invoice_item.invoice_item import InvoiceItem
		from frappe.types import DF

		amended_from: DF.Link | None
		amount_paid: DF.Currency
		balance_amount: DF.Currency
		customer: DF.Link
		discount_amount: DF.Currency
		due_date: DF.Date | None
		grand_total: DF.Currency
		invoice_date: DF.Date | None
		manager_status: DF.Literal["Approve", "Not Approved"]
		purchased_products: DF.Table[InvoiceItem]
		status: DF.Literal["Paid", "Partially Paid", "Not Paid"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Invoice"

	# def validate(self):
	# 	if self.invoice_date > getdate(today):
	# 		frappe.throw("Invoice date must be entered today")

	def before_save(self):
		total = 0
		for row in self.purchased_products:
			row.total_amount = row.quantity * row.rate
			total += row.total_amount

		self.grand_total = total

		if self.status == "Partially Paid":
			self.balance_amount = self.grand_total - self.amount_paid

		self.due_date = add_days(self.invoice_date, 30)

	def validate(self):
		if not self.amount_paid:
			frappe.throw("Must settle the initial amount")

		for item in self.purchased_products:
			product = frappe.get_doc("Product", item.item_name)

			if(product.stock_quantity >= item.quantity):
				product.stock_quantity -= item.quantity
				product.save()
			else:
				frappe.throw("Required quantity not available")

	def has_permission(self, permission):
		return True
		roles = frappe.get_roles()
		if "Administrator" in roles:
			return True
		if "Sales User" in roles:
			return True
		if "Customer" in roles:
			return self.customer == frappe.get_value("Customer",{"email":frappe.session.user},"name")
		return False
	