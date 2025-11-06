# -*- coding: utf-8 -*-
from odoo import models, fields

class BookstorePublisher(models.Model):
    _name = 'bookstore.publisher'
    _description = 'Nhà xuất bản'
    _order = 'name'

    name = fields.Char('Tên NXB', required=True)

    book_ids = fields.One2many(
        'bookstore.book',
        'publisher_id',
        string='Sách đã xuất bản'
    )