from django import forms
from .models import PQR

class PQRForm(forms.ModelForm):

    class Meta:
        model = PQR
        fields = ['title','description','status']

        widgets = {

            'title': forms.TextInput(attrs={
                'class':'w-full bg-slate-800 border border-slate-600 rounded-lg px-4 py-2 text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition',
                'placeholder':'Ingrese el título de la solicitud'
            }),

            'description': forms.Textarea(attrs={
                'class':'w-full bg-slate-800 border border-slate-600 rounded-lg px-4 py-2 text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition',
                'rows':'5',
                'placeholder':'Describe la solicitud...'
            }),

            'status': forms.Select(attrs={
                'class':'w-full bg-slate-800 border border-slate-600 rounded-lg px-4 py-2 text-gray-200 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition'
            })

        }