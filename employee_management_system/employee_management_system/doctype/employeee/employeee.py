# Copyright (c) 2024, omarmagdy2@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, date
ALLOWED_TRANSITIONS = {
    "Application Received": ["Interview Scheduled", "Not Accepted"],
    "Interview Scheduled": ["Hired", "Not Accepted"],
    "Not Accepted": ["Interview Scheduled"],
    "Hired": [] 
}

class Employeee(Document):
	def validate(self):
		self.validate_email()
		self.validate_mobile_number()
		self.validate_department_relationship()

	def before_validate(self):
		if self.employee_status == "Hired" :
			self.calculate_number_of_project_assigned()
			if self.hired_on:
				self.calculate_days_employed()
		else :
			pass

	def onload(self):
		if self.employee_status == "Hired" :
			self.calculate_number_of_project_assigned()
			if self.hired_on:
				self.calculate_days_employed()
		else :
			pass
	
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

	def validate_email(self):
		if not frappe.utils.validate_email_address(self.email_address):
			frappe.throw(f"Invalid email format: {self.email_address}")

	def validate_mobile_number(self):
		if len(self.mobile_number.split('-')[-1]) != 10 :
			frappe.throw(f"Invalid Length for Mobile Number: {self.mobile_number}")
		if not self.mobile_number.split('-')[-1].isdigit():
			frappe.throw(f"Mobile Number Must be ONLY Numbers: {self.mobile_number}")


	def calculate_days_employed(self):
		today = datetime.today()
		hired_on_date = check_hiring_date_type(self.hired_on)
		days_with_company = (today - hired_on_date).days  # Extract days from timedelta
		self.days_employed = days_with_company
		self.db_update()

	def validate_department_relationship(self):
		department = frappe.get_doc("Departmentt", self.department)
		if department.company != self.company:
			frappe.throw("Selected Department does not belong to the selected Company.")



def check_hiring_date_type(date_of_hire):
    if isinstance(date_of_hire, str):
        return datetime.strptime(date_of_hire, "%Y-%m-%d")
    elif isinstance(date_of_hire, date):
        return datetime.combine(date_of_hire, datetime.min.time())
    return date_of_hire

def validate_employee_status(doc, method=None):
    previous_status = frappe.db.get_value("Employeee", doc.name, "employee_status")
    new_status = doc.employee_status

    if previous_status == new_status:
        return

    if previous_status and new_status not in ALLOWED_TRANSITIONS.get(previous_status, []):
        frappe.throw(
            f"Invalid status transition from '{previous_status}' to '{new_status}'."
        )

@frappe.whitelist()
def change_employee_status(employee_id, new_status):
    doc = frappe.get_doc("Employeee", employee_id)
    doc.employee_status = new_status
    doc.save()
    frappe.db.commit()
    return f"Employee status updated to {new_status}"