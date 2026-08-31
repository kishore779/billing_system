// Copyright (c) 2026, kishore and contributors
// For license information, please see license.txt

// to set a full name to the customer
frappe.ui.form.on('Customer', {
    refresh(frm){
        frappe.realtime.off("creation");
        frappe.realtime.on("creation", (data)=>{

            console.log( "Created Successfully");
        });
        
    }
    
});

