import frappe

@frappe.whitelist()
def get_all_companies():
    return frappe.get_all("Companyy",
                        fields=["company_name",
                                "number_of_departments",
                                "number_of_employees",
                                "number_of_projects"])

@frappe.whitelist()
def get_company(company_name):
    company = frappe.get_doc("Companyy", company_name)
    return company.as_dict()

@frappe.whitelist()
def get_all_departments():
    return frappe.get_all("Departmentt",
                        fields=["department_name",
                                "company",
                                "number_of_employees",
                                "number_of_projects"])

@frappe.whitelist()
def get_department(department_name):
    department = frappe.get_doc("Departmentt", department_name)
    return department.as_dict()

@frappe.whitelist()
def create_employee(data):
    data = frappe.parse_json(data)
    employee = frappe.get_doc({
        "doctype": "Employeee",
        **data
    })
    employee.insert()
    frappe.db.commit()
    return employee.as_dict()

@frappe.whitelist()
def get_employees():
    return frappe.get_all("Employeee",
                        fields=["employee_name",
                                "email_address",
                                "mobile_number",
                                "address",
                                "company",
                                "department",
                                "designation",
                                "employee_status",
                                "hired_on",
                                "days_employed",
                                "number_of_assigned_projects"])

@frappe.whitelist()
def get_employee(employee_name):
    employee = frappe.get_doc("Employeee", employee_name)
    return employee.as_dict()

@frappe.whitelist()
def update_employee(employee_name, data):
    data = frappe.parse_json(data)
    employee = frappe.get_doc("Employeee", employee_name)
    for key, value in data.items():
        setattr(employee, key, value)
    employee.save()
    frappe.db.commit()
    return employee.as_dict()

@frappe.whitelist()
def delete_employee(employee_name):
    frappe.delete_doc("Employeee", employee_name, force=1)
    frappe.db.commit()
    return {"message": f"Employee {employee_name} deleted successfully"}

@frappe.whitelist()
def create_project(data):
    data = frappe.parse_json(data)
    project = frappe.get_doc({
        "doctype": "Projectt",
        **data

    })
    project.insert()
    frappe.db.commit()
    return project.as_dict()

@frappe.whitelist()
def get_projects():
    return frappe.get_all("Projectt",
                            fields=["project_name",
                                    "description",
                                    "company",
                                    "department",
                                    "start_date",
                                    "end_date"])

@frappe.whitelist()
def get_project(project_name):
    project = frappe.get_doc("Projectt", project_name)
    return project.as_dict()

@frappe.whitelist()
def update_project(project_name, data):
    data = frappe.parse_json(data)
    project = frappe.get_doc("Projectt", project_name)
    for key, value in data.items():
        setattr(project, key, value)
    project.save()
    frappe.db.commit()
    return project.as_dict()

@frappe.whitelist()
def delete_project(project_name):
    frappe.delete_doc("Projectt", project_name, force=1)
    frappe.db.commit()
    return {"message": f"Project {project_name} deleted successfully"}

