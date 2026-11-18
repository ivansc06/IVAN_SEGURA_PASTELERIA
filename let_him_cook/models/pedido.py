
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class pedido(models.Model):

    _name = "let_him_cook.pedido"
    _description = "Clase de pedido"

    nombrePedido = fields.Char(
        string="Número de Pedido",
        required=True
    )

    fechaPedido = fields.Date(
        string="Fecha del Pedido"
    )

    fechaEntrega = fields.Date(
        string="Fecha de Entrega",
        required=True
    )

    fechaRegistro = fields.Datetime(
        string="Fecha y Hora de Registro"
    )

    estadoPedido = fields.Selection(
        selection=[
            ("pendiente", "Pendiente"),
            ("preparacion", "En Preparación"),
            ("listo", "Listo para Entregar"),
            ("entregado", "Entregado"),
            ("cancelado", "Cancelado")
        ],
        string="Estado del Pedido",
        default="pendiente",
        required=True
    )

    precioTotal = fields.Float(
        string="Precio Total",
        default=0.0,
        compute="SumaPrecioTotal"
    )

    observacionesPedido = fields.Text(
        string="Observaciones"
    )

    pedidoUrgente = fields.Boolean(
        string="Pedido Urgente",
        default=False
    )

    imagenPedido = fields.Binary(
        string="Imagen de Referencia"
    )

    empleado_id = fields.Many2one(
        comodel_name="let_him_cook.empleado",
        string="Empleado encargado"
    )

    producto_ids = fields.Many2many(
        comodel_name="let_him_cook.producto",
        relation="pedido_producto_rel",
        column1="pedido_id",
        column2="producto_id",
        string="Productos del pedido"
    )

    @api.depends("producto_ids.precioProducto")
    def SumaPrecioTotal(self):
        for pedido in self:
            total = sum(
                pedido.producto_ids.mapped("precioProducto")
            )

            if total < 0:
                raise UserError(
                    "El precio total no puede ser negativo"
                )

            pedido.precioTotal = total

    @api.constrains("fechaPedido", "fechaEntrega")
    def _check_fecha_entrega(self):
        for pedido in self:
            if pedido.fechaPedido and pedido.fechaEntrega:
                if pedido.fechaEntrega < pedido.fechaPedido:
                    raise ValidationError(
                        "La fecha de entrega no puede ser anterior "
                        "a la fecha del pedido"
                    )

    def action_marcar_listo(self):
        for pedido in self:
            pedido.estadoPedido = "listo"

    def action_marcar_entregado(self):
        for pedido in self:
            pedido.estadoPedido = "entregado"
