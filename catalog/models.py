from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns


class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name



# class T_Week_Target(models.Model):
class Author(models.Model):
    """Model representing an author."""
    t_memorization_package_memory_palace_technique_foreignkey = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type_location_number = models.ForeignKey('T_Memory_Palace_Type_Location_Number', on_delete=models.SET_NULL, null=True)
    date_frame_from_weekday = models.DateField(null=True, blank=True)
    date_frame_to_weekday = models.DateField(null=True, blank=True)
    phase_week_target_is_excluded_from_wt_mp_assignment_until = models.DateField(null=True, blank=True)
    phase_week_target_is_excluded_from_wt_mp_assignment_cause = models.CharField(max_length=255, default='')
    phase_week_target_is_excluded_from_wt_mp_assignment_wish = models.CharField(max_length=255, default='')
    is_not_during_working_hours = models.IntegerField(null=True, default=None)
    week_target_manual_sorting_category_indistinguishable = models.CharField(max_length=255, default='')
    recurrence_period_weeks = models.IntegerField(null=True, default=None)
    due_datetime = models.DateTimeField(null=True, blank=True)
    is_done_datetime = models.DateTimeField(null=True, blank=True)
    workpackages_relevantinformation_is_separate_memory_palace = models.IntegerField(null=True, default=None)
    memorization_sequence = models.IntegerField(null=True, default=None)
    memorization_sequence_is_fixed_because_memorized = models.IntegerField(null=True, default=None)

#Weitere zum Löschen:
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    memorizable_week_target = models.CharField(max_length=4000, default='')
    week_target_comment = models.CharField(max_length=4000, default='')
    

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 't_week_target'
        verbose_name = 'T_Week_Target'

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.memorizable_week_target



class T_Memory_Palace_Memorization_Timeseries(models.Model):
    t_week_target = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    t_workpackage_relevantinformation_tobememorized = models.ForeignKey('BookInstance', on_delete=models.SET_NULL, null=True)
    t_information_item_tobeoperationalized = models.ForeignKey('T_Information_Item_Tobeoperationalized', on_delete=models.SET_NULL, null=True) 
    t_conflict_strategy_category_measure = models.ForeignKey('T_Conflict_Strategy_Category_Measure', on_delete=models.SET_NULL, null=True)
    t_calendar = models.ForeignKey('T_Calendar', on_delete=models.SET_NULL, null=True)
    t_memory_palace_memorization_timeseries_action = models.ForeignKey('T_Memory_Palace_Memorization_Timeseries_Action', on_delete=models.SET_NULL, null=True)
    action_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_memory_palace_memorization_timeseries'



class T_Memory_Palace_Memorization_Timeseries_Action(models.Model):
    action_description = models.CharField(max_length=255, default='')   #--1: memory palace datapoint description shown, 2. corresponding memorizable known, 3: decided to repeat memory palace datapoint description

    class Meta:
        db_table = 't_memory_palace_memorization_timeseries_action'



class T_Day_Target_Sequence_Timeseries(models.Model):
    sequence_proposed_for_day_target_memory_palace = models.IntegerField(null=True, default=None)
    sequence_memorized_in_day_target_memory_palace = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_day_target_sequence_timeseries'



class T_Week_Target_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday(models.Model):
    t_week_target = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    week_target_isnot_potential_day_target_on_weekday_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 't_week_target_is_excluded_from_dt_mp_assignment_on_weekday'



# class T_Workpackage(models.Model):
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    t_calendar = models.ForeignKey('T_Calendar', on_delete=models.SET_NULL, null=True)
    associated_email_subject = models.CharField(max_length=1000, default='')
    associated_email_received_datetime = models.DateTimeField(null=True, blank=True)
    associated_email_received_account = models.CharField(max_length=1000, default='')
    filepath_for_readiness_enhancement = models.CharField(max_length=2000, default='')
    hyperlink_for_readiness_enhancement = models.CharField(max_length=2000, default='')
    is_shown_at_next_time_measurement_stop = models.IntegerField(null=True, default=None)
    plan_duration_mins = models.IntegerField(null=True, default=None)
    due_datetime = models.DateTimeField(null=True, blank=True)
    datetime_is_done = models.DateTimeField(null=True, blank=True)

#Weitere zum Löschen:
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    class Meta:
        db_table = 't_workpackage'
        verbose_name = 'T_Workpackage'



class T_Workpackage_Actual_Duration_Timeseries(models.Model):
    t_workpackage = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    measurement_datetime = models.DateTimeField(null=True, blank=True)
    measurement_type_start_or_stop = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_workpackage_actual_duration_timeseries'



class T_Wt_Or_Wp_Or_Infotbo_Category_Timeseries(models.Model):
    t_week_target = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    t_workpackage = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    t_information_item_tobeoperationalized = models.ForeignKey('T_Information_Item_Tobeoperationalized', on_delete=models.SET_NULL, null=True)
    t_category_table = models.ForeignKey('T_Category_Table', on_delete=models.SET_NULL, null=True)
    t_category_table_entry = models.ForeignKey('T_Category_Table_Entry', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_wt_or_wp_or_infotbo_category_timeseries'



import uuid  # Required for unique book instances
import datetime
import pytz

utc=pytz.UTC

from django.contrib.auth.models import User  # Required to assign User as a borrower

# class T_Workpackage_Relevantinformation_Tobememorized(models.Model):
class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id_asinteger = models.IntegerField(primary_key=True, default=None)
    id = models.UUIDField(primary_key=False, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    t_information_item_tobeoperationalized = models.ForeignKey('T_Information_Item_Tobeoperationalized', on_delete=models.SET_NULL, null=True)
    t_memorization_package_memory_palace_technique_foreignkey2 = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type_location_number = models.ForeignKey('T_Memory_Palace_Type_Location_Number', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    target_group_question = models.CharField(max_length=1000, default='')
    memorizable_workpackage_relevantinformation_tobememorized = models.CharField(max_length=1000, default='')
    relevantinformation_comment = models.CharField(max_length=2000, default='')
    memorization_sequence = models.IntegerField(null=True, default=None)
    memorization_sequence_is_fixed_because_memorized = models.IntegerField(null=True, default=None)
    is_workpackage = models.IntegerField(null=True, default=None)

#Weitere zum Löschen:
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and datetime.datetime.now().replace(tzinfo=utc) > self.due_back.replace(tzinfo=utc):
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)
        db_table = 't_workpackage_relevantinformation_tobememorized'
        verbose_name = 'T_Workpackage_Relevantinformation_Tobememorized'

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)



class T_Week_Target_Or_Workpackage_Or_Relevinf_Timeseries(models.Model):
    t_week_target = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    t_workpackage = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    t_workpackage_relevantinformation_tobememorized = models.ForeignKey('BookInstance', on_delete=models.SET_NULL, null=True)
    action_datetime = models.DateTimeField(null=True, blank=True)
    action_description_create_read_update_delete = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_week_target_or_workpackage_or_relevinf_timeseries'



class T_Information_Item_Tobeoperationalized(models.Model):
    t_memorization_package_memory_cards_technique = models.ForeignKey('T_Memorization_Package_Memory_Cards_Technique', on_delete=models.SET_NULL, null=True)
    t_memorization_package_memory_palace_technique_foreignkey3 = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type_location_number = models.ForeignKey('T_Memory_Palace_Type_Location_Number', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    target_group_question = models.CharField(max_length=1000, default='')
    memorizable_information_item_tobeoperationalized = models.CharField(max_length=1000, default='')
    memorization_sequence_memory_cards_technique = models.IntegerField(null=True, default=None)
    memorization_sequence_memory_palace_technique = models.IntegerField(null=True, default=None)
    memorization_sequence_mem_pal_tec_is_fixed_because_memorized = models.IntegerField(null=True, default=None)
    is_information_item_tobeoperationalized = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_information_item_tobeoperationalized'



class T_Information_Item_Tobeoperationalized_Memor_Timeseries(models.Model):
    t_information_item_tobeoperationalized = models.ForeignKey('T_Information_Item_Tobeoperationalized', on_delete=models.SET_NULL, null=True)
    t_information_item_tobeoperationalized_memor_timeseries_act = models.ForeignKey('T_Information_Item_Tobeoperationalized_Memor_Timeseries_Act', on_delete=models.SET_NULL, null=True)
    action_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_information_item_tobeoperationalized_memor_timeseries'



class T_Information_Item_Tobeoperationalized_Memor_Timeseries_Act(models.Model):
    action_description = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_information_item_tobeoperationalized_memor_timeseries_act'



class t_category_table(models.Model):
    category_table_name = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_category_table'



class T_Category_Table_Predicate_Asverb(models.Model):
    t_category_table_subject = models.ForeignKey('T_Category_Table', on_delete=models.SET_NULL, null=True)
    t_category_table_object = models.ForeignKey('T_Category_Table', related_name = 'T_Category_Table_Related_Name', on_delete=models.SET_NULL, null=True)
    predicate_asverb = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_category_table_predicate_asverb'



class t_category_table_entry(models.Model):
    t_category_table = models.ForeignKey('T_Category_Table', on_delete=models.SET_NULL, null=True)
    category_name = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_category_table_entry'
        verbose_name = 'T_Category_Table_Entry'



class T_Calendar(models.Model):
    t_workpackage = models.ForeignKey('Book', related_name = 'Book_Related_Name', on_delete=models.SET_NULL, null=True)
    t_calendar_conflict_related_association_foreignkey = models.ForeignKey('T_Calendar_Conflict_Related_Association', on_delete=models.SET_NULL, null=True)
    t_memorization_package_memory_palace_technique_foreignkey4 = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type_location_daytime = models.ForeignKey('T_Memory_Palace_Type_Location_Daytime', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    datetime_start = models.DateTimeField(null=True, blank=True)
    datetime_end = models.DateTimeField(null=True, blank=True)
    subject_description = models.CharField(max_length=1000, default='')
    location_description = models.CharField(max_length=1000, default='')
    series_frequency_in_days = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_calendar'



class T_Conflict(models.Model):
    priorization_conflict_workpackage_one = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    priorization_conflict_workpackage_two = models.ForeignKey('Book', related_name = 'Book_Related_Name2', on_delete=models.SET_NULL, null=True)
    general_conflict_konfliktgegenstand_titel = models.CharField(max_length=255, default='')
    general_conflict_konfliktgegenstand_mein_ziel_description = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_conflict'


class T_Calendar_Conflict_Related_Association(models.Model):
    t_calendar_foreignkey = models.ForeignKey('T_Calendar', on_delete=models.SET_NULL, null=True)
    t_conflict = models.ForeignKey('T_Conflict', on_delete=models.SET_NULL, null=True)
    t_category_table_entry = models.ForeignKey('T_Category_Table_Entry', on_delete=models.SET_NULL, null=True)  #t_client_id = Konfliktpartner
    t_memorization_package_memory_palace_technique = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    hypothetic_appointment_datetime = models.DateTimeField(null=True, blank=True)
    hypothetic_appointment_association_description = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_calendar_conflict_related_association'


class T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt(models.Model):
    t_conflict = models.ForeignKey('T_Conflict', on_delete=models.SET_NULL, null=True)
    t_calendar_conflict_related_association = models.ForeignKey('T_Calendar_Conflict_Related_Association', on_delete=models.SET_NULL, null=True)
    t_ausatemmuskulatur_strategyrefinement_conflict_phase = models.ForeignKey('T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    memorized_unit_is_gone_through_mentally = models.IntegerField(null=True, default=None)
    memory_palace_is_enhanced_or_complete = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt'


class T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase(models.Model):
    conflict_phase_name = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_ausatemmuskulatur_strategyrefinement_conflict_phase'


class T_Conflict_Strategy_Category(models.Model):
    conflict_strategy_category_verb = models.CharField(max_length=255, default='')
    conflict_strategy_category_mywish = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_conflict_strategy_category'


class T_Conflict_Strategy_Category_Measure(models.Model):
    t_conflict_strategy_category =  models.ForeignKey('T_Conflict_Strategy_Category', on_delete=models.SET_NULL, null=True)
    t_memorization_package_memory_palace_technique_foreignkey5 =  models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type_location_number =  models.ForeignKey('T_Memory_Palace_Type_Location_Number', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    conflict_strategy_category_measure_description = models.CharField(max_length=255, default='')
    memorization_sequence = models.IntegerField(null=True, default=None)
    memorization_sequence_is_fixed_because_memorized = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_conflict_strategy_category_measure'



class T_Memorization_Package_Memory_Palace_Technique(models.Model):
    t_memory_palace_type = models.ForeignKey('T_Memory_Palace_Type', on_delete=models.SET_NULL, null=True)
    t_week_target = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    t_workpackage_relevantinformation_tobememorized = models.ForeignKey('BookInstance', on_delete=models.SET_NULL, null=True)
    t_information_item_tobeoperationalized_foreignkey = models.ForeignKey('T_Information_Item_Tobeoperationalized', on_delete=models.SET_NULL, null=True)
    t_conflict_strategy_category_measure_foreignkey = models.ForeignKey('T_Conflict_Strategy_Category_Measure', on_delete=models.SET_NULL, null=True)
    t_calendar_foreignkey2 = models.ForeignKey('T_Calendar', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    memorization_package_title = models.CharField(max_length=255, default='')
    memorization_package_is_active = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memorization_package_memory_palace_technique'


class T_Memory_Palace_Type(models.Model):
    memory_palace_type = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_memory_palace_type'


class T_Memory_Palace_Type_Location(models.Model):
    t_memorization_package_memory_palace_technique = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type = models.ForeignKey('T_Memory_Palace_Type', on_delete=models.SET_NULL, null=True)
    sequence_proposed_for_new_memorization_package = models.IntegerField(null=True, default=None)
    memory_palace_type_location = models.CharField(max_length=255, default='')
    memory_palace_type_location_is_inactive = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memory_palace_type_location'


class T_Memory_Palace_Type_Location_Packageassignment_Timeseries(models.Model):
    t_memory_palace_type_location = models.ForeignKey('T_Memory_Palace_Type_Location', on_delete=models.SET_NULL, null=True)
    t_memorization_package_memory_palace_technique = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    assignment_to_memorization_package_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_memory_palace_type_location_packageassignment_timeseries'


class T_Memory_Palace_Type_Location_Number(models.Model):
    t_memory_palace_type_location = models.ForeignKey('T_Memory_Palace_Type_Location', on_delete=models.SET_NULL, null=True)
    memory_palace_number = models.IntegerField(null=True, default=None)
    memory_palace_datapoint_description = models.CharField(max_length=255, default='')
    memory_palace_datapoint_lastuse_date = models.DateTimeField(null=True, blank=True)
    memory_palace_datapoint_is_inactive = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memory_palace_type_location_number'


class T_Memory_Palace_Type_Location_Daytime(models.Model):
    t_memory_palace_type_location = models.ForeignKey('T_Memory_Palace_Type_Location', on_delete=models.SET_NULL, null=True)
    memory_palace_daytime = models.DateTimeField(null=True, blank=True)
    memory_palace_daytime_datapoint_description = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_memory_palace_type_location_daytime'


class T_Memorization_Package_Memory_Cards_Technique(models.Model):
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    memorization_package_title = models.CharField(max_length=255, default='')
    memorization_package_is_active = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memorization_package_memory_cards_technique'

