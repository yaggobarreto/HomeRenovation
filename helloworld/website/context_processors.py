from .views import MODULOS


def menu_lateral(request):
    return {'menu_lateral': MODULOS}
