from odoo import fields, models

class Processus(models.Model):
    _name = "pdca.processus"
    _description = "Processus d'une Unite"

    name = fields.Char('Nom De Processus')
    directeur_id = fields.Many2one('res.partner', 'Directeur')
    unite_id = fields.Many2one('pdca.unite', 'Unite :')

