#-*-coding:utf-8-*- 

from django.shortcuts import render,render_to_response
from django.http import HttpResponse

#----------------  ajax test -----------------------

from django.http import JsonResponse

#---------------------------------------------------

import MySQLdb as mysql
import json
import requests
import solve as get_data

#create your views here.



def caozuo():

    listdata = get_data.TableToJson()
            
    name = []
    row = 0
        
    for row in range(len(listdata)):
        name.append(listdata[row][0])

    row = 0
    column = 0
    data_list=[]

        
    for row in range(len(listdata)):
        data_list.append(listdata[row][1:])

    row = 0
    chuli = []
    #chuli = [[],[],[],[],[]]
    for row in range(len(listdata)):
        chuli.append([])
        chuli[row]=list(data_list[row])

    
   
    row = 0
    dict_data = []
    #dict_data = [{},{},{},{},{}]
    for row in range(len(listdata)):
        dict_data.append({})
        dict_data[row]= dict(name = name[row],data = chuli[row])

    return dict_data

def index(request):
    return render_to_response('blog/index.html')




# ajax test:
def ajax_dict(request):
    new_data = caozuo()
    return HttpResponse(json.dumps(new_data),content_type='application/json')
