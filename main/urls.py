from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet, TeamMembershipViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('persons/<int:pk>/add_to_team/', TeamMembershipViewSet.as_view({'post': 'add_member'}), name='add-member'),
    path('persons/<int:pk>/remove_from_team/', TeamMembershipViewSet.as_view({'post': 'remove_member'}), name='remove-member'),
]
