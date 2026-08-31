# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class Item(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Literal["Cotton", "Polister", "Fancy"]
		item_name: DF.Data | None
		price: DF.Currency
		route: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Item"

	website = frappe._dict(template = "billing_system/doctype/item/item.html")

	def get_context(self, context):
		context.title = "ITEMSSS"
		context.item = self.item_name
		


