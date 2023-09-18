# -*- coding: utf-8 -*-

from rest_framework import permissions
from common.utils.utils import *


class GroupPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        usuario = request.user
        is_authenticated = usuario.is_authenticated

        if view.action in ['list', 'create', 'partial_update', 'update', 'destroy', 'retrieve']:
            return has_permission(request, view) and is_authenticated
        return False

    def has_object_permission(self, request, view, application):
        usuario = request.user
        is_authenticated = usuario.is_authenticated

        if view.action in ['partial_update', 'update', 'destroy', 'retrieve']:
            return has_permission(request, view) and is_authenticated
        return False

