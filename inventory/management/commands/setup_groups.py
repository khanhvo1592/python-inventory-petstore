from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from inventory.models import Product

class Command(BaseCommand):
    help = 'Sets up initial user groups and permissions'

    def handle(self, *args, **kwargs):
        # Create or get groups
        manager_group, created = Group.objects.get_or_create(name='Manager')
        regular_user_group, created = Group.objects.get_or_create(name='Regular User')

        # Get content type for Product model
        content_type = ContentType.objects.get_for_model(Product)

        # Get permissions
        view_permission = Permission.objects.get(
            codename='can_view_product',
            content_type=content_type
        )
        edit_permission = Permission.objects.get(
            codename='can_edit_product',
            content_type=content_type
        )

        # Clear existing permissions
        manager_group.permissions.clear()
        regular_user_group.permissions.clear()

        # Assign permissions to groups
        manager_group.permissions.add(view_permission, edit_permission)
        regular_user_group.permissions.add(view_permission)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions')) 