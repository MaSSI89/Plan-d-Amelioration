from odoo import models , fields

class Action(models.Model):
    _name = "pdca.action"
    _description = "Les Actions"


    action = fields.Text('Action:')
    cause = fields.Char('Cause')
    risque = fields.Char('Risque')
    opportunite = fields.Char('Opportunite')
    commentaire = fields.Text('Commentaire')
    moyen = fields.Char('Moyen:')
    date_fin_previsionelle = fields.Date('Date FIn Previsionelle:')
    direction_id = fields.Many2one('pdca.direction','Direction')
    constat_id = fields.Many2one('pdca.constat', 'Constat')
    pilote_id = fields.Many2one('pdca.employe','Pilote')
    type_action = fields.Selection([
        ('corrective','Action Corrective'),
        ('preventive','Action Preventive'),
        ('amelioration','Action Amelioration'),
        ('non_retenue', 'Non Retenue')
    ],string="Type Action")
    type_risque = fields.Selection([
        ('qualite','Qualite'),
        ('finance', 'Finance')
    ],string="Type Risque")
    taux_avancement = fields.Integer(default=0,string="Taux Avancement")
    statut_action = fields.Selection([
        ('non entamee', 'Non Entame'),
        ('en attente validation','En Attente Validation'),
        ('en cours','En Cours'),
        ('en attente approbation','En Attente Approbation'),
        ('approuve','Approuvee'),
        ('realise','Realise'),
        ('solde','Soldee'),
        ('abandone','Abondanne'),
    ], default='non entamee', string='Statut Action')


