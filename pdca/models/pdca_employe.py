from odoo import fields, models, api

class Employee(models.Model):
    _name="pdca.employe"
    _description = "Les Employees"
    _inherits = {'res.users': 'user_id'}

    user_id = fields.Many2one('res.users',ondelete='cascade')

    matricule = fields.Integer('Matricule:')
    matricule_cnas = fields.Integer('Matricule CNAS:')
    poste_occupe = fields.Char('Poste Occupe')
    direction_id = fields.Many2one('pdca.direction','Direction')
    

    @api.onchange('login')
    def onchnge_login(self):
        if self.login :
            self.email = self.login
        else :
            self.email = ''