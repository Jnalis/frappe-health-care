# Copyright (c) 2022, Juve and contributors
# For license information, please see license.txt

# import frappe
from frappe import _
from frappe.model.document import Document, frappe

# from frappe.model.document import frappe


class PatientAppointment(Document):
	def before_save(self):

		# get patients info
		get_patient_info = frappe.get_doc("Patient", self.patient)
		# frappe.msgprint(str(get_patient_info))
		self.patient_name = f'{get_patient_info.full_name or ""}'
		self.gender = f'{get_patient_info.gender or ""}'
		self.age = f'{get_patient_info.age or ""}'

		# geting practitioners info
		get_practitioner_info = frappe.get_doc("Practitioner", self.practitioner)
		self.practitioner_name = f'{get_practitioner_info.practitioner_full_name or ""}'
		self.practitioner_department = f'{get_practitioner_info.department or ""}'

		self.append_appointment_details()


	def append_appointment_details(self):
		if self.invoiced:
			return
		else:
			if not self.item_charged or self.amount_paid:
				item_to_charge = frappe.get_last_doc('Item', filters={
					'is_consultation': 1,
					'consultation_type': self.appointment_type
				})

				if item_to_charge:
					self.invoiced = 1
					self.item_charged = item_to_charge.name
					self.amount_paid = item_to_charge.item_price
		
		
		
		
		
		
		
