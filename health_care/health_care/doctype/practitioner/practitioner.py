# Copyright (c) 2022, Juve and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Practitioner(Document):
	def before_save(self):
		self.practitioner_full_name = f'{self.first_name} {self.second_name or ""}'
