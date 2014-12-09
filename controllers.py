# -*- coding: utf-8 -*-
from openerp import http

class Yachtrip(http.Controller):
    @http.route('/package',auth='public',website=True)
    def index(self):
        Packages = http.request.env['yachtrip.package']
        return http.request.render('yachtrip.index',{
            'eleaves':Packages.search([]),
        })

    @http.route('/package/<model("yachtrip.package"):item>/',auth='public',website=True)
    def package(self,item):
        return http.request.render('yachtrip.packageitem',{
            'item':item,
        })

    """
    @http.route('/academy/<int:id>/',auth='public',website=True)
    def teacher(self,id):
        return '<h1>{}{}</h1>'.format(id,type(id).__name__)

    @http.route('/academy/<model("academy.teachers"):teacher>/',auth='public',website=True)
    def teacher(self,teacher):
        return http.request.render('academy.biography',{
            'person':teacher,
        })
    """