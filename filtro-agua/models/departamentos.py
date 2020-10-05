from odoo import models, fields, api

class departamentos(models.Model):
    _name = 'fa.departamento'
    _rec_name='name'

    colores = [ ('redes','redes'), ('analistas','analistas'), ('desarrollo','desarrollo') ]
    name = fields.Char(string='Departamento',required=True)
    tipos  = fields.Selection(colores,required=True, string="Clasificación")
    filtros_ids = fields.Many2many('fa.filtro_agua',string='Filtros')

   