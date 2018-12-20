import json
import logging
import traceback

from snippets.utils import attr
from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

debug = attr(settings, 'DEBUG')


class LogMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.get_response = get_response

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        meta = request.META
        ip = meta.get('HTTP_X_FORWARDED_FOR') or meta.get('REMOTE_ADDR') or "no-ip"
        path = request.get_full_path()
        content = ""
        content_type = response['Content-Type']
        if content_type in ['application/json', "text/xml"] and response.content:
            content = "response:%s" % response.content.decode('raw_unicode_escape')
        data = ""

        if request.method in ["POST", "PUT",'PATCH']:
            if request.POST:
                data = " form:%s" % json.dumps(request.POST)
            else:
                pass#data = f" body:{request.data}"

        name = attr(request, "user.username")
        user_info = f"admin-user-name:{name}" if name else ""
        message = f'111{ip} "{request.method} {path}"{data} {response.status_code} {content} {user_info}'

        print(message)

        return response

    def process_exception(self, request, exception):
        meta = request.META
        ip = meta.get('HTTP_X_FORWARDED_FOR') or meta.get('REMOTE_ADDR') or "no-ip"
        path = request.get_full_path()
        trace = traceback.format_exc()
        logger.error(f'{ip} {request.method} {path},process_exception: {json.dumps({"trace": trace})}')
        if debug:
            logger.error(trace)

        if request.GET.get("debug") == '100':
            return HttpResponse(trace, content_type="application/json")
