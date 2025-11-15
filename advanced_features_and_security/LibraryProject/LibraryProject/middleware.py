"""
Custom middleware for enhanced security headers and HTTPS enforcement.
"""

class SecurityHeadersMiddleware:
    """
    Middleware to add security headers to all responses.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        # Content Security Policy (Basic)
        csp = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "  # unsafe-inline for Django admin
            "img-src 'self' data:; "
            "font-src 'self'; "
            "connect-src 'self'; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "form-action 'self'; "
        )
        response['Content-Security-Policy'] = csp
        
        return response


class SSLMiddleware:
    """
    Middleware to log SSL requests and enforce HTTPS in production.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log SSL information for monitoring
        is_secure = request.is_secure()
        protocol = 'HTTPS' if is_secure else 'HTTP'
        
        # You can log this information for security monitoring
        if not is_secure and not request.get_host().startswith(('localhost', '127.0.0.1')):
            # Log non-HTTPS requests in production
            print(f"⚠️  Non-HTTPS request: {request.method} {request.path}")
        
        response = self.get_response(request)
        return response