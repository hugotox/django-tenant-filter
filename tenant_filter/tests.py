# coding: utf-8
from django.test import TestCase
from django.apps import apps
from tenant_filter.models import TenantFilterManager
from django.conf import settings


class TenantModelManagerTest(TestCase):
    def test_model_uses_manager(self):
        """
        Check that all models are using the default manager (with some exceptions)
        """
        tenant_model = settings.TENANT_FILTER['TENANT_MODEL'].split('.')[-1]
        implement_manager_exceptions = (tenant_model, 'LogEntry', 'Permission', 'Group', 'User', 'ContentTypeManager', 'ContentType',
                                        'Session', 'Manager', 'Source', 'Thumbnail', 'ThumbnailDimensions')\
                                        + settings.TENANT_FILTER['MODEL_EXCEPTIONS']
        models = apps.get_models()
        for model in models:
            if model.__name__ not in implement_manager_exceptions:
                if not isinstance(model.objects, TenantFilterManager):
                    print "Model %s does not implement TenantFilterManager" % model
                self.assertIsInstance(model.objects, TenantFilterManager)
