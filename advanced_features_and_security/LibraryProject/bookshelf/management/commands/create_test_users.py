from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create test users for permission testing'
    
    def handle(self, *args, **options):
        # Get the custom user model
        User = get_user_model()
        
        users_data = [
            ('viewer_user', 'Viewers'),
            ('editor_user', 'Editors'),
            ('admin_user', 'Admins'),
        ]
        
        for username, group_name in users_data:
            user, created = User.objects.get_or_create(username=username)
            user.set_password('password123')
            user.is_active = True  # Ensure user is active
            user.save()
            
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            
            if created:
                self.stdout.write(self.style.SUCCESS(f"✓ Created {username} in {group_name} group"))
            else:
                self.stdout.write(self.style.WARNING(f"✓ Updated {username} in {group_name} group"))