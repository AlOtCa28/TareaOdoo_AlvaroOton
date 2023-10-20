# -*- coding: utf-8 -*

from odoo import models, fields, api


class alvaro_oton(models.Model):
  _name = 'alvaro_oton.task'
  _description = 'alvaro_oton.task'

  name = fields.Char()
  descripcion = fields.Char()
  fecha = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
