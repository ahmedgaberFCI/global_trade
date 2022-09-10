# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    """Extend to add company registry."""

    _inherit = 'res.partner'

    company_registry = fields.Char(
        string="Company Registry",
    )

    @api.model
    def _commercial_fields(self):
        result = super(ResPartner, self)._commercial_fields()
        result.append('company_registry')
        return result
