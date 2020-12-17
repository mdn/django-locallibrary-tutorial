from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Book, BookInstance, T_Workpackage_Actual_Duration_Timeseries, T_Memorization_Package_MP_Technique_Assignmenttype_Category, Author, T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_Timeseries, T_Day_Target_Sequence_Timeseries, BookInstance, Genre, T_Calendar, T_Conflict, T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt, T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase, T_Conflict_Strategy_Category, T_Conflict_Strategy_Category_Measure, T_Information_Item_Tobeoperationalized, T_Information_Item_Tobeoperationalized_Memor_Timeseries, T_Information_Item_Tobeoperationalized_Memor_Timeseries_Act, T_Category_Table, T_Category_Table_Predicate_Asverb, T_Category_Table_Entry, T_Category_Timeseries, T_Memorization_Package_Memory_Palace_Or_Cards_Technique, T_Memory_Palace_Type, T_Memory_Palace_Type_Location, T_Memory_Palace_Type_Location_Packageassignment_Timeseries, T_Memory_Palace_Type_Location_Number, T_Memory_Palace_Type_Location_Daytime, T_Memory_Palace_Or_Cards_Memorization_Timeseries, T_Memory_Palace_Or_Cards_Memorization_Timeseries_Action


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available copies of books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_visits': num_visits},
    )


from django.views import generic


class BookListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10

class BookDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class BookInstanceDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a bookinstance."""
    model = BookInstance


class T_Workpackage_Actual_Duration_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_workpackages_actual_duration_timeseries."""
    model = T_Workpackage_Actual_Duration_Timeseries
    paginate_by = 10

class T_Workpackage_Actual_Duration_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_workpackage_actual_duration_timeseries."""
    model = T_Workpackage_Actual_Duration_Timeseries

#class T_Memorization_Package_MP_Technique_AssignmenttypeListView(LoginRequiredMixin, generic.ListView):
#    """Generic class-based list view for a list of t_memorization_package_mp_technique_assignmenttypes."""
#    model = T_Memorization_Package_MP_Technique_Assignmenttype
#    paginate_by = 10

#class T_Memorization_Package_MP_Technique_AssignmenttypeDetailView(LoginRequiredMixin, generic .DetailView):
#    """Generic class-based detail view for an t_memorization_package_mp_technique_assignmenttype."""
#    model = T_Memorization_Package_MP_Technique_Assignmenttype

class T_Memorization_Package_MP_Technique_Assignmenttype_CategoryListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based list view for a list of t_memorization_package_mp_technique_assignmenttype_categorys."""
    model = T_Memorization_Package_MP_Technique_Assignmenttype_Category
    paginate_by = 10

class T_Memorization_Package_MP_Technique_Assignmenttype_CategoryDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for an t_memorization_package_mp_technique_assignmenttype_category."""
    model = T_Memorization_Package_MP_Technique_Assignmenttype_Category

class AuthorListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10

class AuthorDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for an author."""
    model = Author


class T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based list view for a list of t_wt_is_excluded_from_dt_mp_assignment_on_weekdays_timeseries."""
    model = T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_Timeseries
    paginate_by = 10

class T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_wt_is_excluded_from_dt_mp_assignment_on_weekday_timeseries."""
    model = T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_Timeseries


class T_Day_Target_Sequence_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based list view for a list of t_day_targets_sequence_timeseries."""
    model = T_Day_Target_Sequence_Timeseries
    paginate_by = 10

class T_Day_Target_Sequence_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_day_target_sequence_timeseries."""
    model = T_Day_Target_Sequence_Timeseries


class T_CalendarListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_calendars."""
    model = T_Calendar
    paginate_by = 10

class T_CalendarDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_calendar."""
    model = T_Calendar


class T_ConflictListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_conflicts."""
    model = T_Conflict
    paginate_by = 10

class T_ConflictDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_conflict."""
    model = T_Conflict


class T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt."""
    model = T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt
    paginate_by = 10

class T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt."""
    model = T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt


class T_Ausatemmuskulatur_Strategyrefinement_Conflict_PhaseListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_ausatemmuskulatur_strategyrefinement_conflict_phases."""
    model = T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase
    paginate_by = 10

class T_Ausatemmuskulatur_Strategyrefinement_Conflict_PhaseDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_ausatemmuskulatur_strategyrefinement_conflict_phase."""
    model = T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase


class T_Conflict_Strategy_CategoryListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_conflict_strategy_categorys."""
    model = T_Conflict_Strategy_Category
    paginate_by = 10

class T_Conflict_Strategy_CategoryDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_conflict_strategy_category."""
    model = T_Conflict_Strategy_Category


class T_Conflict_Strategy_Category_MeasureListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_conflict_strategy_category_measures."""
    model = T_Conflict_Strategy_Category_Measure
    paginate_by = 10

class T_Conflict_Strategy_Category_MeasureDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_conflict_strategy_category_measure."""
    model = T_Conflict_Strategy_Category_Measure


class T_Information_Item_TobeoperationalizedListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_information_items_tobeoperationalized."""
    model = T_Information_Item_Tobeoperationalized
    paginate_by = 10

class T_Information_Item_TobeoperationalizedDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_information_item_tobeoperationalized."""
    model = T_Information_Item_Tobeoperationalized


class T_Information_Item_Tobeoperationalized_Memor_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_information_item_tobeoperationalized_memor_timeseries."""
    model = T_Information_Item_Tobeoperationalized_Memor_Timeseries
    paginate_by = 10

class T_Information_Item_Tobeoperationalized_Memor_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_information_item_tobeoperationalized_memor_timeseries."""
    model = T_Information_Item_Tobeoperationalized_Memor_Timeseries


class T_Information_Item_Tobeoperationalized_Memor_Timeseries_ActListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_information_item_tobeoperationalized_memor_timeseries_act."""
    model = T_Information_Item_Tobeoperationalized_Memor_Timeseries_Act
    paginate_by = 10

class T_Information_Item_Tobeoperationalized_Memor_Timeseries_ActDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_information_item_tobeoperationalized_memor_timeseries_act."""
    model = T_Information_Item_Tobeoperationalized_Memor_Timeseries_Act


class T_Category_TableListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_category_tables."""
    model = T_Category_Table
    paginate_by = 10

class T_Category_TableDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_category_table."""
    model = T_Category_Table


class T_Category_Table_EntryListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_category_table_entries."""
    model = T_Category_Table_Entry
    paginate_by = 10

class T_Category_Table_EntryDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_category_table_entry."""
    model = T_Category_Table_Entry


class T_Category_Table_Predicate_AsverbListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_category_table_predicates_asverb."""
    model = T_Category_Table_Predicate_Asverb
    paginate_by = 10

class T_Category_Table_Predicate_AsverbDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_category_table_predicate_asverb."""
    model = T_Category_Table_Predicate_Asverb


class T_Category_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_category_timeseries."""
    model = T_Category_Timeseries
    paginate_by = 10

class T_Category_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_category_timeseries."""
    model = T_Category_Timeseries


class T_Memorization_Package_Memory_Palace_Or_Cards_TechniqueListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memorization_packages_memory_palace_or_cards_technique."""
    model = T_Memorization_Package_Memory_Palace_Or_Cards_Technique
    paginate_by = 10


class T_Memorization_Package_Memory_Palace_Or_Cards_TechniqueDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memorization_package_memory_palace_or_cards_technique."""
    model = T_Memorization_Package_Memory_Palace_Or_Cards_Technique


class T_Memory_Palace_TypeListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palaces_type."""
    model = T_Memory_Palace_Type
    paginate_by = 10

class T_Memory_Palace_TypeDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_type."""
    model = T_Memory_Palace_Type


class T_Memory_Palace_Type_LocationListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palaces_type_location."""
    model = T_Memory_Palace_Type_Location
    paginate_by = 10

class T_Memory_Palace_Type_LocationDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location."""
    model = T_Memory_Palace_Type_Location


class T_Memory_Palace_Type_Location_Packageassignment_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palaces_type_location."""
    model = T_Memory_Palace_Type_Location_Packageassignment_Timeseries
    paginate_by = 10

class T_Memory_Palace_Type_Location_Packageassignment_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location_packageassignment_timeseries."""
    model = T_Memory_Palace_Type_Location_Packageassignment_Timeseries


class T_Memory_Palace_Type_Location_NumberListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palace_type_location_number."""
    model = T_Memory_Palace_Type_Location_Number
    paginate_by = 10

class T_Memory_Palace_Type_Location_NumberDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location_number."""
    model = T_Memory_Palace_Type_Location_Number


class T_Memory_Palace_Type_Location_DaytimeListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palaces_type_location_daytime."""
    model = T_Memory_Palace_Type_Location_Daytime
    paginate_by = 10

class T_Memory_Palace_Type_Location_DaytimeDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location_daytime."""
    model = T_Memory_Palace_Type_Location_Daytime


class T_Memory_Palace_Or_Cards_Memorization_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palaces_or_cards_memorization_timeseries."""
    model = T_Memory_Palace_Or_Cards_Memorization_Timeseries
    paginate_by = 10

class T_Memory_Palace_Or_Cards_Memorization_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_or_cards_memorization_timeseries."""
    model = T_Memory_Palace_Or_Cards_Memorization_Timeseries


class T_Memory_Palace_Or_Cards_Memorization_Timeseries_ActionListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_memory_palace_or_cards_memorization_timeseries_actions."""
    model = T_Memory_Palace_Or_Cards_Memorization_Timeseries_Action
    paginate_by = 10

class T_Memory_Palace_Or_Cards_Memorization_Timeseries_ActionDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_memory_palace_or_cards_memorization_timeseries_action."""
    model = T_Memory_Palace_Or_Cards_Memorization_Timeseries_Action





class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


# Added as part of challenge!
from django.contrib.auth.mixins import PermissionRequiredMixin


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required

from catalog.forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        proposed_test_character_field = Book.objects.get(pk=pk)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date, 'test_character_field': proposed_test_character_field})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


from catalog.forms import CreateWorkPackage_WithProposedWeekTarget_Form, CreateT_Workpackage_Relevantinformation_Tobememorized_WithProposedWorkpackage_Form, AssignT_Workpackage_Relevantinformation_Tobememorized_To_MemoryPalace_Location_And_Number_ForSpecificWorkpackage_Form, Assign_Memorizable_Set_To_Memorypalace_Locations_And_Numbers_Form
from django import forms

@permission_required('catalog.can_mark_returned')
def book_create_proposed_week_target(request, pk):
    """View function for creating a new work package for a specific week target."""
    week_target = get_object_or_404(Author, pk=pk)
    work_package = Book()   #workpackage_title="Neuer Arbeitspaket Titel", filepath_for_readiness_enhancement="filepath123"
#funzt:     datetime_start = forms.IntegerField(widget=forms.Select(choices=T_Calendar.objects.all().values_list()))
#    e = Book.objects.select_related('bookinstance')
    f = Book.objects.prefetch_related('bookinstance_set').all()
#    g = f.memorizable_workpackage_relevantinformation_tobememorized
    h = BookInstance.objects.prefetch_related('bookinstance_set').all().values()
    i = Author.objects.prefetch_related('book_set').all()
    j = Author.objects.prefetch_related('book_set').get(pk=1)
    k = Author.objects.prefetch_related('book__bookinstance').values()
#    l = k.value_from_object(l)
    n = BookInstance.objects.prefetch_related('book_set').values()
    o = n.values('book_id').filter(book_id=1)


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateWorkPackage_WithProposedWeekTarget_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            work_package.author_id = form.cleaned_data['week_target_workpackagecreation'].id
            work_package.author_id = pk
            if form.cleaned_data['datetime_start'] is not None:
                work_package.t_calendar_id = form.cleaned_data['datetime_start'].id
            work_package.created_datetime = datetime.datetime.now()
            work_package.workpackage_title = form.cleaned_data['workpackage_title_workpackagecreation']
            work_package.associated_email_subject = form.cleaned_data['associated_email_subject_workpackagecreation']
            work_package.associated_email_received_datetime = form.cleaned_data['associated_email_received_datetime_workpackagecreation']
            work_package.associated_email_received_account = form.cleaned_data['associated_email_received_account_workpackagecreation']
            work_package.filepath_for_readiness_enhancement = form.cleaned_data['filepath_for_readiness_enhancement_workpackagecreation']
            work_package.hyperlink_for_readiness_enhancement = form.cleaned_data['hyperlink_for_readiness_enhancement_workpackagecreation']
            work_package.is_shown_at_next_time_measurement_stop = form.cleaned_data['is_shown_at_next_time_measurement_stop_workpackagecreation']
            work_package.plan_duration_mins = form.cleaned_data['plan_duration_mins_workpackagecreation']
            due_datetime = form.cleaned_data['due_datetime_workpackagecreation']
            work_package.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('books'))

    # If this is a GET (or any other method) create the default form
    else:
        week_target_proposed = Author.objects.get(pk=pk)
        t_calendar_proposed = T_Calendar.objects.latest('datetime_start')
        form = CreateWorkPackage_WithProposedWeekTarget_Form(initial={'week_target_workpackagecreation': week_target_proposed, 'datetime_start': t_calendar_proposed})

    context = {
        'form': form,
        'work_package': work_package,
    }

    return render(request, 'catalog/book_create_proposed_week_target.html', context)


@permission_required('catalog.can_mark_returned')
def bookinstance_create_proposed_workpackage(request, pk):
    """View function for creating a new work package for a specific week target."""
#    workpackage = get_object_or_404(Book, pk=pk)
    t_workpackage_relevantinformation_tobememorized = BookInstance()

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateT_Workpackage_Relevantinformation_Tobememorized_WithProposedWorkpackage_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            work_package.author_id = form.cleaned_data['week_target_workpackagecreation'].id
            t_workpackage_relevantinformation_tobememorized.book_id = pk
            t_workpackage_relevantinformation_tobememorized.created_datetime = datetime.datetime.now()
#            t_workpackage_relevantinformation_tobememorized.target_group_question = form.cleaned_data['target_group_question_wpritbmcreation']
            t_workpackage_relevantinformation_tobememorized.memorizable_workpackage_relevantinformation_tobememorized = form.cleaned_data['memorizable_workpackage_relevantinformation_tobememorized_wpritbmcreation']
            t_workpackage_relevantinformation_tobememorized.relevantinformation_comment = form.cleaned_data['relevantinformation_comment_wpritbmcreation']
            t_workpackage_relevantinformation_tobememorized.is_workpackage = form.cleaned_data['is_workpackage_wpritbmcreation']
            t_workpackage_relevantinformation_tobememorized.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('books'))        #ToDo: will für das erste Arbeitspaket wieder auf der Übersicht mit Arbeitspaket UND relevanten AP-Informationen landen d.h. auf http://127.0.0.1:8000/catalog/book/1

    # If this is a GET (or any other method) create the default form
    else:
        workpackage_proposed = Book.objects.get(pk=pk)
        week_target_proposed = Author.objects.get(pk=workpackage_proposed.author_id)
#        workpackage_proposed.author
#        Author.objects.get(pk=pk)
#        t_calendar_proposed = T_Calendar.objects.latest('datetime_start')
        form = CreateT_Workpackage_Relevantinformation_Tobememorized_WithProposedWorkpackage_Form(initial={'workpackage_wpritbmcreation': workpackage_proposed, 'week_target_wpritbmcreation': week_target_proposed})

    context = {
        'form': form,
        't_workpackage_relevantinformation_tobememorized': t_workpackage_relevantinformation_tobememorized,
    }

    return render(request, 'catalog/bookinstance_create_proposed_workpackage.html', context)



@permission_required('catalog.can_mark_returned')
def book_bookinstance_assign_memorypalace_location_and_number_for_specific_workpackage(request, pk):
    """View function for assigning a workpackage_relevantinformation to a memory palace location and number."""
    t_workpackage_relevantinformation_tobememorized_tobeassigned = get_object_or_404(BookInstance, pk=pk)


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AssignT_Workpackage_Relevantinformation_Tobememorized_To_MemoryPalace_Location_And_Number_ForSpecificWorkpackage_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            work_package.author_id = form.cleaned_data['week_target_workpackagecreation'].id
#            t_workpackage_relevantinformation_tobememorized.book_id = pk
#            t_workpackage_relevantinformation_tobememorized.created_datetime = datetime.datetime.now()
#            t_workpackage_relevantinformation_tobememorized.target_group_question = form.cleaned_data['target_group_question_wpritbmcreation']
#            t_workpackage_relevantinformation_tobememorized.memorizable_workpackage_relevantinformation_tobememorized = form.cleaned_data['memorizable_workpackage_relevantinformation_tobememorized_wpritbmcreation']
#            t_workpackage_relevantinformation_tobememorized.relevantinformation_comment = form.cleaned_data['relevantinformation_comment_wpritbmcreation']
#            t_workpackage_relevantinformation_tobememorized.is_workpackage = form.cleaned_data['is_workpackage_wpritbmcreation']
#            t_workpackage_relevantinformation_tobememorized.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('books'))        #ToDo: will für das erste Arbeitspaket wieder auf der Übersicht mit Arbeitspaket UND relevanten AP-Informationen landen d.h. auf http://127.0.0.1:8000/catalog/book/1

    # If this is a GET (or any other method) create the default form
    else:
        workpackage_relevantinformation_tobememorized_proposed = BookInstance.objects.get(pk=pk)
        workpackage_relevantinformation_tobememorized_memorization_sequence_proposed = workpackage_relevantinformation_tobememorized_proposed.memorization_sequence
        workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_id_proposed = workpackage_relevantinformation_tobememorized_proposed.t_memory_palace_type_location_id
        workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_number_id_proposed = workpackage_relevantinformation_tobememorized_proposed.t_memory_palace_type_location_number_id

#        workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_id_proposed = t_memory_palace_type_location.objects.get(pk=workpackage_proposed.author_id)
#        workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_number_id_proposed = t_memory_palace_type_location_number.objects.get(pk=workpackage_proposed.author_id)
        form = AssignT_Workpackage_Relevantinformation_Tobememorized_To_MemoryPalace_Location_And_Number_ForSpecificWorkpackage_Form(initial={'workpackage_relevantinformation_tobememorized_memorization_sequence': workpackage_relevantinformation_tobememorized_memorization_sequence_proposed, 'workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_id': workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_id_proposed, 'workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_number_id': workpackage_relevantinformation_tobememorized_t_memory_palace_type_location_number_id_proposed})

    context = {
        'form': form,
        't_workpackage_relevantinformation_tobememorized_tobeassigned': t_workpackage_relevantinformation_tobememorized_tobeassigned,
    }

    return render(request, 'catalog/book_bookinstance_assign_memorypalace_location_and_number_for_specific_workpackage.html', context)


#from django.db.models import FilteredRelation, Q
#from itertools import chain
from django.db.models import Value, CharField, Count, Max, Min

@permission_required('catalog.can_mark_returned')
def aaa(request, pk):
#aaa=assign_memorizable_set_to_memorypalace_locations_and_numbers
    """View function for assigning a workpackage_relevantinformation to a memory palace location and number."""
    #Separate MP:
#    memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__week_target__object_list = Author.objects.filter(t_memorization_package_mp_technique_assignmenttype_category__t_memorization_package_mp_technique_assignmenttype=1).values('memorization_sequence', 'memorizable_week_target', 't_memory_palace_type_location__memory_palace_type_location', 't_memory_palace_type_location_number__memory_palace_datapoint_description').order_by('memorization_sequence').annotate(origination_table=Value('t_week_target', output_field=CharField())).values_list('memorization_sequence', 'memorizable_week_target', 't_memory_palace_type_location__memory_palace_type_location', 't_memory_palace_type_location_number__memory_palace_datapoint_description', 'origination_table')
    memorizable_objects_tobeassignedto_mp_locations__separate_memorypalace__week_target = Author.objects.filter(t_memorization_package_mp_technique_assignmenttype_category=pk)
#    memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__workpackage_relevantinformation_tobememorized__object_list = BookInstance.objects.filter(book__author__t_memorization_package_mp_technique_assignmenttype_category__t_memorization_package_mp_technique_assignmenttype=1).values('memorization_sequence', 'memorizable_workpackage_relevantinformation_tobememorized', 't_memory_palace_type_location_id', 't_memory_palace_type_location_number_id').order_by('memorization_sequence').annotate(origination_table=Value('t_workpackage_relevantinformation_tobememorized', output_field=CharField()))

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Assign_Memorizable_Set_To_Memorypalace_Locations_And_Numbers_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            assigned_memory_palace_fromform_first = form.cleaned_data['assigned_memory_palace_first']
            assigned_memory_palace_fromform_second = form.cleaned_data['assigned_memory_palace_second']
            maximum_capacity_assigned_memory_palace_fromform_first = assigned_memory_palace_fromform_first.number_of_memorypalace_datapoints_perlocation        #.annotate(abc = Max('t_memory_palace_type_location_number__memory_palace_number'))
            maximum_capacity_assigned_memory_palace_fromform_second = assigned_memory_palace_fromform_second.number_of_memorypalace_datapoints_perlocation        #.annotate(abc = Max('t_memory_palace_type_location_number__memory_palace_number'))
            
            #Initialize and start for-loop:
            i = 1
            for mem in memorizable_objects_tobeassignedto_mp_locations__separate_memorypalace__week_target:
                if mem.memorization_sequence <= maximum_capacity_assigned_memory_palace_fromform_first:
                    mem.t_memory_palace_type_location_id = assigned_memory_palace_fromform_first.id
                    mem.t_memory_palace_type_location_number_id = T_Memory_Palace_Type_Location_Number.objects.get(t_memory_palace_type_location_id = assigned_memory_palace_fromform_first.id, memory_palace_number = i).id
                    mem.save()
                    i+=1
                else:
                    mem.t_memory_palace_type_location_id = assigned_memory_palace_fromform_second
                    mem.t_memory_palace_type_location_number_id = T_Memory_Palace_Type_Location_Number.objects.get(t_memory_palace_type_location_id = assigned_memory_palace_fromform_second.id, memory_palace_number = i - maximum_capacity_assigned_memory_palace_fromform_first).id
                    mem.save()
                    i+=1

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('assign-memorizables-set-to-memorypalace-locations-and-numbers', kwargs={'pk': pk}))
#books=assign_memorizables_set_to_memorypalace_locations_and_numbers
    # If this is a GET (or any other method) create the default form
    else:
        assigned_memory_palace_proposed_first = T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date')[0]
        assigned_memory_palace_proposed_second = T_Memory_Palace_Type_Location.objects.filter(t_memory_palace_type=1).annotate(number_of_memorypalace_datapoints_perlocation = Count('t_memory_palace_type_location_number', distinct=True)).annotate(lastusage_date = Max('t_memory_palace_type_location_packageassignment_timeseries__assignment_to_memorization_package_datetime')).order_by('lastusage_date')[1]

        form = Assign_Memorizable_Set_To_Memorypalace_Locations_And_Numbers_Form(initial={'assigned_memory_palace_first': assigned_memory_palace_proposed_first,'assigned_memory_palace_second': assigned_memory_palace_proposed_second})

    context = {
        'form': form,
        'context_week_targets': memorizable_objects_tobeassignedto_mp_locations__separate_memorypalace__week_target
#        'memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__week_target__object_list': memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__week_target__object_list,
#        'memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__workpackage_relevantinformation_tobememorized__object_list': memorizable_set_tobeassignedto_mp_locations__separate_memorypalace__workpackage_relevantinformation_tobememorized__object_list,
    }

    return render(request, 'catalog/aaa.html', context)
#aaa=assign_memorizable_set_to_memorypalace_locations_and_numbers


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}
    permission_required = 'catalog.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'catalog.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'


# Classes created for the forms challenge
class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_mark_returned'


class T_Category_TableCreate(PermissionRequiredMixin, CreateView):
    model = T_Category_Table
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class T_Category_TableUpdate(PermissionRequiredMixin, UpdateView):
    model = T_Category_Table
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class T_Category_TableDelete(PermissionRequiredMixin, DeleteView):
    model = T_Category_Table
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'