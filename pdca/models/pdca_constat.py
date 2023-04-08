from odoo import fields, models, api
from odoo.exceptions import UserError
class Constat(models.Model):
    _name = "pdca.constat"
    _description = "Constats"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    document = fields.Binary('Document:')
    name = fields.Text('Constat:',required=True)
    genere_action = fields.Boolean('Le Constat genere une action ?:',required=True)
    type_constat = fields.Selection([('fort','Point fort'),
                                     ('progre','Piste de Progres'),
                                     ('sensible','Point Sensible'),
                                     ('recommendation','Recommendation'),
                                     ('recommendation_maj','Recommendation Majeure'),
                                     ('observation','Observation')],string="Type Constat")
    direction_concerne_ids = fields.Many2many('pdca.direction', string="Direction Concernees",required=True)
    activite_id = fields.Many2one('pdca.unite',string="Activite",required=True)
    processus_id = fields.Many2one('pdca.processus',string="Processus",required=True)
    direction_pilote_ids = fields.Many2many('pdca.direction','id',string="Direction Pilote",required=True)
    les_actions_ids = fields.One2many('pdca.action', 'constat_id','Les Actions:')
    statut = fields.Selection([
        ('ouvert','Ouvert'),
        ('supprime','Supprimé'),
        ('solde','Soldé')
    ],default="ouvert")
    origine = fields.Selection([
                            ('blanc', 'Audit à blanc'),
                            ('ema', 'Audit externe EMA'),
                            ('iso45', 'Audit externe ISO 45001'),
                            ('iso90', 'Audit externe ISO 9001'),
                            ('2iso', 'Audit externe iso 9001 et 45001'),
                            ('externe', 'Audit externe métier'),
                            ('interne', 'Audit interne'),
                            ('bhe', 'BHE'),
                            ('boite', 'Boite à idée'),
                            ('mystere', 'Enquête mystère QdS'),
                            ('satisfactionVOyage', 'Enquête satisfaction voyageurs'),
                            ('satisfactionEMA', 'Enquêtes satisfaction EMA'),
                            ('exercices', 'Exercices / Simulations'),
                            ('fiche', 'Fiche d\'Amélioration et de Progrès'),
                            ('incident', 'incident / Accident'),
                            ('innov', 'Innov & Go'),
                            ('hse', 'Inspection HSE'),
                            ('qualite', 'Inspection Qualité'),
                            ('securite', 'Inspection sécurité ferroviaire'),
                            ('inspectionSecurite', 'Inspection sécurité incendie'),
                            ('inspectionSurete', 'Inspection Sureté'),
                            ('rapportAnnuel', 'Rapport Annuel d\'Activité'),
                            ('rapportMensuel', 'Rapport Mensuel d\'Activité'),
                            ('rapportMetier', 'Rapport Métier'),
                            ('revueDirection', 'Revue de Direction'),
                            ('revueAmelioration', 'Revue du Plan d\'Amélioration'),
                            ('riskManagement', 'Risk management'),
                            ('conformite', 'Conformité légale'),
                            ('auditCertification', 'Audit de certification')],'Origine')
    
    def creer_constat_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        constat_form_url = '/web#id=%d&action=310&model=pdca.constat&view_type=form&cids=&menu_id=222' % self.id
        print(base_url+constat_form_url)
        return base_url + constat_form_url
    
    def send_mail_notif(self):
        for rec in self:
            template_id = self.env.ref('pdca.creation_constat_email')
            self.creer_constat_url()
            template_id.send_mail(rec.id, force_send=True)
        return
        
    # passer les emails de referent et directeur de direction_pilote 
    def pass_dir_pilote_emails(self):
        dir_pilote_ids = self.direction_pilote_ids.ids
        dir_pilote_records = self.env['pdca.direction'].search([('id','in',dir_pilote_ids)])
        personnes_concernes = ''
        for dir_pilote in dir_pilote_records:
            if dir_pilote.directeur.email not in personnes_concernes:
                personnes_concernes += dir_pilote.directeur.email + ','
            if dir_pilote.referent.email not in personnes_concernes:
                personnes_concernes += dir_pilote.referent.email + ','

        personnes = personnes_concernes.rstrip(",")
        return personnes
    
    # pour Envoyer un mail quand constat fort et genere pas action    
    def send_mail_constat_fort(self):
        print('INVOKED')
        print(self)
        for rec in self:
            print('IN THE LOOP')
            template_id = self.env.ref('pdca.mail_constat_fort')
            self.creer_constat_url()
            template_id.send_mail(rec.id, force_send=True)
            print('NRMLMNT TROH')
        return

    @api.model
    def create(self, vals):
        record = super(Constat, self).create(vals)    
        # record.pass_dir_pilote_emails()
        if vals['type_constat'] == 'fort': 
            print('COnstat type fort')
            if not vals['genere_action']:
                print('N eGenere pas Actions')
                record.send_mail_constat_fort()
                return record
            
        record.send_mail_notif()
        return record

    def affecter_pilote(self):
        return {
            'res_model': 'pdca.affectation.pilote',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('pdca.pdca_affectation_pilote_view_form').id, 
            'context': {
                'default_constat_id' : self.id,
                'default_type_constat': self.type_constat,
                'default_origine_constat': self.origine,
            }
        }

    @api.onchange('direction_pilote_ids')
    def _onchange_(self):
        if self.direction_pilote_ids :
            # recherche des unites de direction concernees:
            activite_domain = [('direction_id','in',self.direction_pilote_ids.ids)]
            print(self.direction_pilote_ids.ids)
            return {'domain': {'activite_id': activite_domain}}
        else:
            self.activite_id = []

    @api.onchange('activite_id')       
    def onchange_unite_id(self):
        if self.activite_id:
            processus_domain = [('unite_id','=',self.activite_id.id)]
            return {'domain': {'processus_id': processus_domain}}
        else:
            self.processus_id = []
            print(self.processus_id)
 
