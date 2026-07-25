from datetime import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().strftime('%Y-%m-%d %I:%M %p')
        print(f"\nTime: {current_time}")
        print(f"Method: {request.method}")
        print(f"Path: {request.path}\n")

        response = self.get_response(request)
        return response
