import frappe

def get_context(context):
    
    if not frappe.session.user == "Administrator":
        frappe.throw("Login to Access this Page")
    
    context.customers = frappe.get_all("Customer",
                             fields = ["first_name", "email"])
    return context