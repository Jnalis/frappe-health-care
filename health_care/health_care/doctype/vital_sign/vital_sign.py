# Copyright (c) 2022, Juve and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VitalSign(Document):
	def before_save(self):
		self.patient_name = f'{self.patient or ""}'
