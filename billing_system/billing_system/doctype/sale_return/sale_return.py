# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SaleReturn(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from billing_system.billing_system.doctype.return_item.return_item import ReturnItem
		from frappe.types import DF

		amended_from: DF.Link | None
		customer: DF.Link | None
		items: DF.Table[ReturnItem]
		original_invoice: DF.Link | None
		payable_amount: DF.Currency
		return_amount: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Sale Return"

	# def validate(self):
	# 	for item in self.items:
	# 		inv = frappe.get_doc("Invoice", )
	# 		if item.quantity > :
	# 			frappe.throw()
	def before_save(self):
		invoice = frappe.get_doc("Invoice", self.original_invoice)
		self.payable_amount = invoice.balance_amount - self.return_amount


	def on_submit(self):
		for row in self.items:
			pro = frappe.get_doc("Product", row.product)
			pro.stock_quantity += row.quantity
			pro.save()
		frappe.db.commit()

	