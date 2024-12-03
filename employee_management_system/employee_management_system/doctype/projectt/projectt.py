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
		for row in self.assigned_employees:
			update_project_count(row.employee,self.name)

	def validate_assigned_employees(self):
		for assigned in self.assigned_employees:
			employee = frappe.get_doc("Employeee", assigned.employee)
			if employee.company != self.company or employee.department != self.department:
				frappe.throw(f"Employee {employee.name} is not part of the selected Company or Department.")

	def validate_department_relationship(self):
		department = frappe.get_doc("Departmentt", self.department)
		if department.company != self.company:
			frappe.throw("Selected Department does not belong to the selected Company.")


@frappe.whitelist()
def update_project_count(employee_id, project_id):
    employee = frappe.get_doc("Employeee", employee_id)
    project_count = frappe.db.count("Assigend Employees", filters={"employee": employee_id, "parent": project_id})
    employee.number_of_assigned_projects = project_count
    employee.save(ignore_permissions=True)
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