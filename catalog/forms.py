from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
import pytz

utc=pytz.UTC

from django import forms
from .widgets import XDSoftDateTimePickerInput
from .models import T_Calendar, Author, Book, BookInstance

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


class CreateT_Workpackage_Relevantinformation_Tobememorized_WithProposedWorkpackage_Form(forms.Form):
    """Form to create T_Workpackage_Relevantinformation with proposed t_workpackage_id and t_week_target_id."""
    week_target_wpritbmcreation = forms.ModelChoiceField(queryset=Author.objects.all(), label="Author", widget=forms.Select(), initial=0)
    workpackage_wpritbmcreation = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book", widget=forms.Select(), initial=0)
#    target_group_question_wpritbmcreation = forms.CharField()
    memorizable_workpackage_relevantinformation_tobememorized_wpritbmcreation = forms.CharField()
    relevantinformation_comment_wpritbmcreation = forms.CharField(required=False)
    is_workpackage_wpritbmcreation = forms.IntegerField(required=False)

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


class AssignT_Workpackage_Relevantinformation_Tobememorized_To_MemoryPalace_Location_And_Number_ForWorkpackage_Form(forms.Form):
    """Form to assign a workpackage_relevantinformation to a memory palace location and number."""
    workpackage_relevantinformation_tobememorized_memorization_sequence = forms.ModelChoiceField(queryset=BookInstance.objects.values_list('memorization_sequence', flat=True), label="Memorization sequence of workpackage relevant information to be memorized", widget=forms.Select(), initial=0)
    workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_id = forms.ModelChoiceField(queryset=BookInstance.objects.values_list('t_memory_palace_type_location_id', flat=True), label="Memory palace type location", widget=forms.Select(), initial=0)
    workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_number_id = forms.ModelChoiceField(queryset=BookInstance.objects.values_list('t_memory_palace_type_location_number_id', flat=True), label="Memory palace type location number", widget=forms.Select(), initial=0)

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