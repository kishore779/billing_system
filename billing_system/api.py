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
	if user == "Administrator":
		return ""
	if "Sale User" in frappe.get_roles(user) :
		return ""
	cus_id=frappe.get_value("Customer",{"email":user},"name")
	return f"tabInvoice.customer={frappe.db.escape(cus_id)}"

@frappe.whitelist()
def get_customer_invoice_details():
	Invoice = frappe.qb.DocType("Invoice")
	SaleReturn = frappe.qb.DocType("Sale Return")

	data = frappe.qb.from_(Invoice).join(SaleReturn).on(Invoice.customer == SaleReturn.customer).where(Invoice.grand_total > 50000).select(Invoice.name,SaleReturn.return_amount, Invoice.grand_total).run(as_dict=True)
	return data

def payment_list(user):
	if user == "Administrator":
		return ""
	if "Sale User" in frappe.get_roles(user) :
		return ""
	cus_id=frappe.get_value("Customer",{"email":user},"name")
	return f"tabPayment.customer={frappe.db.escape(cus_id)}"
	