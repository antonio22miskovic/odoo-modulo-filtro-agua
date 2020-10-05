from odoo import models, fields, api

class vasos_agua(models.Model):
    _name = 'fa.vasos_agua'

    colores = [ ('negro','negro'), ('blanco','blanco'),('rojo','rojo') ]
    color     = fields.Selection(colores,required=True)
    litros    = fields.Float(string='Cantidad en litros',required=True)
    status    = fields.Boolean(string='vacio',required=True)
    filtro_id = fields.Many2one('fa.filtro_agua',string='Filtro de Aguas')
