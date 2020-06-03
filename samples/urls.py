from django.urls import path
from . import views

urlpatterns = [
    # for samples
    path("", views.IndexTemplateView.as_view(), name="index"),
    path("samples/", views.SampleListView.as_view(), name="sample-list"),
    path("samples/new/", views.SampleCreateView.as_view(), name="sample-new"),
    path("samples/<int:pk>/detail/", views.SampleDetailView.as_view(), name="sample-detail"),

    # for obs
    path("samples/<int:sample>/new-observation/", views.ObservationCreateView.as_view(), name="obs-new"),
    path("observation/<int:pk>/edit/", views.ObservationUpdateView.as_view(), name="obs-edit"),
]
