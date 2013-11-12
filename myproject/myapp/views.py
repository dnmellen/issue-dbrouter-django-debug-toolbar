from .models import Foo
from django.views.generic import TemplateView
# Create your views here.


class Index(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        obj = Foo.objects.create(name='Test issue')
        context['name'] = obj.name
        obj.delete()
        return context
    template_name = "index.html"
