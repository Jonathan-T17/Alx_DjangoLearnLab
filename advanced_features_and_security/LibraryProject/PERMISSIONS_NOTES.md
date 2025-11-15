# Permissions & Groups Setup

## Custom Permissions Added to Book Model

- can_view
- can_create
- can_edit
- can_delete

## Groups Created

### Viewers

- can_view

### Editors

- can_view
- can_create
- can_edit

### Admins

- can_view
- can_create
- can_edit
- can_delete

## Usage in Views

Permissions are enforced using `@permission_required`:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)

