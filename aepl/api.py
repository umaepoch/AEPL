from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def fetch_po_value_l1(name,user_l1):
	print("l1 approver",name,user_l1)
	frappe.client.set_value("Purchase Order",name,"l1_approval",user_l1)

@frappe.whitelist()
def fetch_po_value_l2(name,user_l2):
	print("l2 approver",name,user_l2)
	frappe.client.set_value("Purchase Order",name,"l2_approval",user_l2)

@frappe.whitelist()
def fetch_po_value_less(name,user_approve_less):
	print("data",name,user_approve_less)
	print("name",name)
	frappe.client.set_value("Purchase Order",name,"approved_by",user_approve_less)
	
@frappe.whitelist()
def fetch_po_value_btn(name,user_approve_btn):
	print("data",name,user_approve_btn)
	print("name",name)
	frappe.client.set_value("Purchase Order",name,"approved_by",user_approve_btn)

@frappe.whitelist()
def fetch_po_value_mr(name,user_approve_mr):
	print("data",name,user_approve_mr)
	print("name",name)
	frappe.client.set_value("Purchase Order",name,"l3_approval",user_approve_mr)