from django.shortcuts import render

# Create your views here.

MODULOS = [
    {
        'codigo': 'M-02',
        'nome': 'Reforma',
        'descricao': 'Itens, custos e status da reforma da casa.',
        'status': 'em_andamento',
        'status_label': 'Em andamento',
        'icon': 'hammer',
        'url': '/reforma/',
    },
    {
        'codigo': 'M-03',
        'nome': 'Metas financeiras',
        'descricao': 'Organização do dinheiro pro casamento e pra reforma.',
        'status': 'planejamento',
        'status_label': 'Planejamento',
        'icon': 'piggy-bank',
        'url': None,
    },
    {
        'codigo': 'M-04',
        'nome': 'Tarefas & prazos',
        'descricao': 'O que precisa ser feito e até quando.',
        'status': 'planejamento',
        'status_label': 'Planejamento',
        'icon': 'calendar-check-2',
        'url': None,
    },
    {
        'codigo': 'M-05',
        'nome': 'Relatórios',
        'descricao': 'Resumo financeiro e progresso, tudo num lugar.',
        'status': 'planejamento',
        'status_label': 'Planejamento',
        'icon': 'bar-chart-3',
        'url': None,
    },
]


def home(request):
    em_andamento = sum(1 for m in MODULOS if m['status'] == 'em_andamento')
    planejamento = sum(1 for m in MODULOS if m['status'] == 'planejamento')
    return render(request, 'website/home.html', {
        'modulos': MODULOS,
        'total_modulos': len(MODULOS),
        'em_andamento': em_andamento,
        'planejamento': planejamento,
    })
