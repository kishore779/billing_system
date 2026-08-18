# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ReturnItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		price: DF.Currency
		product: DF.Link | None
		quantity: DF.Int
		total: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Return Item"
