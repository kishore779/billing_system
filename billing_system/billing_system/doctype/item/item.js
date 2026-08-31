// Copyright (c) 2026, kishore and contributors
// For license information, please see license.txt

frappe.ui.form.on("Item", {
	item_name(frm) {
        frm.set_value("route",frm.doc.item_name);
	},
});
