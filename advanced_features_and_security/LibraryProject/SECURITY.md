# Security Configurations & Testing Notes

## Settings (LibraryProject/settings.py)

- DEBUG = False in production
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- X_FRAME_OPTIONS = 'DENY'
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SECURE = True
- SECURE_HSTS_SECONDS set for HTTPS environments

## CSRF Protection

- All POST forms include `{% csrf_token %}` (see templates in bookshelf/templates/...)

## SQL Injection Prevention

- Use Django ORM methods (e.g., `.filter()`, `.get()`, `.exclude()`) and ModelForms
- Example: `Book.objects.filter(title__icontains=q)` instead of raw SQL string formatting

## Content Security Policy

- Implemented via `LibraryProject/middleware.py` which sets `Content-Security-Policy` header
- Adjust `script-src`, `style-src`, etc. if using CDNs

## Testing Approach

1. CSRF: try submitting a POST form without CSRF token — should be blocked.
2. XSS: try to submit `<script>alert(1)</script>` as a title and confirm template auto-escapes output.
3. SQL injection: try search query with SQL fragments — ORM should treat it as literal string.
4. Cookies: check cookies are flagged Secure and HttpOnly when using HTTPS.

## Notes

- Ensure HTTPS is used in production to enforce cookie security and HSTS.
- Review CSP strictly when adding external JS/CSS sources.
