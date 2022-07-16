from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from .models import Task


class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, obj):

        if isinstance(obj, Task):
            return model_to_dict(obj)

        return super().default(obj)
