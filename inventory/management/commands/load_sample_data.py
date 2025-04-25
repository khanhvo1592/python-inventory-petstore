from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load sample data for the inventory application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample data...')
        
        try:
            # Load the fixture data
            call_command('loaddata', 'sample_data.json')
            self.stdout.write(self.style.SUCCESS('Successfully loaded sample data'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading sample data: {str(e)}')) 