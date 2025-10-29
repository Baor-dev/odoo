# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class DemoSuperhuman(models.Model):
    _name = 'demo.superhuman'
    _inherit = 'demo.human'
    _description = 'Demo Superhuman (Linked to Human)'

    # --- Các trường riêng của Superhuman ---
    superpower = fields.Char(string='Siêu năng lực', required=True, tracking=True)
    hero_name = fields.Char(string='Bí danh Siêu anh hùng', tracking=True)

    @api.model
    def create(self, vals):
        record = super(DemoSuperhuman, self).create(vals)
        _logger.info("✅ Created new Superhuman: %s (Power: %s)", record.hero_name, record.superpower)
        return record

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.hero_name or record.name} ({record.superpower})"
            result.append((record.id, name))
        return result



