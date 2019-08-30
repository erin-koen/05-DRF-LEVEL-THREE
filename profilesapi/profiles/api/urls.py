from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views import (
    ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView)

# ***The below is an implementation sans routers***
# profile_list = ProfileViewSet.as_view({"get": "list"})
# profile_detail = ProfileViewSet.as_view({"get": "retrieve"})
# # where does 'retrieve' come from ? (check readonlymodelvivewset in viewsets)

# urlpatterns = [
#     path("profiles/", profile_list, name="profile-list"),
#     path("profiles/<int:pk>", profile_detail, name="profile-detail")
# ]

router = DefaultRouter()
# raw strings (prefixed by r) treat backslashes as literal characters
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]
