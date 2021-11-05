# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': ' Editable margins in Sales Orders',
    "version": "14.0.1.0.0",
    'category': 'Sales/Sales',
    'description': """
This module give you the possibilite to edit margin in euro and margin in %.
=============================================

This gives the profitability by calculating the difference between the Unit
Price and Cost Price.
    """,
    "category": "Sale",
    'author': 'Odoo Consultant medconsultantweb@gmail.com',
    'website': 'http://www.weblemon.org',
    'price': '10.0',
    'currency': 'USD',
    'depends': ['sale_management', 'sale_margin','account'],
    'demo': [],
    'data': [
        'views/sale_margin_view.xml',
    ],
}
