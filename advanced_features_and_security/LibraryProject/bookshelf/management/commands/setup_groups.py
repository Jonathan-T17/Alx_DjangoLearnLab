from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book, Library

class Command(BaseCommand):
    help = 'Create default groups and assign permissions'

    def handle(self, *args, **options):
        # Get content types for permission assignment
        book_content_type = ContentType.objects.get_for_model(Book)
        library_content_type = ContentType.objects.get_for_model(Library)

        # Get permissions
        can_view_book = Permission.objects.get(codename='can_view_book', content_type=book_content_type)
        can_create_book = Permission.objects.get(codename='can_create_book', content_type=book_content_type)
        can_edit_book = Permission.objects.get(codename='can_edit_book', content_type=book_content_type)
        can_delete_book = Permission.objects.get(codename='can_delete_book', content_type=book_content_type)
        
        can_view_library = Permission.objects.get(codename='can_view_library', content_type=library_content_type)
        can_manage_library = Permission.objects.get(codename='can_manage_library', content_type=library_content_type)

        # Create Viewers group (read-only access)
        viewers, created = Group.objects.get_or_create(name='Viewers')
        viewers.permissions.set([can_view_book, can_view_library])
        if created:
            self.stdout.write(self.style.SUCCESS('Created Viewers group'))

        # Create Editors group (can create and edit books)
        editors, created = Group.objects.get_or_create(name='Editors')
        editors.permissions.set([
            can_view_book, can_create_book, can_edit_book,
            can_view_library
        ])
        if created:
            self.stdout.write(self.style.SUCCESS('Created Editors group'))

        # Create Admins group (full access)
        admins, created = Group.objects.get_or_create(name='Admins')
        admins.permissions.set([
            can_view_book, can_create_book, can_edit_book, can_delete_book,
            can_view_library, can_manage_library
        ])
        if created:
            self.stdout.write(self.style.SUCCESS('Created Admins group'))

        self.stdout.write(self.style.SUCCESS('Successfully set up all groups and permissions'))