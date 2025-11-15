# Permissions and Groups Setup Guide

## Overview

This application uses Django's built-in permission system with custom permissions to control access to different features.

## Custom Permissions Defined

### Book Permissions

- `can_view_book` - View book listings
- `can_create_book` - Create new books  
- `can_edit_book` - Edit existing books
- `can_delete_book` - Delete books

### Library Permissions

- `can_view_library` - View library listings
- `can_manage_library` - Manage library book collections

## Groups Configuration

### Viewers Group

- Permissions: `can_view_book`, `can_view_library`
- Access: Read-only access to books and libraries

### Editors Group  

- Permissions: `can_view_book`, `can_create_book`, `can_edit_book`, `can_view_library`
- Access: Can view, create, and edit books; view libraries

### Admins Group

- Permissions: All custom permissions
- Access: Full access to all features

## Setup Commands

1. Run migrations to create permission records

```bash
python manage.py migrate
