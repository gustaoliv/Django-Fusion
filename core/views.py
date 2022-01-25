from django.views.generic import FormView
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
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

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)