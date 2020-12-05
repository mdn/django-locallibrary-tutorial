from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
import pytz

utc=pytz.UTC

from django import forms
from .widgets import XDSoftDateTimePickerInput
from .models import T_Calendar, Author

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


class CreateWorkPackage_WithProposedWeekTarget_Form(forms.Form):
    """Form for a librarian to renew books."""
#    week_target_workpackagecreation = forms.CharField()
    week_target_workpackagecreation = forms.ModelChoiceField(queryset=Author.objects.all(), label="Author", widget=forms.Select(), initial=0)
    datetime_start = forms.ModelChoiceField(queryset=T_Calendar.objects.all().order_by('datetime_start'), label="T_Calendar", widget=forms.Select(), initial=0, empty_label='', required=False)
    workpackage_title_workpackagecreation = forms.CharField()
    associated_email_subject_workpackagecreation = forms.CharField()
    associated_email_received_datetime_workpackagecreation = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())
    associated_email_received_account_workpackagecreation = forms.CharField()   #ToDo: Dropdown-Liste mit meinen Email-Adressen mit MCH-Adresse als Default
    filepath_for_readiness_enhancement_workpackagecreation = forms.CharField()
    hyperlink_for_readiness_enhancement_workpackagecreation = forms.CharField()
    is_shown_at_next_time_measurement_stop_workpackagecreation = forms.IntegerField()
    plan_duration_mins_workpackagecreation = forms.IntegerField()
    due_datetime_workpackagecreation = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())

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
