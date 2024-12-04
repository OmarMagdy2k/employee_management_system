// Copyright (c) 2024, omarmagdy2@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Projectt', {
	company: function(frm) {
		frm.set_value('department', null);
		frm.set_query('department', function() {
            return {
                filters: {
                    'company': frm.doc.company
                }
            };
        });
	},
	department: function(frm){
		frm.set_value('assigned_employees', null);
		frm.set_query('assigned_employees', function() {
            return {
                filters: {
                    'department': frm.doc.department
                }
            };
        });
	}
});
