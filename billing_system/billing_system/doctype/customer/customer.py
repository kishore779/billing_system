# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Customer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.SmallText | None
		email: DF.Data
		first_name: DF.Data
		last_name: DF.Data | None
		phone_number: DF.Phone | None
		user: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Customer"

	@property
	def full_name(self):
		return f"{self.first_name} {self.last_name}"

	def after_insert(self):
		frappe.publish_realtime("creation", {"customer" : self.name})	
		print("published")
