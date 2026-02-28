from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CustomerCreditLimit(models.Model):
    _name = 'customer.credit.limit'
    _description = 'Customer Credit Limit Management'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True, ondelete='cascade')
    credit_limit = fields.Monetary(string="Credit Limit", required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    active = fields.Boolean(default=True)
    note = fields.Text(string="Description")

    total_due = fields.Monetary(compute='_compute_amounts', store=True, string="Total Due")
    remaining_credit = fields.Monetary(compute='_compute_amounts', store=True, string="Remaining Credit")

    _sql_constraints = [
        ('unique_active_partner', 'unique(partner_id, active)', 'A partner can only have one active credit limit!')
    ]

    @api.depends('partner_id', 'partner_id.total_due', 'credit_limit')
    def _compute_amounts(self):
        for rec in self:
            # Accounting'dagi posted to'lanmagan invoice'lar summasi
            rec.total_due = rec.partner_id.total_due
            rec.remaining_credit = rec.credit_limit - rec.total_due

    @api.constrains('active', 'partner_id')
    def _check_unique_active(self):
        for rec in self:
            if rec.active:
                domain = [('partner_id', '=', rec.partner_id.id), ('active', '=', True), ('id', '!=', rec.id)]
                if self.search_count(domain) > 0:
                    raise ValidationError(_("This customer already has an active credit limit."))