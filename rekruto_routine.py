from copy import deepcopy

from flask_restful import Resource
from flask import request, Response

from common import html

class Rekruto(Resource):

    def get(self):
        req = dict(deepcopy(request.args))

        response: Response = None
        try:
            response: Response = Response(html(f"Hello {req['name']}!<br>{req['message']}"))
        except KeyError:
            pass
        return response
