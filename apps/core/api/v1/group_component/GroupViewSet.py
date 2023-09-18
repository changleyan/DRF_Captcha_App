# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core.api.v1.group_component.GroupPermissions import GroupPermissions
from apps.core.api.v1.group_component.GroupSerializar import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = (GroupPermissions,)
    parser_classes = (MultiPartParser, JSONParser)

    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
