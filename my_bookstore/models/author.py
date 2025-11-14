from odoo import models, fields

class BookstoreAuthor(models.Model):
    _name = 'bookstore.author'
    _description = 'Tác giả sách'
    _order = 'name'

    name = fields.Char('Tên tác giả', required = True)
    bio = fields.Text('Tiểu sử')

    book_ids = fields.One2many(
        'bookstore.book',
        'author_id',
        string='Sách đã viết'
    )