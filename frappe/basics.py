####bench new-app feedback_management


####bench generate doctype feedback

##feedback_management/feedback_management/doctype/feedback/feedback.py



##bench --site your-site-name migrate

from __future__ import unicode_literals
import frappe

def get_data():
    return {
        'fieldname': 'feedback',
        'transa6ctions': [
            {
                'label': _('Feedback'),
                'items': ['Feedback']
            }
        ]
    }
    
    
    
    
    
    
    ////////
    from __future__ import unicode_literals
import frappe

class CustomerFeedback(frappe.DynamicLink):
    def validate(self):
        """
        Validates and submits customer feedback to the system.
        """
        # Code to process and store feedback in the Frappe database
        frappe.msgprint(f"Feedback from {self.customer_name} submitted successfully.")

@frappe.whitelist()
def get_user_input():
    # Section: Gather User Input
    customer_name = input("Enter your name: ")
    feedback_text = input("Provide your feedback: ")

    # Section: Process Feedback
    feedback_handler = CustomerFeedback(doctype="Customer Feedback")
    feedback_handler.customer_name = customer_name
    feedback_handler.feedback_text = feedback_text
    feedback_handler.validate()

if __name__ == "__main__":
    get_user_input()
    
    #################################Cost 
    # myapp/myapp/doctype/task/task.py
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Task(Document):
    pass  # Additional fields and methods can be added based on user stories

# Sample code to create a new task
def create_new_task(title, description, due_date):
    new_task = frappe.new_doc("Task")
    new_task.title = title
    new_task.description = description
    new_task.due_date = due_date
    new_task.insert()
    frappe.msgprint(f"Task '{title}' created successfully.")
    
    
    ###cd /path/to/parent/directory


