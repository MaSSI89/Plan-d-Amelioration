from odoo import fields, models

class Direction(models.Model):
    _name = "pdca.direction"
    _description = "les directions"

    name = fields.Char('Nom Direction:', required=True)
    cree_le = fields.Date('Date de creation') 
    referent = fields.Many2one('pdca.employe','Referent')
    directeur = fields.Many2one('pdca.employe','Directeur')
    les_unites_ids = fields.One2many('pdca.unite','direction_id',string="Unites")
    les_actions_ids = fields.One2many('pdca.action','direction_id',string="Les Actions")
    les_employes_ids = fields.One2many('pdca.employe','direction_id',string="Les Employees")