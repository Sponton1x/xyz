from axes.middleware import AxesMiddleware
from django.http import HttpResponse
from datetime import datetime, timedelta


class BlockAdminMiddleware(AxesMiddleware):
    def process_request(self, request):
        response = super().process_request(request)

        if response and response.status_code == 403 and response['WWW-Authenticate'] == 'Axes':
            if request.path.startswith('/admin/'):
                expiration_time = datetime.now() + timedelta(minutes=10)
                response = HttpResponse("Your account has been blocked. Let's try for 10 minutes.")
                response.set_cookie('block_admin', 'true', expires=expiration_time)

        return response
