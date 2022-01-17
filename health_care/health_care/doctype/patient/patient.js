// Copyright (c) 2022, Juve and contributors
// For license information, please see license.txt


frappe.ui.form.on('Patient', {
	refresh: function (frm) {
		
	},
	onload: function (frm) {
		if(frm.doc.date_of_birth){
			$(frm.fields_dict['age'].wrapper).html("Age : " + get_age(frm.doc.date_of_birth));
		}
	}
});

frappe.ui.form.on("Patient", "date_of_birth", function(frm) {
	if(frm.doc.date_of_birth){
		var today = new Date();
		var birthDate = new Date(frm.doc.date_of_birth);
		var age_str = get_age(frm.doc.date_of_birth);
		$(frm.fields_dict['age'].wrapper).html("Age : " + age_str);
	}
});

var get_age = function (birth) {
	var ageMS = Date.parse(Date()) - Date.parse(birth);
	var age = new Date();
	age.setTime(ageMS);
	var years = age.getFullYear() - 1970;
	return years + " Year(s) " + age.getMonth() + " Month(s) " + age.getDate() + " Day(s)";
};