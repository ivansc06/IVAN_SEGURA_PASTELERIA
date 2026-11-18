# -*- coding: utf-8 -*-
{
    'name': "LET HIM COOK",
    'summary': "Gestión de una pastelería de alta gama",
    'description': "Aplicación de gestión de la pastelería LET HIM COOK",
    'author': "Ivan",
    'website': "",
    'category': "Tools",
    'version': '0.1',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/empleado.xml',
    'views/pedido.xml',
    'views/producto.xml',
    'views/proveedor.xml',
    'views/menu.xml',
    'demo/demo.xml',
],

    'installable': True,
    'application': True,
}