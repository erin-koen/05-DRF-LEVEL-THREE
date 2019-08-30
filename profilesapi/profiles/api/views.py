from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from profiles.models import Profile, ProfileStatus
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly
from profiles.api.serializers import (
    ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer)


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]
    # below overwrites the get_object method on UpdateAPIView

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    # thanks to the profile serializer except for the avatar field, we can
    # update all the other fiels in a profile instance. How do we define
    # a specific permission such that those fields can only be updated by
    # their owner?


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
