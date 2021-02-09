import random

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def random_key_generator(value):
    return value + str(random.randint(0000, 9999))


def reference_id():
    return f"nwbn-{str(random.randint(0000, 9999))}"

#
# class CSRFExemptMixin(object):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(CSRFExemptMixin, self).dispatch(request, *args, **kwargs)
