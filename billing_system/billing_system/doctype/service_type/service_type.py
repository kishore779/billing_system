# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ServiceType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category: DF.Data | None
		default_rate: DF.Currency
		description: DF.SmallText | None
		is_active: DF.Check
		service_name: DF.Data
		tax: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Service Type"
