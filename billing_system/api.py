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
	if not user == "Administrator":
		cus_id=frappe.get_value("Customer",{"email":frappe.session.user},"name")
		print(cus_id)
		return f"tabInvoice.customer={frappe.db.escape(cus_id)}"
	print(user)

@frappe.whitelist()
def get_customer_invoice_details():
	Invoice = frappe.qb.DocType("Invoice")
	SaleReturn = frappe.qb.DocType("Sale Return")

	query = (
		frappe.qb.from_(Invoice)
		.outer_join(SaleReturn)
		.on(Invoice.customer == SaleReturn.customer)
		.select(
			Invoice.name,
			Invoice.customer,
			Invoice.balance_amount,
			SaleReturn.return_amount,
			SaleReturn.payable_amount
		)
	).run(as_dict = True)
	return{
		"success" : True,
		"count" : len(query),
		"data" : query
	}	

def payment_list(user):
	if not user == "Administrator" or not user == "Sale User":
		customer_id = frappe.db.get_value("Customer", {"email" : frappe.session.user}, "name")
		return f"tabPayment.customer = {frappe.db.escape(customer_id)}"