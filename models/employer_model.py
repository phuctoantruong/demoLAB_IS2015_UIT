# -*- coding: utf-8 -*-
from openerp import models, fields

class Employer(models.Model):
    _name = 'employer.management'
    _description = 'Employer Management'
    
    name = fields.Char(string='Author Name', required=True)
    birthday = fields.Date(string='BirthDay')
    address = fields.Char(string='Address')
    email = fields.Char(string='eMail')
    phone_number = fields.Char(string='Phone Number')
    salary = fields.Float(string='Salary')
    department_id = fields.Many2one('department.management', string="Department ID")
    