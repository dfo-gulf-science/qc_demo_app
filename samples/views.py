from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView, CreateView, DetailView, ListView, TemplateView
from . import models
from . import forms


class IndexTemplateView(TemplateView):
    template_name = 'samples/index.html'


class SampleListView(ListView):
    model = models.Sample


class SampleCreateView(CreateView):
    model = models.Sample
    fields = "__all__"


class SampleDetailView(DetailView):
    model = models.Sample


class ObservationCreateView(CreateView):
    model = models.Observation
    form_class = forms.ObservationForm

    def get_initial(self):
        return {"sample": self.kwargs["sample"]}


class ObservationUpdateView(UpdateView):
    model = models.Observation
    form_class = forms.ObservationForm
