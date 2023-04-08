from odoo import fields, models, api

class AffectationPilote(models.Model):
    _name = "pdca.affectation.pilote"
    _description = "Affectation Pilote"

    type_constat = fields.Char('Type Constat')
    origine_constat = fields.Char('Origine')
    constat_id = fields.Many2one('pdca.constat','Constat')
    pilote_id = fields.Many2one('pdca.employe','Pilote',required=True)


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
                    'deafault_direction_id': self.pilote_id.direction
                }
            }
    
    @api.model
    def default_get(self, fields):
        res = super(AffectationPilote, self).default_get(fields)
        current_user = self.env.user.id
        print(res)
        print(fields)
        current_employe = self.env['pdca.employe'].search([('user_id','=',current_user)])
        print(current_employe)
        current_employe_direction = current_employe.direction_id.id
        print(current_employe_direction)
        pilote_ids = self.env['pdca.employe'].search([('direction_id','=',current_employe_direction)]).ids
        res['pilote_id'] = pilote_ids
        print(res['pilote_id'])
        return res
    

