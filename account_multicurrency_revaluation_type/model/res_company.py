# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    revaluation_rate_type = fields.Selection(
        string="Rate type",
        selection=[
            ('average', 'Average'),
            ('daily', 'Daily'),
        ],
        default='daily')
