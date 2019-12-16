from django.core.management.base import BaseCommand, CommandError
from rest_shoebox.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Populate data for shoe type and color'

    def handle(self, *args, **options):
        ShoeType.objects.create(style="sneaker")
        ShoeType.objects.create(style="boot")
        ShoeType.objects.create(style="sandal")
        ShoeType.objects.create(style="dress")
        ShoeType.objects.create(style="other")

        ShoeColor.objects.create(color_name="Red")
        ShoeColor.objects.create(color_name="Orange")
        ShoeColor.objects.create(color_name="Yellow")
        ShoeColor.objects.create(color_name="Green")
        ShoeColor.objects.create(color_name="Blue")
        ShoeColor.objects.create(color_name="Indigo")
        ShoeColor.objects.create(color_name="Violet")
        ShoeColor.objects.create(color_name="White")
        ShoeColor.objects.create(color_name="Black")
