from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from genifytask.searchmodel import searchbycode
import json


@require_http_methods(["GET"])
def home(request):
    
    return HttpResponse("welcome to my api")
         
@require_http_methods(["POST"])
def getReco(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        content = body['code']
        items   = searchbycode(content)
        if(items==''):
             return HttpResponseNotFound("code not found")
        else:
            reco={}
            reco['recommendations']=items
            json_data = json.dumps(reco)
            print(json_data)
            return HttpResponse( json_data)
    except Exception:
        return HttpResponseBadRequest("bad request")
    
