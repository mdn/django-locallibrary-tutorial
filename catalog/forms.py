from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
import pytz

utc=pytz.UTC

from django import forms
from .widgets import XDSoftDateTimePickerInput
from .models import T_Calendar, Author, Book, BookInstance, T_Conflict, T_Memory_Palace_Type_Location

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


class AssignT_Workpackage_Relevantinformation_Tobememorized_To_MemoryPalace_Location_And_Number_ForSpecificWorkpackage_Form(forms.Form):
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


from django.db.models import Value, CharField, Count, Max, Min

class Assign_Memorizable_Set_To_Memorypalace_Locations_And_Numbers_Form(forms.Form):
    """Form to assign a memorizable set to memory palace locations and their respective numbers."""
    assigned_memory_palace_first = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)
    assigned_memory_palace_second = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)


#    is_job_week_targets = forms.IntegerField()
#    is_job_workpackages_relevantinformation_tobememorized = forms.IntegerField()
#    is_private_week_targets = forms.IntegerField()
#    is_private_workpackages_relevantinformation_tobememorized = forms.IntegerField()
#    conflict_measures = forms.ModelChoiceField(queryset=T_Conflict.objects.values_list('general_conflict_konfliktgegenstand_titel', flat=True).order_by('id'), label="Konflikt auswählen", widget=forms.Select(), initial=0, empty_label='', required=False)

    #Separate MP:
#    memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__week_target__object_list = forms.ModelChoiceField(queryset=Author.objects.filter(t_memorization_package_mp_technique_assignmenttype_category__t_memorization_package_mp_technique_assignmenttype=1).values('memorization_sequence', 'memorizable_week_target', 't_memory_palace_type_location__memory_palace_type_location', 't_memory_palace_type_location_number__memory_palace_datapoint_description').order_by('memorization_sequence').annotate(origination_table=Value('t_week_target', output_field=CharField())).values_list('memorization_sequence', 'memorizable_week_target', 't_memory_palace_type_location__memory_palace_type_location', 't_memory_palace_type_location_number__memory_palace_datapoint_description', 'origination_table'), label="memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__week_target", widget=forms.Select(), initial=0, empty_label='', required=False)
    #Proposed memory palaces:
###    assigned_memory_palace = T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).order_by('id').annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).values('memory_palace_type_location', 'number_of_memorypalace_datapoints_perlocation', 'lastusage_date')

#    workpackage_wpritbmcreation = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book", widget=forms.Select(), initial=0)
#    test = assigned_memory_palace.values
#    assigned_memory_palace_choices = [('')] + [(id.memory_palace_type_location) for id in assigned_memory_palace]
#    a, b, c = assigned_memory_palace
#    assigned_memory_palace_choices_form = forms.ChoiceField(assigned_memory_palace_choices, required=False, widget=forms.Select())
##    assigned_memory_palace = forms.ModelChoiceField(queryset=T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).values('memory_palace_type_location').order_by('id').annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).values_list('memory_palace_type_location', 'number_of_memorypalace_datapoints_perlocation', 'lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0, empty_label='', required=False)
#    assigned_memory_palace_sss = forms.MultipleChoiceField(assigned_memory_palace, widget=forms.Select(), required=False)


    # ToDo: noch anpassen
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


class Assign_Memorizables_To_MP_Locations_And_Numbers_Workpackage_Relevantinformation_Tobememorized_Form(forms.Form):
    """Form to assign a memorizable set to memory palace locations and their respective numbers."""
    assigned_memory_palace_first = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)
    assigned_memory_palace_second = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)
    assigned_memory_palace_third = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)
    assigned_memory_palace_fourth = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)
    assigned_memory_palace_fifth = forms.ModelChoiceField(T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date'), label="assigned_memory_palace", widget=forms.Select(), initial=0)

    # ToDo: noch anpassen
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
