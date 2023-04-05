from odoo import models , fields

class Action(models.Model):
    _name = "pdca.action"
    _description = "Les Actions"


    constat_id = fields.Many2one('pdca.constat', 'Constat')
    action = fields.Text('Action:')
    cause = fields.Char('Cause')
    risque = fields.Char('Risque')
    opportunite = fields.Char('Opportunite')
    commentaire = fields.Text('Commentaire')
    moyen = fields.Char('Moyen:')
    date_fin_previsionelle = fields.Date('Date FIn Previsionelle:')
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


