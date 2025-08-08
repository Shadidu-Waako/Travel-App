from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, DeleteView, UpdateView
from .models import Trip, Note
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips
    }
    return render(request, 'trip/trips_list.html', context)

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trips-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    # Template named -> model_from.html --> trip/trip_form.html

    def form_valid(self, form):
        # owner = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class TripDetailView(DetailView):
    model = Trip

    #data store on trip to also have the notes data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context
    
class NoteDetailView(DetailView):
    model = Note

class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset

class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note-list')

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
    
class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note-list')

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    # No template needed - we send a post request to this url

class TripUpdateView(UpdateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    success_url = reverse_lazy('trips-list')

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trips-list')
    # No template needed - we send a post request to this url