from django.db.models import Sum
from django.shortcuts import redirect, render
from .models import ReformaItem


def listar_reforma(request):
    reformas = ReformaItem.objects.all()
    concluidos = reformas.filter(status=ReformaItem.Status.CONCLUIDO).count()
    total_estimado = reformas.aggregate(Sum('custo_estimado'))['custo_estimado__sum'] or 0

    return render(request, 'reforma/listar.html', {
        'reformas': reformas,
        'concluidos': concluidos,
        'total_estimado': total_estimado,
    })


def criar_reforma(request):
    if request.method == 'POST':
        ReformaItem.objects.create(
            nome=request.POST['nome'],
            categoria=request.POST['categoria'],
            custo_estimado=request.POST['custo_estimado'],
            custo_real=request.POST.get('custo_real') or None,
            status=request.POST['status'],
            prioridade=request.POST['prioridade'],
            data_estimavel=request.POST['data_estimavel'],
        )
        return redirect('listar_reforma')
    return render(request, 'reforma/criar.html')