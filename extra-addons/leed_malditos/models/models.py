# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class leed_malditos(models.Model):
#     _name = 'leed_malditos.leed_malditos'
#     _description = 'leed_malditos.leed_malditos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

