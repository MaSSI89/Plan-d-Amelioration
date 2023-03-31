from odoo import fields, models

class Processus(models.Model):
    _name = "pdca.processus"
    _description = "Processus d'une Unite"

    name = fields.Char('Nom De Processus')
    directeur = fields.Many2one('res.partner', 'Directeur')
    unite = fields.Many2one('pdca.unite', 'Unite :')

