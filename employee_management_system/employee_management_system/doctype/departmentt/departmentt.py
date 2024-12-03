# Copyright (c) 2024, omarmagdy2@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Departmentt(Document):
	def validate(self):
		self.calculate_aggregates()

	def onload(self):
		self.calculate_aggregates()

	def before_delete(self):
		employees = frappe.get_all("Employeee", filters={"department": self.name})
		if employees:
			frappe.throw("Cannot delete a Department with assigned Employees.")

	def calculate_aggregates(self):
		self.number_of_employees = frappe.db.count('Employeee', {'department': self.name})
		self.number_of_projects = frappe.db.count('Projectt', {'department': self.name})
