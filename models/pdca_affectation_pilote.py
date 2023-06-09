from odoo import fields, models, api

class AffectationPilote(models.Model):
    _name = "pdca.affectation.pilote"

    constat_id = fields.Many2one('pdca.constat','Constat')
    pilote = fields.Many2one('res.users','Pilote')


    def creer_affectation_pilote_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        object_url=  '/web#id=%d&active_id=5&model=pdca.affectation.pilote&view_type=form&cids=1&menu_id=105' % self.id
        print(base_url+object_url)
        return base_url + object_url    

    def send_mail_notif(self):
        template_id = self.env.ref('pdca.affectation_constat_email')
        for rec in self:
            template_id.send_mail(rec.id, force_send=True)
        return
        
    
    @api.model
    def create(self, vals):
        record = super(AffectationPilote, self).create(vals)
        record.send_mail_notif()
        return record
    
    def pilote_creer_action(self):
          return {
                'res_model': 'pdca.action',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'view_id': self.env.ref('pdca.pdca_action_view_form').id,
                'context': {
                    'default_constat_id': self.constat_id.id,
                }
            }