// Copyright (c) 2026, kishore and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product", {
	stock_quantity(frm) {
        if(frm.doc.stock_quantity >= 1){
            frm.set_value("is_available",1);
        }
	},
    rate(frm){
        calculate_selling_amount(frm);
    },
    tax(frm){
        calculate_selling_amount(frm);
    }
});
function calculate_selling_amount(frm){
    rate = frm.doc.rate || 1;
    tax = frm.doc.tax || 1;

    total_amount = (rate * (tax/ 100)) + rate;
    frm.set_value("selling_amount", total_amount)
}
