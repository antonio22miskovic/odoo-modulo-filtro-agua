# -*- coding: utf-8 -*-

from odoo import models, fields, api

class filtro_agua(models.Model):
    _name = 'fa.filtro_agua'
    _rec_name='serial'

    # ATRIBUTOS
    array = [ ('sansumg', 'sansumg'),('LG', 'LG'),('Frigilux','Frigilux') ]
    serial = fields.Char(string='Serial',required=True)
    marca = fields.Selection(array,required=True)
    temperatura = fields.Float(string='Temperatura',required=True)
    dispensadores = fields.Integer(string='Dispensadores',required=True,default=2)
    date = fields.Date(string='Fecha inicio',required=True,default=fields.Date.today())
    fecha_garantia = fields.Datetime(string='Garantia', required=True)
    gabinete = fields.Boolean(string='Gabinete',required=True)
    
    persona_id = fields.Many2one('res.partner' ,string='Popietario',required=True)
    botellones = fields.One2many('fa.botellon', 'filtro_id', string='Botellones',required=True)
    departamentos_ids = fields.Many2many('fa.departamento',string='Depratamentos',required=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100