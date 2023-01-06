from django.views.decorators.http import require_GET
from django.http import JsonResponse

from .models import Redirect,HistoryKey




@require_GET
def get_url_redirect(key):
    try:
        data = {
            'key': key,
            'url': Redirect.get_redirect(key)
        }
        return JsonResponse(data, status=200)
    except:
        data = {
            "error": f'url does not exist for the key: {key}'
        }
        HistoryKey.create_key(key,HistoryKey.StateChoice.NO_EXIST)
        return JsonResponse(data, status=404)


