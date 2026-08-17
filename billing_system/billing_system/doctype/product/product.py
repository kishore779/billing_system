# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Product(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Literal["Laptop", "Mobile", "Earphones"]
		description: DF.SmallText | None
		is_available: DF.Check
		pro_name: DF.Data
		rate: DF.Currency
		selling_amount: DF.Currency
		stock_quantity: DF.Int
		tax: DF.Percent
	# end: auto-generated types

	_DOCTYPE_NAME = "Product"

	def validate(self):
		if not self.pro_name.strip():
			frappe.throw("Name must needed")
