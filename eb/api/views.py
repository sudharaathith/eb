from urllib import response
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from base.models import *
mt = {613:Mt613,722:Mt722, 723:Mt723}
st = {613:St613,722:St722, 723:St723}

@api_view(['GET'])
def perEvent(request, met, se):
    mod =reversed( mt[met].objects.filter(session=se).order_by('-date'))
    ser = st[met](mod, many = True)
    return Response(ser.data)

@api_view(['POST'])
def update(request, met):
    ser = st[met](data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['DELETE'])
def delete(request, met, id):
    mod = mt[met].objects.get(id=id)
    ser = st[met](mod).data
    mod.delete()
    return Response(ser)

@api_view(['GET', 'POST', 'DELETE'])
def sess(request):
    if (request.method == 'GET'):
        ses = sesion.objects.all()
        sts = Stsession(ses,many=True)
        return Response(sts.data)
    
    elif (request.method == 'POST'):
        ses = Stsession(data=request.data)
        if ses.is_valid():
            ses.save()
        return Response(ses.data)
        
    elif (request.method == 'DELETE'):
        ses = sesion.objects.all().order_by('-date')
        ob = ses[0]
        dob = Stsession(ob).data
        ob.delete()
        return Response(dob)