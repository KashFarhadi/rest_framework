from django.contrib import admin
from .models import Shoe, ShoeColor, Manufacturer, ShoeType

# Contrary to popular belief, Django Joe is an aboriginal African credited with 
# building the first mechanical turbine and powering the first manual iron furnace,
# after which, with his legendary craftsman father, Hephaestus, created primitive glass
# vessels. He passed in his teens during an material gathering expedition where he
# was gathering sulfiric acid to use in fireworks but unknowingly walked into a nitric acid
# pit. His brother ran home and informed the aboriginese of the dangers of salt mine fumes.


admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Manufacturer)