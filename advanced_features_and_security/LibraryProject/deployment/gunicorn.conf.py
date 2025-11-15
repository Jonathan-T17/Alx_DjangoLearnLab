# Gunicorn Configuration for HTTPS Django Application

# Server socket
bind = "127.0.0.1:8000"

# Worker processes
workers = 3
worker_class = "sync"
worker_connections = 1000

# Security
max_requests = 1000
max_requests_jitter = 100

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"

# Process naming
proc_name = "django_library_app"

# SSL Note: SSL termination should be handled by Nginx/Apache
# Gunicorn runs behind reverse proxy with HTTPS