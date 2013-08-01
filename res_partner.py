# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv

class res_partner(osv.osv):
    _name= "res.partner"
    _inherit = "res.partner"

    _columns = {
        'nombre': fields.char('Nombre', size=20),
        'apellidos': fields.char('Apellidos', size=20),
        'empresa': fields.boolean('Entidad Jurídica', help='Marque esta casilla si el contacto es una entidad jurídica o empresa.'),
        'dni' : fields.char('DNI', size=9, help='Documento Nacional de Identidad'),

        'movil': fields.related('address', 'mobile', type='char', string='Móvil'),
        'cpostal': fields.related('address', 'zip', type='char', string='Código Postal'),
    }

    def onchange_checkdni(self, cr, uid, ids, dni):
        dniok = False
        try:
            if len(dni)==9:                
                try: numero = int(dni[:-1])
                except: return {'warning':{'title':'Atención','message':'El DNI no es correcto.'}}
                NIF='TRWAGMYFPDXBNJZSQVHLCKE'
                letra_correcta = NIF[numero%23]
                letra = dni[-1].upper()
                if letra == letra_correcta: return {'value':{'vat':'ES'+dni}}
                else: return {'warning':{'title':'Atención','message':'El DNI no es correcto.'}}
            else:
                #TODO: Revisar
                return {'warning':{'title':'Atención','message':'El DNI no es correcto.'}}

        except: return True

    def onchange_nomyapel(self, cr, uid, ids, nom,apel):
        v = {}
        # Si se modifican nombre o apellidos se asignan al campo name original de OpenERP
        if nom and nom!='':
            nom = nom.encode('utf-8','replace')
            if apel and apel!='':
                apel = apel.encode('utf-8','replace')
                v = {'name':str(nom) + ' ' + str(apel), }
            else:
                v = {'name':nom, } 
        return {'value': v}

    def onchange_empresa(self, cr, uid, ids, valor):
        v = {}
        # Si se marca la casilla 'empresa' borra los datos no necesarios
        if valor:
            v = {'nombre':'','apellidos':'', 'dni':''}
        return {'value': v}

res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
