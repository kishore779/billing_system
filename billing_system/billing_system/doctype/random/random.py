# Copyright (c) 2026, kishore and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document


class Random(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		city: DF.Data | None
		humidity: DF.Percent
		temperature: DF.Float
		weather: DF.Data | None
	# end: auto-generated types

	
	def db_insert(self, *args, **kwargs):
		raise NotImplementedError

	def load_from_db(self, *args, **kwargs):
		raise NotImplementedError

	def db_update(self, *args, **kwargs):
		raise NotImplementedError

	def delete(self, *args, **kwargs):
		raise NotImplementedError

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
		url = "https://api.open-meteo.com/v1/forecast"

		params = {
			"latitude": 13.0827,
			"longitude": 80.2707,
			"current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
		}

		response = requests.get(url, params=params)
		data = response.json()

		print(data["current"]["temperature_2m"])

	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass

