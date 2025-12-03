# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medidorAgotamiento(models.Model):
    _name = 'modulo_bebida_cafe.modulo_bebida_cafe'
    _description = 'Medidor que señala el nivel de agotamiento de la pobre alma'

    alumnos = fields.Char(string="Nombre del Alumno")

    agotamiento = fields.Selection([
        ('1', '1 - Descansado'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4 - Un poco agotado'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7 - Extremadamente agotado'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10 - No puedo mas...'),
    ], string="Nivel de Cansancio", required=True)

    bebida = fields.Char(
        string='Bebida Sugerida',
        compute='_calcular_bebida',
        store=True
    )

    @api.depends('agotamiento')
    def _calcular_bebida(self):
        for record in self:
            sleep = int(record.agotamiento) if record.agotamiento else 0

            if 1 <= sleep <= 3:
                record.bebida = 'Café con leche'
            elif 4 <= sleep <= 6:
                record.bebida = 'Café solo largo'
            elif 7 <= sleep <= 9:
                record.bebida = 'Café solo larguísimo'
            elif sleep == 10:
                record.bebida = 'Inyección de adrenalina'
            else:
                record.bebida = 'ERROR'
