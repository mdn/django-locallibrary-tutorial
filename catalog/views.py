from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Book, T_Workpackage_Actual_Duration_Timeseries, Author, T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_Timeseries, T_Day_Target_Sequence_Timeseries, BookInstance, Genre, T_Calendar, T_Conflict, T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt, T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase, T_Conflict_Strategy_Category, T_Conflict_Strategy_Category_Measure, T_Information_Item_Tobeoperationalized, T_Information_Item_Tobeoperationalized_Memor_Timeseries, T_Information_Item_Tobeoperationalized_Memor_Timeseries_Act, T_Category_Table, T_Category_Table_Predicate_Asverb, T_Category_Table_Entry, T_Category_Timeseries, T_Memorization_Package_Memory_Palace_Or_Cards_Technique, T_Memory_Palace_Type, T_Memory_Palace_Type_Location, T_Memory_Palace_Type_Location_Packageassignment_Timeseries, T_Memory_Palace_Type_Location_Number, T_Memory_Palace_Type_Location_Daytime, T_Memory_Palace_Or_Cards_Memorization_Timeseries, T_Memory_Palace_Or_Cards_Memorization_Timeseries_Action


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


class T_Workpackage_Actual_Duration_TimeseriesListView(LoginRequiredMixin, generic .ListView):
    """Generic class-based view for a list of t_workpackages_actual_duration_timeseries."""
    model = T_Workpackage_Actual_Duration_Timeseries
    paginate_by = 10

class T_Workpackage_Actual_Duration_TimeseriesDetailView(LoginRequiredMixin, generic .DetailView):
    """Generic class-based detail view for a t_workpackage_actual_duration_timeseries."""
    model = T_Workpackage_Actual_Duration_Timeseries


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

# from .forms import RenewBookForm
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
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


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
