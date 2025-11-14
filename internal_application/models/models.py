# -*- coding: utf-8 -*-
from odoo import models, fields


# Thêm một class mới kế thừa 'hr.employee'
class HrEmployeeInherit(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    x_hometown = fields.Char(string="Quê quán")
    x_ethnicity = fields.Char(string="Dân tộc")
    x_religion = fields.Char(string="Tôn giáo")

