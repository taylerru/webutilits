import time
import hashlib

from django.utils.html import escape
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from shorturl.models import Url, Protocol
from shorturl.forms import ShortenerUrlForm
from core.utilits import get_client_ip, incCountHit


def index(request):
    context = dict()
    form = ShortenerUrlForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        protocol, url = form.cleaned_data['url']

        # Хэширую URL с солью в виде нынешнего времени, для последующего
        # формирования короткой ссылки.
        short_url = hashlib.md5(
            "".join([url, str(time.time())]).encode('utf8')
        ).hexdigest()[:10]

        protocol, c = Protocol.objects.get_or_create(protocol=protocol)

        url, c = Url.objects.get_or_create(
            url=escape(url),
            url_short=short_url,
            protocol=protocol,
            defaults={'creator_ip': get_client_ip(request)}
        )

        context['url'] = request.build_absolute_uri(url.get_absolute_url())
    context['form'] = form
    return render(request, 'shorturl.html', context=context)


def redirect(request, hash):
    url = get_object_or_404(Url, url_short=hash)
    incCountHit(request, url)
    return HttpResponse(
        '<script>window.location.href = "%s://%s";</script>' % (url.protocol.protocol, url.url)
    )
