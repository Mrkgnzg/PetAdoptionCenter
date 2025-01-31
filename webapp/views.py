from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animal, AdoptionRequest, Shelter
from .forms import AnimalForm, AdoptionRequestForm, ShelterForm
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'app/home.html' 

class AdminPage(TemplateView):
    template_name = 'app/admin-panel.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animal_count'] = Animal.objects.count()
        context['adoption_request_count'] = AdoptionRequest.objects.count()
        context['shelter_count'] = Shelter.objects.count()
        context['animals'] = Animal.objects.all()
        context['adoption_requests'] = AdoptionRequest.objects.all()
        context['shelters'] = Shelter.objects.all()
        return context

class AnimalListView(ListView):
    model = Animal
    template_name = 'app/animal_list.html'
    context_object_name = 'animals'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Animal.objects.filter(Q(name__icontains=query) | Q(breed__icontains=query))
        return Animal.objects.all()

class AnimalShowcaseView(ListView):
    model = Animal
    template_name = 'app/animal_showcase.html'
    context_object_name = 'animals'
    
    def get_queryset(self):
        return Animal.objects.filter(available_for_adoption=True)

class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'app/animal_form.html'
    success_url = reverse_lazy('animal_list')

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'app/animal_detail.html'
    context_object_name = 'animal'

class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'app/animal_form.html'
    success_url = reverse_lazy('animal_list')

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'app/animal_confirm_delete.html'
    success_url = reverse_lazy('animal_list')


class AdoptionRequestListView(ListView):
    model = AdoptionRequest
    template_name = 'app/adoption_request_list.html'
    context_object_name = 'adoption_requests'
        

class AdoptionRequestCreateView(CreateView):
    model = AdoptionRequest
    form_class = AdoptionRequestForm
    template_name = 'app/adoption_request_form.html'
    success_url = reverse_lazy('animal_showcase')

class AdoptionRequestDetailView(DetailView):
    model = AdoptionRequest
    template_name = 'app/adoption_request_detail.html'
    context_object_name = 'adoption_request'

class AdoptionRequestUpdateView(UpdateView):
    model = AdoptionRequest
    form_class = AdoptionRequestForm
    template_name = 'app/adoption_update_form.html'
    success_url = reverse_lazy('adoption_request_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add Bootstrap classes dynamically
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form

class AdoptionRequestDeleteView(DeleteView):
    model = AdoptionRequest
    template_name = 'app/adoption_request_confirm_delete.html'
    success_url = reverse_lazy('adoption_request_list')


class ShelterListView(ListView):
    model = Shelter
    template_name = 'app/shelter_list.html'
    context_object_name = 'shelters'

class ShelterDetailView(DetailView):
    model = Shelter
    template_name = 'app/shelter_detail.html'
    context_object_name = 'shelter'

class ShelterCreateView(CreateView):
    model = Shelter
    form_class = ShelterForm
    template_name = 'app/shelter_form.html'
    success_url = reverse_lazy('shelter-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form

class ShelterUpdateView(UpdateView):
    model = Shelter
    form_class = ShelterForm
    template_name = 'app/shelter_form_update.html'
    success_url = reverse_lazy('shelter-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form

class ShelterDeleteView(DeleteView):
    model = Shelter
    template_name = 'app/shelter_confirm_delete.html'
    success_url = reverse_lazy('shelter-list')
