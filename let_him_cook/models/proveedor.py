
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class proveedor(models.Model):

    _name = "let_him_cook.proveedor"
    _description = "Clase de proveedor"

    nombreProveedor = fields.Char(
        string="Nombre del Proveedor",
        required=True
    )

    cifProveedor = fields.Char(
        string="CIF/NIF",
        required=True
    )

    telefonoProveedor = fields.Char(
        string="Teléfono"
    )

    emailProveedor = fields.Char(
        string="Correo Electrónico"
    )

    direccionProveedor = fields.Char(
        string="Dirección"
    )

    tipoProveedor = fields.Selection(
        selection=[
            ("ingredientes", "Ingredientes"),
            ("frutas", "Frutas"),
            ("lacteos", "Lácteos"),
            ("chocolate", "Chocolate"),
            ("envases", "Envases"),
            ("huevos", "Huevos"),
            ("otros", "Otros")
        ],
        string="Tipo de proveedor",
        required=True,
        default="ingredientes"
    )

    fechaAltaProveedor = fields.Date(
        string="Fecha de Alta"
    )

    activoProveedor = fields.Boolean(
        string="Proveedor Activo",
        default=True
    )

    observacionesProveedor = fields.Text(
        string="Observaciones"
    )

    @api.constrains("emailProveedor")
    def _check_email(self):
        for proveedor in self:
            if proveedor.emailProveedor:
                patron = r"^[\w.-]+@[\w.-]+\.\w+$"

                if not re.match(patron, proveedor.emailProveedor):
                    raise ValidationError(
                        "El correo electrónico del proveedor no es válido"
                    )
