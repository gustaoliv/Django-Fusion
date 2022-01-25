from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recurso

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        qtfeatures = Recurso.objects.count()
        qtd = qtfeatures // 2
 
        if (qtfeatures % 2) == 1:
            qtd = qtd + 1



        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos_esq'] = Recurso.objects.order_by('?').all()[:qtd]
        context['recursos_dir'] = Recurso.objects.order_by('?').all()[qtd:]
        return context