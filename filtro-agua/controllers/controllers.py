# -*- coding: utf-8 -*-
from odoo import http

# class Filtro-agua(http.Controller):
#     @http.route('/filtro-agua/filtro-agua/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filtro-agua/filtro-agua/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('filtro-agua.listing', {
#             'root': '/filtro-agua/filtro-agua',
#             'objects': http.request.env['filtro-agua.filtro-agua'].search([]),
#         })

#     @http.route('/filtro-agua/filtro-agua/objects/<model("filtro-agua.filtro-agua"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filtro-agua.object', {
#             'object': obj
#         })