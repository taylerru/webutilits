from core.models import Hint, Download


def get_client_ip(request):
    # Получаем ip-адрес пользователя/отправителя
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def incCountHit(request, obj):
    # Инкрементирую просмотры объекта
    obj.hints.get_or_create(ip=get_client_ip(request))


def incCountDownload(request, obj):
    # Инкрементирую загрузки объекта
    obj.download.get_or_create(ip=get_client_ip(request))