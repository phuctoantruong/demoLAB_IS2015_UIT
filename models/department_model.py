# -*- coding: utf-8 -*-
from openerp import models, fields, api, osv, _

class Department(models.Model):
    _name = 'department.management'
    _description = 'Department Management'
    
    name = fields.Char(string='Department Name', required=True)
    employer_ids = fields.One2many('employer.management', 'department_id', string="Employer IDs")
    getSalary = fields.Float(string='Get Salary')
    salary_ids = fields.One2many('get.salary', 'department_id', string='Salary List')
    
    @api.one
    def filter_salary(self):
        sql='''
            SELECT DISTINCT id, name, salary
            FROM employer_management
            WHERE department_id = '%s'
                AND salary < %s
        '''%(self.id, self.getSalary)
        self.env.cr.execute(sql)
#       Lấy dự liệu trả về kiểu: Dictionary
        res = {}
        for line in self.env.cr.dictfetchall(): 
            res={'salary': line['salary'] or '',
                        'name': line['name'] or '',
                        'employer_id': line['id'] or '',
                        'department_id': self.id or ''}
            salary_obj = self.env['get.salary']
            salary_obj.create(res)
#       Lấy dự liệu trả về kiểu: Tupple
#             salary_obj = self.env['get.salary']
#             salary_obj.create( {'salary' : line[2] ,
#                                 'name' : line[1],
#                                 'employer_id' : line[0],
#                                 'department_id' : self.id} )

# Table tạm lưu dự liệu SELECT
class Salary(models.Model):
    _name = 'get.salary'
    
    name = fields.Char(string='Name', required=True)
    salary = fields.Float(string='Salary')
    employer_id = fields.Many2one('employer.management')
    department_id = fields.Many2one('department.management', 'Department')