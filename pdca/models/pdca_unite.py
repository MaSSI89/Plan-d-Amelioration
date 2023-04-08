from odoo import models, fields

class Unite(models.Model):
    _name = "pdca.unite"
    _description = "UNite"

    name = fields.Char('Nom De Unite', required=True)
    directeur_id = fields.Many2one('pdca.employe', required=True)
    direction_id = fields.Many2one('pdca.direction', 'Direction')
    les_processus = fields.One2many('pdca.processus','unite_id','Processus')
    