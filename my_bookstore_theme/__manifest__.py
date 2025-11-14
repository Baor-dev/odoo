# my_bookstore_theme/__manifest__.py
{
    'name': 'My Bookstore Theme',
    'version': '1.0',
    'summary': 'Tùy chỉnh giao diện backend cho Bookstore',
    'author': 'Baao',
    'license': 'LGPL-3',
    'depends': [
        'web',
    ],

    # Đây là phần quan trọng nhất
    'assets': {
        'web.assets_backend': [
            # THAY ĐỔI:
            # Thay vì neo (anchor) vào 'style.scss' (đang bị lỗi),
            # chúng ta sẽ neo vào 'transitions.scss'.
            # Tệp này được nạp ngay TRƯỚC 'style.scss',
            # nên việc chèn tệp của chúng ta vào SAU nó là hoàn hảo.

            ('after', 'web/static/src/core/utils/transitions.scss', 'my_bookstore_theme/static/src/scss/my_theme.scss'),
        ],
    },

    'installable': True,
    'auto_install': False,
    'application': False,
}