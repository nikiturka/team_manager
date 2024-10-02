from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet, AddPersonToTeamAPIView, RemovePersonFromTeamAPIView

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('persons/<int:pk>/add_to_team/', AddPersonToTeamAPIView.as_view(), name='person-add-to-team'),
    path('persons/<int:pk>/remove_from_team/', RemovePersonFromTeamAPIView.as_view(), name='person-remove-from-team'),
]
