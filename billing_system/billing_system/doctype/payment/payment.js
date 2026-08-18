// Copyright (c) 2026, kishore and contributors
// For license information, please see license.txt



frappe.ui.form.on("Payment", {
	refresh(frm) {
        frm.set_value("outstanding_amount", frm.doc.yet_to_pay - frm.doc.amount);
	},
});