
import frappe

def execute():
	"""Update all Invoice"""

	# Write your patch here.
	doc = frappe.get_doc("Invoice", "INV-0008")
	doc.submit()
	print("Submitted")
