# Copyright (c) 2022, Juve and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Patient(Document):
	# this method will run every time a document is saved
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	def get_age(self): 
		age_str = ""
		if self.date_of_birth:
			born = getdate(self.date_of_birth)
			age = dateutil.relativedelta.relativedelta(getdate(), born)
			age_str = str(age.years) + " year(s) " + str(age.months) + " month(s) " + str(age.days) + " day(s)"
		self.age = age_str
