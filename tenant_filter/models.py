# coding: utf-8
from django.db import models
from middleware import get_current_user
from django.conf import settings


TENANT_FILTER = getattr(settings, 'TENANT_FILTER')


class TenantFilterManager(models.Manager):
    def get_queryset(self):
        """
        Filter the default queryset by the tenant ID found in the local thread. It requires
        'middleware.GlobalRequestMiddleware' to be activated in settings.py
        """
        qs = super(TenantFilterManager, self).get_queryset()
        user = get_current_user()
        if user and user.is_authenticated():
            tenant_user_obj = getattr(user, TENANT_FILTER['TENANT_USER_MODEL'].split('.')[-1].lower())
            tenant_obj = getattr(tenant_user_obj, TENANT_FILTER['TENANT_MODEL'].split('.')[-1].lower())
            filter_dict = {TENANT_FILTER['TENANT_FK_NAME']: tenant_obj.pk}
            qs = qs.filter(**filter_dict)
        return qs