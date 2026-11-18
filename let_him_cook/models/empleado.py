
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class empleado(models.Model):

    _name = "let_him_cook.empleado"
    _description = "Clase de empleado"

    nombreEmpleado = fields.Char(
        string="Nombre Empleado",
        required=True,
        help="Nombre del empleado"
    )

    apellidoEmpleado = fields.Char(
        string="Apellido Empleado",
        required=True,
        help="Apellido del empleado"
    )

    nombreCompleto = fields.Char(
        string="Nombre Completo",
        compute="_compute_nombre_completo",
        store=True
    )

    edadEmpleado = fields.Integer(
        string="Edad Empleado",
        help="Edad del empleado",
        default=18
    )

    puestoEmpleado = fields.Selection(
        selection=[
            ("pastelero", "Pastelero Profesional"),
            ("repostero", "Repostero"),
            ("dependiente", "Dependiente"),
            ("encargado", "Encargado"),
            ("gerente", "Gerente")
        ],
        string="Puesto del empleado",
        required=True,
        default="pastelero"
    )

    salarioEmpleado = fields.Float(
        string="Salario Empleado",
        help="Salario mensual del empleado",
        default=0.0
    )

    fechaNacimientoEmpleado = fields.Date(
        string="Fecha de nacimiento"
    )

    fechaContratacionEmpleado = fields.Date(
        string="Fecha de contratación"
    )

    observacionesEmpleado = fields.Text(
        string="Observaciones"
    )

    activoEmpleado = fields.Boolean(
        string="Empleado activo",
        default=True
    )

    pedido_ids = fields.One2many(
        comodel_name="let_him_cook.pedido",
        inverse_name="empleado_id",
        string="Pedidos gestionados"
    )

    @api.depends("nombreEmpleado", "apellidoEmpleado")
    def _compute_nombre_completo(self):
        for empleado in self:
            empleado.nombreCompleto = (
                (empleado.nombreEmpleado or "") + " " +
                (empleado.apellidoEmpleado or "")
            ).strip()

    @api.constrains("edadEmpleado")
    def _check_edad(self):
        for empleado in self:
            if empleado.edadEmpleado < 16:
                raise ValidationError(
                    "No tiene la edad adecuada para trabajar"
                )

    @api.constrains("salarioEmpleado")
    def _check_salario(self):
        for empleado in self:
            if empleado.salarioEmpleado < 0:
                raise ValidationError(
                    "El salario no puede ser negativo"
                )
