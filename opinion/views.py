from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import OpinionForm
from .models import Opinion
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# def opinion(request):
#     if request.method == 'POST':
#         print (request.POST['nombre'])
#         if request.POST['nombre']=='':
#             return render(request,'opinion/opinion.html', {'error': True})
#         return HttpResponseRedirect('gracias')
#     return render(request,'opinion/opinion.html', {'error': False})

class OpinionView(CreateView):
    model = Opinion
    form_class = OpinionForm
    template_name = 'opinion/opinion.html'
    success_url = "/gracias"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)



    # def get(self, request):
    #     print ('metodo get')
    #     form = OpinionForm()
    #     return render(request, 'opinion/opinion.html', {
    #         'form': form
    #     })

    # def post(self, request):
    #     form = OpinionForm(request.POST)
    #     if form.is_valid():
    #         print ('form.cleaned_data', form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect('gracias')


# def opinion(request):
#     if request.method == 'POST':
#         form = OpinionForm(request.POST)
#         if form.is_valid():
#             print ('form.cleaned_data', form.cleaned_data)
#             # opinion = Opinion(
#             #     nombre = form.cleaned_data['nombre'],
#             #     opinion = form.cleaned_data['opinion'],
#             #     puntaje = form.cleaned_data['puntaje'],
#             # )
#             form.save()
#             return HttpResponseRedirect('gracias')
#     else:
#         form = OpinionForm()
#     return render(request, 'opinion/opinion.html', {
#         'form': form
#     })

class Gracias(TemplateView):
    template_name = 'opinion/gracias.html'

    # def get(self, request):
    #     return render(request, 'opinion/gracias.html')


# def gracias(request):
#     return render(request, 'opinion/gracias.html')

class OpinionListView(ListView):
    template_name = 'opinion/lista_opiniones.html'
    model = Opinion
    context_object_name = 'opiniones'

    # def get_queryset(self):
    #     consulta = super().get_queryset()
    #     return consulta.filter(puntaje__lte=4)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print ('context', context)
    #     opiniones = Opinion.objects.all()
    #     context['opiniones'] = opiniones
    #     return context

class OpinionDetalleView(DetailView):
    template_name = 'opinion/opinion_detalle.html'
    model = Opinion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        opinion_cargada = self.object
        request = self.request
        opinion_id = request.session.get('opinion_fav')
        print ('opinion_id', type(opinion_id))
        print ('opinion_cargada.id', type(opinion_cargada.id))
        context['es_favorito'] = opinion_id == str(opinion_cargada.id)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print ('kwargs', kwargs)
    #     opinion_id = kwargs['id']
    #     opinion = Opinion.objects.get(id=opinion_id)
    #     context['opinion'] = opinion
    #     return context

class AgregarFavoritoView(View):
    def post(self, request):
        opinion_id = request.POST['opinion_id']
        request.session["opinion_fav"] = opinion_id
        return HttpResponseRedirect("/opinion/" + opinion_id)
