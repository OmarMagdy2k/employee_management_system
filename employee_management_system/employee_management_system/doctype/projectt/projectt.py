# Copyright (c) 2024, omarmagdy2@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Projectt(Document):
	def validate(self):
		self.validate_assigned_employees()
		self.validate_department_relationship()
		update_company_counts(self.company)
		update_department_counts(self.department)

	def onload(self):
		self.calculate_number_of_project_assigned()

	def validate_assigned_employees(self):
		for assigned in self.assigned_employees:
			employee = frappe.get_doc("Employeee", assigned.employee)
			if employee.company != self.company or employee.department != self.department:
				frappe.throw(f"Employee {employee.name} is not part of the selected Company or Department.")

	def validate_department_relationship(self):
		department = frappe.get_doc("Departmentt", self.department)
		if department.company != self.company:
			frappe.throw("Selected Department does not belong to the selected Company.")

	def calculate_number_of_project_assigned(self):
			employees = frappe.get_all("Employeee", fields=["name"])
			for employee in employees:
				# Count projects where the employee is in the "assigned employee" field
				assigned_projects_count = frappe.db.count(
					"Assigend Employees",
					filters={"employee": ["like", f"%{employee['name']}%"]}
				)
				frappe.msgprint(f"Number of Projects for emp : {employee['name']} is {assigned_projects_count}")
				# Update the number_of_assigned_projects field
				frappe.db.set_value(
					"Employeee",
					employee["name"],
					"number_of_assigned_projects",
					assigned_projects_count
				)
				frappe.db.commit()

@frappe.whitelist()
def update_company_counts(company_id):
    company = frappe.get_doc("Companyy", company_id)
    project_count = frappe.db.count("Projectt", filters={"company": company_id})
    company.number_of_projects = project_count
    company.save()
    frappe.db.commit()


@frappe.whitelist()
def update_department_counts(department_id):
    department = frappe.get_doc("Departmentt", department_id)
    project_count = frappe.db.count("Projectt", filters={"department": department_id})
    department.number_of_projects = project_count
    department.save()
    frappe.db.commit()