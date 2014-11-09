Django Tenant Filter
====================

A simple Django app to automatically filter all model's queryset by the tenant ID.

All models are required to define a foreign key field pointing to the Tenant model and
use the Tenant Filter Manager.

Mandatory settings:
```
TENANT_FILTER = {
    'TENANT_FK_NAME': 'tenant',
    'TENANT_MODEL': 'my_app.models.Tenant',
    'TENANT_USER_MODEL': 'my_app.models.TenantUser',
    'MODEL_EXCEPTIONS': ( )
}
```

Where `my_app.models.py` is:
```
from django.contrib.auth.models import User
from django.db import models
from tenant_filter.models import TenantFilterManager


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    

class TenantUser(models.Model):
    user = models.OneToOneField(User)
    tenant = models.ForeignKey(Tenant)
    objects = TenantFilterManager()
    
    
class OtherModel(models.Model):
    tenant = models.ForeignKey(Tenant)
    objects = TenantFilterManager()

```

