from rest_framework import viewsets
from .models import PQR
from .serializers import PQRSerializer

class PQRViewSet(viewsets.ModelViewSet):

    queryset = PQR.objects.all()
    serializer_class = PQRSerializer















""" from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import PQR
from .forms import PQRForm


def pqr_list(request):
    pqr = PQR.objects.all()
    return render(request,'pqr/pqr_list.html',{'pqr':pqr})


def pqr_create(request):

    form = PQRForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pqr_list')
    return render(request,'pqr/pqr_create.html',{'form':form})


def pqr_detail(request,id): 
    pqr = get_object_or_404(PQR,id=id)
    return render(request,'pqr/pqr_detail.html',{'pqr':pqr})


def pqr_delete(request,id):
    pqr = get_object_or_404(PQR,id=id)
    pqr.delete()
    return redirect('pqr_list') """


