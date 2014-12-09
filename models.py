from openerp import fields
from openerp import models
from openerp.tools.translate import _


class yatrip_type(models.Model):
    _name = 'yachtrip.yatrip.type'
    name = fields.Char(size=100)

class yatrip_length(models.Model):
    _name = 'yachtrip.yatrip.length'
    name = fields.Selection([('ft','FT'),('m','M')])
    m_length = fields.Float()
    ft_length = fields.Float()
    

class yatrip(models.Model):
    _name = 'yachtrip.yatrip'
    
    name = fields.Char(size=500)
    country = fields.Many2one("res.country")
    province = fields.Many2one("res.country.state",domain="[('country_id','=',country)]")
    price = fields.Float()
    currency = fields.Many2one("res.currency")
    yatriptype = fields.Many2one("yachtrip.yatrip.type")
    guests = fields.Selection([('0-4','04'),('0-6','06'),('6-8','68'),('8-10','810'),('10-12','1012'),('12+','12+')])
    length = fields.Many2one('yachtrip.yatrip.length')
    builder = fields.Many2one('res.partner')
    broker = fields.Many2one('res.partner')
    last_refitted = fields.Date()
    max_speed = fields.Char(size=100)
    cruise_speed = fields.Char(size=100)
    description = fields.Html()


class package(models.Model):
    _name = 'yachtrip.package'
    name = fields.Char(size=500)
    price = fields.Char(size=100)
    excepts= fields.Char(size=1000)
    content = fields.Html()
    special_benefit = fields.Boolean()
    create_date = fields.Datetime()

    #images = fields.Many2one('ir.attachment',domain="[('res_model','=','yachtrip.package')]")
    
    def attachment_tree_view(self, cr, uid, ids, context):
        domain = [
             '&', ('res_model', '=', 'yachtrip.package'), ('res_id', 'in', ids),
        ]
        res_id = ids and ids[0] or False
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, res_id)
        }
    
class pagekcage_days(models.Model):
    _name = 'yachtrip.package.days'
    name = fields.Char(size=500)
    content = fields.Html()
    #images = fields.Many2one('ir.attachment',domain="[('res_model','=','yachtrip.package.days')]")
    
    def attachment_tree_view(self, cr, uid, ids, context):
        domain = [
             '&', ('res_model', '=', 'yachtrip.package.days'), ('res_id', 'in', ids),
        ]
        res_id = ids and ids[0] or False
        return {
            'name': _('Images'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, res_id)
        }
        
