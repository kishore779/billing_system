// Copyright (c) 2026, kishore and contributors
// For license information, please see license.txt

//
frappe.ui.form.on("Invoice Item", {
    quantity : function(frm, cdt, cdn){
        //
        // to Calculate the item price with required quantity
        //
        let row = locals[cdt][cdn];

        total = row.rate * row.quantity;

        frappe.model.set_value(
            cdt,
            cdn,
            "total_amount",
            total
        );
        //
        //To sum the total item selected
        //
        let sum = 0;
        
        for(item of frm.doc.purchased_products){
            sum += item.total_amount;
        }
        frm.set_value("grand_total", sum);

        frappe.call({
            method : "billing_system.api.product_availability",
            args: {
                name : row.item_name,
                quantity : row.quantity,
            },
            callback : function(res){
                if(!res.exe){
                    console.log("success")
                }
            }
        });
    }
});

frappe.ui.form.on("Invoice", {
        amount_paid(frm){

            if(!frm.doc.dis_amount){
                
                if (frm.doc.amount_paid == 0){
                    frm.set_value("status", "Not Paid");
                }
                else if (frm.doc.amount_paid < frm.doc.grand_total){
                    frm.set_value("status", "Partially Paid");
                    frm.set_value("balance_amount", frm.doc.grand_total - frm.doc.amount_paid)
                }
                else if (frm.doc.amount_paid == frm.doc.grand_total){
                    frm.set_value("status", "Paid");
                }
            }
            if(frm.doc.dis_amount){
                if (frm.doc.amount_paid == 0){
                    frm.set_value("status", "Not Paid");
                }
                else if (frm.doc.amount_paid < frm.doc.dis_amount){
                    frm.set_value("status", "Partially Paid");
                    frm.set_value("balance_amount", frm.doc.dis_amount - frm.doc.amount_paid)
                }
                else if (frm.doc.amount_paid == frm.dis_amount){
                    frm.set_value("status", "Paid");
                }
            }
        },
        invoice_date(frm){
            frm.set_value("due_date", frappe.datetime.add_days(frm.doc.invoice_date,30));
        }
});

frappe.ui.form.on("Invoice", {
    refresh(frm){
        frm.add_custom_button("Discount",function(){
            frappe.prompt(
                {
                    label : "Discount Percentage",
                    fieldname : "discount",
                    fieldtype : "Percent"
                },
            function(values){
                frappe.confirm(
                    `Do You Confirm the Discount of ${values.discount}`,

                    () => {
                        dis_amount = frm.doc.grand_total - (frm.doc.grand_total * (values.discount/100));
                        frm.set_value("discount_amount", dis_amount);
                        frappe.msgprint({
                            title : __("Success"),
                            indicator : "green",
                            message : __("Discount Applied to the grand total") 
                        })
                    },
                    () => {
                        frappe.msgprint("Discount Cancelled")
                    }
                );
            });

        }, __("Details Group"));
        frm.add_custom_button("Details", function(){
            let d = new frappe.ui.Dialog({
                title : "Customer Details",
                fields : [
                    {
                        "label" : "Name",
                        "fieldname" : "name",
                        "fieldtype" : "Data"
                    },
                    {
                        "label" : "Date of Birth",
                        "fieldname" : "dob",
                        "fieldtype" : "Date"
                    }
                ],
                primary_action_label : "Confirm",
                primary_action(values){
                    console.log("Customer Entered");
                    d.hide();
                } ,
                secondary_action_label : "Exit",
                secondary_action(values){
                    console.log("Customer cancelled");
                    d.hide();
                },
            });
            d.show();
        }, __("Details Group"));
    },
    manager_status:function(frm){
        console.log("loaded")
        if(!frm.is_new()){
            frappe.call({
                method : "billing_system.api.approve_invoice",
                args : {
                    invoice_name : frm.doc.name
                },
                callback : function(res){
                    if(!res.exe){
                        console.log(res)
                    }
                }
            });
        }
    }
});


