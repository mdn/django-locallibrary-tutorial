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
    # t_memorization_package_memory_palace_technique_id = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    # t_memory_palace_type_location_number_id = models.ForeignKey('T_Memory_Palace_Type_Location_Number', on_delete=models.SET_NULL, null=True)
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

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)



# class T_Workpackage(models.Model):
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in file.
    # t_calendar_id = ForeignKey('t_calendar', on_delete=models.SET_NULL, null=True)
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


import uuid  # Required for unique book instances
import datetime
import pytz

utc=pytz.UTC

from django.contrib.auth.models import User  # Required to assign User as a borrower

# class T_Workpackage_Relevantinformation_Tobememorized(models.Model):
class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#    t_information_item_tobeoperationalized_id = models.ForeignKey('t_information_item_tobeoperationalized', on_delete=models.SET_NULL, null=True)
#    t_memorization_package_memory_palace_technique_id = models.ForeignKey('t_memorization_package_memory_palace_technique', on_delete=models.SET_NULL, null=True)
#    t_memory_palace_type_location_number_id = models.ForeignKey('t_memory_palace_type_location_number', on_delete=models.SET_NULL, null=True)
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

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)


class T_Information_Item_Tobeoperationalized(models.Model):
#    t_memorization_package_memory_cards_technique_id = models.ForeignKey('t_memorization_package_memory_cards_technique', on_delete=models.SET_NULL, null=True)
#    t_memorization_package_memory_palace_technique_id = models.ForeignKey('t_memorization_package_memory_palace_technique', on_delete=models.SET_NULL, null=True)
#    t_memory_palace_type_location_number_id = models.ForeignKey('t_memory_palace_type_location_number', on_delete=models.SET_NULL, null=True)
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


class T_Calendar(models.Model):
#   t_workpackage_id = models.ForeignKey('t_workpackage_id', on_delete=models.SET_NULL, null=True)
#   t_calendar_conflict_related_association_id = models.ForeignKey('t_calendar_conflict_related_association_id', on_delete=models.SET_NULL, null=True)
#   t_memorization_package_memory_palace_technique_id = models.ForeignKey('t_memorization_package_memory_palace_technique_id', on_delete=models.SET_NULL, null=True)
#   t_memory_palace_type_location_daytime_id = models.ForeignKey('t_memory_palace_type_location_daytime_id', on_delete=models.SET_NULL, null=True)
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
    priorization_conflict_workpackage_id_one = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#    priorization_conflict_workpackage_id_two = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    general_conflict_konfliktgegenstand_titel = models.CharField(max_length=255, default='')
    general_conflict_konfliktgegenstand_mein_ziel_description = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_conflict'



class T_Memorization_Package_Memory_Palace_Technique(models.Model):
#    t_memory_palace_type_id = models.ForeignKey('T_Memory_Palace_Type', on_delete=models.SET_NULL, null=True)
    t_week_target_id = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    t_workpackage_relevantinformation_tobememorized_id = models.ForeignKey('BookInstance', on_delete=models.SET_NULL, null=True)
    t_information_item_tobeoperationalized_id = models.ForeignKey('T_Information_Item_Tobeoperationalized', on_delete=models.SET_NULL, null=True)
#    t_conflict_strategy_category_measure_id = models.ForeignKey('T_Conflict_Strategy_Category_Measure', on_delete=models.SET_NULL, null=True)
    t_calendar_id = models.ForeignKey('T_Calendar', on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    memorization_package_title = models.CharField(max_length=255, default='')
    memorization_package_is_active = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memorization_package_memory_palace_technique'



class T_Memorization_Package_Memory_Cards_Technique(models.Model):
    created_datetime = models.DateTimeField(null=True, blank=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    memorization_package_title = models.CharField(max_length=255, default='')
    memorization_package_is_active = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memorization_package_memory_cards_technique'


class T_Memory_Palace_Type(models.Model):
    memory_palace_type = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 't_memory_palace_type'


class T_Memory_Palace_Type_Location(models.Model):
    t_memorization_package_memory_palace_technique_id = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    t_memory_palace_type_id = models.ForeignKey('T_Memory_Palace_Type', on_delete=models.SET_NULL, null=True)
    sequence_proposed_for_new_memorization_package = models.IntegerField(null=True, default=None)
    memory_palace_type_location = models.CharField(max_length=255, default='')
    memory_palace_type_location_is_inactive = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memory_palace_type_location'


class T_Memory_Palace_Type_Location_Packageassignment_Timeseries(models.Model):
    t_memory_palace_type_location_id = models.ForeignKey('T_Memory_Palace_Type_Location', on_delete=models.SET_NULL, null=True)
    t_memorization_package_memory_palace_technique_id = models.ForeignKey('T_Memorization_Package_Memory_Palace_Technique', on_delete=models.SET_NULL, null=True)
    assignment_to_memorization_package_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 't_memory_palace_type_location_packageassignment_timeseries'


class T_Memory_Palace_Type_Location_Number(models.Model):
    t_memory_palace_type_location_id = models.ForeignKey('T_Memory_Palace_Type_Location', on_delete=models.SET_NULL, null=True)
    memory_palace_number = models.IntegerField(null=True, default=None)
    memory_palace_datapoint_description = models.CharField(max_length=255, default='')
    memory_palace_datapoint_lastuse_date = models.DateTimeField(null=True, blank=True)
    memory_palace_datapoint_is_inactive = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 't_memory_palace_type_location_number'


class T_Memory_Palace_Type_Location_Daytime(models.Model):
    t_memory_palace_type_location_id = models.ForeignKey('T_Memory_Palace_Type_Location', on_delete=models.SET_NULL, null=True)
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

