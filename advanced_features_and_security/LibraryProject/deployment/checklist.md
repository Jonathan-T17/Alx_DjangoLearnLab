# HTTPS Production Deployment Checklist

## Pre-Deployment Checks

- [ ] Set `DEBUG = False` in production
- [ ] Configure `ALLOWED_HOSTS` with production domain
- [ ] Set `DJANGO_SECRET_KEY` as environment variable
- [ ] Verify SSL certificate is installed and valid
- [ ] Test HTTPS redirect locally

## Web Server Configuration (Nginx)

```nginx
# /etc/nginx/sites-available/your-domain
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/private.key;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
