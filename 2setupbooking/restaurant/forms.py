from django.forms import ModelForm

from .models import Menu, Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"