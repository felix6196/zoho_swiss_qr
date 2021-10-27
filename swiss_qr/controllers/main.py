from odoo import http
from odoo.http import request
import tempfile
from qrbill import QRBill
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


class SwissQR(http.Controller):

    @http.route('/swizz_qr', auth='public', website=True)
    def index(self, **kw):
        my_bill = QRBill(
            account='CH4431999123000889012',
            creditor={
                'name': 'Robert Schneider AG',
                'street': 'Rue du Lac',
                'house_num': '1268',
                'pcode': '2501',
                'city': 'Biel',
                'country': 'CH',
            },
            amount='1949.7',
            currency='CHF',
            due_date='2019-10-31',
            debtor={
                'name': 'Pia-Maria Rutschmann-Schnyder',
                'street': 'Grosse Marktgasse',
                'house_num': '28',
                'pcode': '9400',
                'city': 'Rorschach',
                'country': 'CH',
            },
            ref_number='210000000003139471430009017'
        )
        with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
            my_bill.as_svg(temp)
            temp.seek(0)
            drawing = svg2rlg(temp)
        w_file = open("./file.pdf", "r+b") 
        renderPDF.drawToFile(drawing, w_file)
        r_fiel =  open('./file.pdf', "rb+").read()
        headers = [('Content-Type', 'application/pdf')]
        return request.make_response(r_fiel, headers=headers)


