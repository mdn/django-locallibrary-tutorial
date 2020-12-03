from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
import pytz

utc=pytz.UTC

from django import forms
from .widgets import XDSoftDateTimePickerInput

class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
            help_text="Enter a date between now and 4 weeks (default 3).", widget=XDSoftDateTimePickerInput())
    test_character_field = forms.CharField()

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data.replace(tzinfo=utc) < datetime.datetime.now().replace(tzinfo=utc):
            raise ValidationError(_('Invalid date - renewal in past'))
        # Check date is in range librarian allowed to change (+4 weeks)
        if data.replace(tzinfo=utc) > datetime.datetime.now().replace(tzinfo=utc) + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
