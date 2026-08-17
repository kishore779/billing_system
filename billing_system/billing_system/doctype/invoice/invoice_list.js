frappe.listview_settings["Invoice"] = {
    onload(listview){
        console.log("Invoice loaded");
    },

    add_fields : ["status","grand_total","balance_amount"],
    get_indicator : function(doc){
        if( doc.status == "Paid"){
            return [__("Paid"), "green", "status,=,Paid"];
        }
        else if (doc.status == "Partially Paid"){
            return [__("Partially Paid"), "yellow", "status,=,Partially Paid"];
        }
        else{
            return [__("Not Paid"), "red", "status,=,Not Paid"];
        }
    }
};