import frappe

@frappe.whitelist()
def fullname(docname:str)->str:
	doc = frappe.get_doc("Customer", docname)
	doc.full_name = doc.first_name + " " + doc.last_name
	doc.save()
	return "success"

@frappe.whitelist()
def product_availability(name:str, quantity:int)->str:
	doc = frappe.get_doc("Product", name)
	pro_quantity = doc.stock_quantity

	if pro_quantity < quantity:
		frappe.throw("Insufficient Quantity of this product")

def invoice_list(user):
	print(user)
	cus_id=frappe.get_value("Customer",{"email":frappe.session.user},"name")
	print(cus_id)
	return f"tabInvoice.customer={frappe.db.escape(cus_id)}"
	