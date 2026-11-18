
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class producto(models.Model):

    _name = "let_him_cook.producto"
    _description = "Clase de producto"

    nombreProducto = fields.Char(
        string="Nombre del Producto",
        required=True
    )

    descripcionProducto = fields.Text(
        string="Descripción"
    )

    precioProducto = fields.Float(
        string="Precio",
        required=True,
        default=0.0
    )

    cantidadProducto = fields.Integer(
        string="Cantidad Disponible",
        default=0
    )

    disponibleProducto = fields.Boolean(
        string="Producto Disponible",
        default=True
    )

    imagenProducto = fields.Binary(
        string="Imagen del Producto"
    )

    fechaCreacionProducto = fields.Date(
        string="Fecha de Creación"
    )

    fechaActualizacionProducto = fields.Datetime(
        string="Fecha de Actualización"
    )

    categoriaProducto = fields.Selection(
        selection=[
            ("tartas", "Tartas"),
            ("macarons", "Macarons"),
            ("bombones", "Bombones"),
            ("bolleria", "Bollería"),
            ("otros", "Otros")
        ],
        string="Categoría del Producto",
        required=True
    )

    valorStock = fields.Float(
        string="Valor del Inventario",
        compute="_compute_valor_stock",
        store=True
    )

    @api.depends("precioProducto", "cantidadProducto")
    def _compute_valor_stock(self):
        for producto in self:
            producto.valorStock = (
                producto.precioProducto * producto.cantidadProducto
            )

    @api.constrains("precioProducto")
    def _check_precio(self):
        for producto in self:
            if producto.precioProducto < 0:
                raise ValidationError(
                    "El precio no puede ser negativo"
                )

    @api.constrains("cantidadProducto")
    def _check_cantidad(self):
        for producto in self:
            if producto.cantidadProducto < 0:
                raise ValidationError(
                    "La cantidad no puede ser negativa"
                )
