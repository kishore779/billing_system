// Copyright (c) 2026, kishore and contributors
// For license information, please see license.txt

frappe.ui.form.on("Return Item", {
	quantity(frm, cdt, cdn){
        row = locals[cdt][cdn]

        total = row.quantity * row.price;

        frappe.model.set_value(
            cdt,
            cdn,
            "total",
            total
        );
        let sum = 0;
        for(item of frm.doc.items){
            sum += item.total;
        }
        frm.set_value("return_amount", sum);
	}
});
frappe.ui.form.on("Sale Return", {
    items(frm){

    }
})
