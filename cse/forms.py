from django import forms
import pytz
class LocationForm(forms.Form):
    timezone = forms.ChoiceField(choices=[(tz, tz) for tz in pytz.all_timezones])