from re import T
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Exercise, TrainingRecord

# Create your views here.
class ExerciseList(ListView):
    model = Exercise
    context_object_name = 'exercises'

#search function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-column') or ""

        if search_input:
            context['exercises'] = context['exercises'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context

class ExerciseDetail(DetailView):
    model = Exercise
    context_object_name = 'exercise'

    def get_context_data(self, **kwargs):
        context = super(ExerciseDetail, self).get_context_data(**kwargs)
        context['records'] = TrainingRecord.objects.all()

        search_input = self.request.GET.get('search-column') or ""

        if search_input:
            context['records'] = context['records'].filter(date__contains=search_input)

        context['search_input'] = search_input

        return context
        
class ExerciseCreate(CreateView):
    model = Exercise
    fields = '__all__'
    success_url = reverse_lazy('exercises')

class ExerciseUpdate(UpdateView):
    model = Exercise
    fields = '__all__'
    success_url = reverse_lazy('exercises')

class ExerciseDelete(DeleteView):
    model = Exercise
    context_object_name = 'exercise'
    success_url = reverse_lazy('exercises')

class TrainingRecordDetail(DetailView):
    model = TrainingRecord
    context_object_name = 'record'

class TrainingRecordCreate(CreateView):
    model = TrainingRecord
    fields = '__all__'

    def get_success_url(self):
        exercise_id=self.kwargs['pk']

        return reverse_lazy('exercise', kwargs={'pk':exercise_id})

class TrainingRecordDelete(DeleteView):
    model = TrainingRecord
    context_object_name = 'record'

    success_url = reverse_lazy('record-delete-success')

class TrainingRecordUpdate(UpdateView):
    model = TrainingRecord
    fields = '__all__'
    success_url = reverse_lazy('record')

    def get_success_url(self):
        record_id=self.kwargs['pk']

        return reverse_lazy('record', kwargs={'pk':record_id})

class TrainingRecordDeleteSuccess(ListView):
    model = Exercise
    template_name = 'base/trainingrecorddeletesuccess_list.html'
    context_object_name = 'record-delete-success'
