from django.urls import path
from .views import HomeView, trips_list, TripCreateView, TripDetailView, NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, TripDeleteView, TripUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trips_list, name='trips-list'),
    path('dashboard/trips/create/', TripCreateView.as_view(), name='trip-create'),
    path('dashboard/trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('dashboard/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('dashboard/notes/', NoteListView.as_view(), name='note-list'),
    path('dashboard/note/create/', NoteCreateView.as_view(), name='note-create'),
    path('dashboard/note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('dashboard/note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('dashboard/trips/<int:pk>/update/', TripUpdateView.as_view(), name='trip-update'),
    path('dashboard/trips/<int:pk>/delete/', TripDeleteView.as_view(), name='trip-delete'),

]

# delete doesn't need a template
# update uses the same template as create