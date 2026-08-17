# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tax(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		product: DF.Link | None
		product_tax: DF.Percent
	# end: auto-generated types

	_DOCTYPE_NAME = "Tax"
