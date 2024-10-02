from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet, TeamMembershipViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('teams/<int:pk>/add/', TeamMembershipViewSet.as_view({'post': 'add_member'}), name='add-member'),
    path('teams/<int:pk>/remove/', TeamMembershipViewSet.as_view({'post': 'remove_member'}), name='remove-member'),
]
