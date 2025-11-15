# bookshelf/management/commands/setup_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Creates default groups with permissions'

    def handle(self, *args, **options):
        # Get permissions for Book model
        content_type = ContentType.objects.get_for_model(Book)
        permissions = Permission.objects.filter(content_type=content_type)
        
        # Create Groups with specific permissions
        groups_permissions = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }
        
        for group_name, perm_codenames in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            
            # Clear existing permissions and add new ones
            group.permissions.clear()
            for codename in perm_codenames:
                try:
                    perm = permissions.get(codename=codename)
                    group.permissions.add(perm)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Added {codename} to {group_name}'
                        )
                    )
                except Permission.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Permission {codename} not found'
                        )
                    )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created group: {group_name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully set up all groups and permissions!')
        )