import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self,get_response):
        self.get_response= get_response
    
    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        duration = time.perf_counter() - start

        # Add custom header (can be seen in browser DevTools > Network > Headers)
        response['X-Response-Time'] = f'{duration:.3f}s'

        # Log to console
        logger.info(f"{request.method} {request.get_full_path()} -> {response.status_code} completed in {duration:.3f}s")

        return response

class ProductActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/products/'):
            start = time.perf_counter()
            response = self.get_response(request)
            duration = time.perf_counter() - start
            user = getattr(request,'user',None)
            username = user.username if user and user.is_authenticated else 'Anonymous'
            response['X-Product-Activity-Time-2'] = f'{duration:.3f}s'
            logger.info(f"{request.method} {request.get_full_path()} -> {response.status_code} by {username} in {duration:.3f}s")
            return response
        
        return self.get_response(request)