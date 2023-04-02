from odoo import fields, models, api
import logging

class Constat(models.Model):
    _name = "pdca.constat"
    _description = "Constats"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    document = fields.Binary('DOcument:')
    name = fields.Text('Constat:')
    type_constat = fields.Selection([('fort','Point fort'),
                                     ('progre','Piste de Progres'),
                                     ('sensible','Point Sensible'),
                                     ('recommendation','Recommendation'),
                                     ('recommendation_maj','Recommendation Majeure'),
                                     ('observation','Observation')],string="Type Constat")
    direction_concerne = fields.Many2one('pdca.direction', string="Direction Concernees")
    activite = fields.Many2one('pdca.unite',string="Activite")
    # processus = fields.One2many('pdca.processus',string="Processus")
    # direction_pilote = fields.One2many('pdca.direction',string="Direction Pilote")
    
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
    
    def send_mail_notif(self):
        template_id = self.env.ref('pdca.creation_constat_email')
        for rec in self:
            template_id.send_mail(rec.id, force_send=True)
        return
        
    
    @api.model
    def create(self, vals):
        record = super(Constat, self).create(vals)
        record.send_mail_notif()
        return record
    
 
