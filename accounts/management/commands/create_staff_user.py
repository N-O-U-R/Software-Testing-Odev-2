from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates an initial staff user.'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(email='admin@admin.com').exists():
            User.objects.create_user(username='admin@admin.com', email='admin@admin.com', password='qpalzm', first_name='Admin', is_staff=True)
            self.stdout.write(self.style.SUCCESS('Successfully created a new staff user: Admin'))
