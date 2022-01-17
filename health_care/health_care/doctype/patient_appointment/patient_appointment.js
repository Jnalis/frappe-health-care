// Copyright (c) 2022, Juve and contributors
// For license information, please see license.txt

frappe.ui.form.on("Patient Appointment", {
  refresh: function (frm) {
    frappe.ui.form.on(
      "Patient Appointment",
      "appointment_type",
      function (frm, cdt, cdn) {
        var appointment_type_field = cur_frm.doc.appointment_type;

        // alert(appointment_type_field);

        // console.log(appointment_type_field);

        frappe.call({
          method: "frappe.client.get",
          args: {
            doctype: "Item",
            name: self.name,
          },
          callback(r) {
            if (r.message) {
              var task = r.message;
              console.log(task);
            }
          },
        });
      }
    );
  },
});
