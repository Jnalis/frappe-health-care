# Copyright (c) 2022, Juve and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document, frappe

# from frappe.model.document import frappe


class PatientAppointment(Document):
    def before_save(self):

		# get patients info
        get_patient_info = frappe.get_doc("Patient", self.patient)
        # frappe.msgprint(str(get_patient_info))
        self.patient_name = f'{get_patient_info.full_name or ""}'
        self.gender = f'{get_patient_info.gender or ""}'

        # geting practitioners info
        get_practitioner_info = frappe.get_doc("Practitioner", self.practitioner)
        self.practitioner_name = f'{get_practitioner_info.practitioner_full_name or ""}'
        self.practitioner_department = f'{get_practitioner_info.department or ""}'
		
