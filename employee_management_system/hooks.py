app_name = "employee_management_system"
app_title = "employee_management_system"
app_publisher = "omarmagdy2@gmail.com"
app_description = "Employee Management System Utilities"
app_email = "omarmagdy2k@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/employee_management_system/css/employee_management_system.css"
# app_include_js = "/assets/employee_management_system/js/employee_management_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/employee_management_system/css/employee_management_system.css"
# web_include_js = "/assets/employee_management_system/js/employee_management_system.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "employee_management_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "employee_management_system.utils.jinja_methods",
# 	"filters": "employee_management_system.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "employee_management_system.install.before_install"
# after_install = "employee_management_system.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "employee_management_system.uninstall.before_uninstall"
# after_uninstall = "employee_management_system.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "employee_management_system.utils.before_app_install"
# after_app_install = "employee_management_system.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "employee_management_system.utils.before_app_uninstall"
# after_app_uninstall = "employee_management_system.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "employee_management_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
	"Companyy": {
		"on_load": "employee_management_system.employee_management_system.doctype.companyy.onload"
	},
    "Employeee": {
		"on_load": "employee_management_system.employee_management_system.doctype.employeee.onload"
    },
    "Projectt": {
        "on_load": "employee_management_system.employee_management_system.doctype.projectt.projectt.onload"
    },
    "Departmentt": {
		"on_load": "employee_management_system.employee_management_system.doctype.departmentt.onload"
	}

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"employee_management_system.tasks.all"
# 	],
# 	"daily": [
# 		"employee_management_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"employee_management_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"employee_management_system.tasks.weekly"
# 	],
# 	"monthly": [
# 		"employee_management_system.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "employee_management_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "employee_management_system.event.get_events"
# }
override_whitelisted_methods = {
    "get_all_companies": "employee_management_system.employee_management_system.api.get_all_companies",
    "get_company" : "employee_management_system.employee_management_system.api.",
    "get_all_departments": "employee_management_system.employee_management_system.api.get_all_departments",
    "get_department" : "employee_management_system.employee_management_system.api.",
    "create_employee": "employee_management_system.employee_management_system.api.create_employee",
    "get_employees": "employee_management_system.employee_management_system.api.get_employees",
    "get_employee" : "employee_management_system.employee_management_system.api.get_employee",
    "update_employee": "employee_management_system.employee_management_system.api.update_employee",
    "delete_employee": "employee_management_system.employee_management_system.api.delete_employee",
    "create_project": "employee_management_system.employee_management_system.api.create_project",
    "get_projects": "employee_management_system.employee_management_system.api.get_projects",
    "get_project" : "employee_management_system.employee_management_system.api.get_project",
    "update_project": "employee_management_system.employee_management_system.api.update_project",
    "delete_project": "employee_management_system.employee_management_system.api.delete_project"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "employee_management_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["employee_management_system.utils.before_request"]
# after_request = ["employee_management_system.utils.after_request"]

# Job Events
# ----------
# before_job = ["employee_management_system.utils.before_job"]
# after_job = ["employee_management_system.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"employee_management_system.auth.validate"
# ]
