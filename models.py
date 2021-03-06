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
    yatrip_id = fields.Many2one('yachtrip.yatrip')
    

class yatrip(models.Model):
    _name = 'yachtrip.yatrip'
    
    name = fields.Char(size=500,required=True)
    country = fields.Many2one("res.country",required=True)
    province = fields.Many2one("res.country.state",domain="[('country_id','=',country)]")
    price = fields.Float()
    currency = fields.Many2one("res.currency")
    yatriptype = fields.Many2one("yachtrip.yatrip.type")
    guests = fields.Selection([('04','0-4'),('06','0-6'),('68','6-8'),('810','8-10'),('1012','10-12'),('12+','12+')])
    #length = fields.One2many('yachtrip.yatrip.length','yatrip_id')
    length = fields.Float()
    builder = fields.Many2one('res.partner')
    broker = fields.Many2one('res.partner')
    last_refitted = fields.Date()
    max_speed = fields.Char(size=100)
    cruise_speed = fields.Char(size=100)
    description = fields.Html()
    images = fields.One2many('ir.attachment',compute='_get_images')

    def _get_images(self):
        for rec in self:
            attachments = self.env['ir.attachment'].search([('res_model','=','yachtrip.yatrip'),('res_id','=',rec.id)])
            self.images = attachments

    def attachment_tree_view(self, cr, uid, ids, context):
        domain = [
             '&', ('res_model', '=', 'yachtrip.yatrip'), ('res_id', 'in', ids),
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

class package(models.Model):
    _name = 'yachtrip.package'
    name = fields.Char(size=500,required=True)
    price = fields.Char(size=100)
    excepts= fields.Char(size=1000,required=True)
    content = fields.Html()
    special_benefit = fields.Boolean()
    active = fields.Boolean(default=True)
    add_date = fields.Datetime()
    days = fields.One2many('yachtrip.package.days','package')
    images = fields.One2many('ir.attachment',compute='_get_images')

    def _get_images(self):
        for rec in self:
            attachments = self.env['ir.attachment'].search([('res_model','=','yachtrip.package'),('res_id','=',rec.id)])
            self.images = attachments

    
    def attachment_tree_view(self, cr, uid, ids, context):
        domain = [
             '&', ('res_model', '=', 'yachtrip.package'), ('res_id', 'in', ids),
        ]
        print 'domain is %s' % domain
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
    
class pagekcage_days(models.Model):
    _name = 'yachtrip.package.days'
    package = fields.Many2one('yachtrip.package')
    name = fields.Char(size=500)
    excepts= fields.Char(size=1000,required=True)
    content = fields.Html()
    #images = fields.Many2one('ir.attachment',domain="[('res_model','=','yachtrip.package.days')]")
    images = fields.One2many('ir.attachment',compute='_get_images')
    attractions = fields.Many2many('yachtrip.package.days.attractions','day_id','attractions_id','days_attractions_rel')

    def _get_images(self):
        print 'days _get_images called'
        for rec in self:
            attachments = self.env['ir.attachment'].search([('res_model','=','yachtrip.package.days'),('res_id','=',rec.id)])
            self.images = attachments

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

class package_days_attractions(models.Model):
    _name = 'yachtrip.package.days.attractions'

    country = fields.Many2one("res.country",required=True)
    province = fields.Many2one("res.country.state",domain="[('country_id','=',country)]")
    name = fields.Char(size=1000,required=True)
    excepts= fields.Char(size=1000,required=True)
    images = fields.One2many('ir.attachment',compute='_get_images')
    
    def _get_images(self):
        print 'days _get_images called'
        for rec in self:
            attachments = self.env['ir.attachment'].search([('res_model','=','yachtrip.package.days.attractions'),('res_id','=',rec.id)])
            self.images = attachments

class package_destination(models.Model):
    _name = 'yachtrip.destination'
    
    name = fields.Char(size=1000,required=True)
    country = fields.Many2one("res.country",required=True)
    province = fields.Many2one("res.country.state",domain="[('country_id','=',country)]")
    excepts = fields.Text(required=True)
    content = fields.Html()
    attractions = fields.Many2many('yachtrip.package.days.attractions','day_id','attractions_id','days_attractions_rel')
    images = fields.One2many('ir.attachment',compute='_get_images')
    
    def _get_images(self):
        print 'days _get_images called'
        for rec in self:
            attachments = self.env['ir.attachment'].search([('res_model','=','yachtrip.destination'),('res_id','=',rec.id)])
            self.images = attachments
