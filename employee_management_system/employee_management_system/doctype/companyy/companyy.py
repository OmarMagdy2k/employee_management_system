# Copyright (c) 2024, omarmagdy2@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Companyy(Document):
	def validate(self):
		self.calculate_aggregates()
	
	def onload(self):
		self.calculate_aggregates()


	def before_delete(self):
		departments = frappe.get_all("Departmentt", filters={"company": self.name})
		if departments:
			frappe.throw("Cannot delete a Company with assigned Departments.")

	def calculate_aggregates(self):
		self.number_of_departments = frappe.db.count('Departmentt', {'company': self.name})
		self.number_of_employees = frappe.db.count('Employeee', {'company': self.name})
		self.number_of_projects = frappe.db.count('Projectt', {'company': self.name})
		self.db_update()

		# self.save()
		# self.reload()