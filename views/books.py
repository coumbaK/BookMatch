#books list endpoint
#booksdetailendpoint
from libgen_api import LibgenSearch
# from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import Response, request
from flask_restful import Resource

import json

def get_path():
    return request.host_url + 'api/results'

class BookListEndpoint(Resource):
    

    def get (self) : 
        # args = request.args
        s = LibgenSearch()
        # text = args.get('text')
        results = s.search_title("pride")
        
        
        return Response(json.dumps(results), mimetype="application/json", status=200)




def initialize_routes(api):
    api.add_resource(
        BookListEndpoint, 
        '/api/results'
    )

