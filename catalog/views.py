from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre, T_Calendar, T_Conflict, T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt, T_Information_Item_Tobeoperationalized, T_Memorization_Package_Memory_Palace_Or_Cards_Technique, T_Memory_Palace_Type, T_Memory_Palace_Type_Location, T_Memory_Palace_Type_Location_Packageassignment_Timeseries, T_Memory_Palace_Type_Location_Number, T_Memory_Palace_Type_Location_Daytime


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


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


class T_CalendarListView(generic.ListView):
    """Generic class-based view for a list of t_calendars."""
    model = T_Calendar
    paginate_by = 10


class T_CalendarDetailView(generic.DetailView):
    """Generic class-based detail view for a t_calendar."""
    model = T_Calendar


class T_ConflictListView(generic.ListView):
    """Generic class-based view for a list of t_conflicts."""
    model = T_Conflict
    paginate_by = 10


class T_ConflictDetailView(generic.DetailView):
    """Generic class-based detail view for a t_conflict."""
    model = T_Conflict


class T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtListView(generic.ListView):
    """Generic class-based view for a list of t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt."""
    model = T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt
    paginate_by = 10

class T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtDetailView(generic.DetailView):
    """Generic class-based detail view for a t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt."""
    model = T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_Strategyrefinemt


class T_Information_Item_TobeoperationalizedListView(generic.ListView):
    """Generic class-based view for a list of t_information_items_tobeoperationalized."""
    model = T_Information_Item_Tobeoperationalized
    paginate_by = 10


class T_Information_Item_TobeoperationalizedDetailView(generic.DetailView):
    """Generic class-based detail view for a t_information_item_tobeoperationalized."""
    model = T_Information_Item_Tobeoperationalized


class T_Memorization_Package_Memory_Palace_Or_Cards_TechniqueListView(generic.ListView):
    """Generic class-based view for a list of t_memorization_packages_memory_palace_or_cards_technique."""
    model = T_Memorization_Package_Memory_Palace_Or_Cards_Technique
    paginate_by = 10


class T_Memorization_Package_Memory_Palace_Or_Cards_TechniqueDetailView(generic.DetailView):
    """Generic class-based detail view for a t_memorization_package_memory_palace_or_cards_technique."""
    model = T_Memorization_Package_Memory_Palace_Or_Cards_Technique


class T_Memory_Palace_TypeListView(generic.ListView):
    """Generic class-based view for a list of t_memory_palaces_type."""
    model = T_Memory_Palace_Type
    paginate_by = 10

class T_Memory_Palace_TypeDetailView(generic.DetailView):
    """Generic class-based detail view for a t_memory_palace_type."""
    model = T_Memory_Palace_Type


class T_Memory_Palace_Type_LocationListView(generic.ListView):
    """Generic class-based view for a list of t_memory_palaces_type_location."""
    model = T_Memory_Palace_Type_Location
    paginate_by = 10

class T_Memory_Palace_Type_LocationDetailView(generic.DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location."""
    model = T_Memory_Palace_Type_Location


class T_Memory_Palace_Type_Location_Packageassignment_TimeseriesListView(generic.ListView):
    """Generic class-based view for a list of t_memory_palaces_type_location."""
    model = T_Memory_Palace_Type_Location_Packageassignment_Timeseries
    paginate_by = 10

class T_Memory_Palace_Type_Location_Packageassignment_TimeseriesDetailView(generic.DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location_packageassignment_timeseries."""
    model = T_Memory_Palace_Type_Location_Packageassignment_Timeseries


class T_Memory_Palace_Type_Location_NumberListView(generic.ListView):
    """Generic class-based view for a list of t_memory_palace_type_location_number."""
    model = T_Memory_Palace_Type_Location_Number
    paginate_by = 10

class T_Memory_Palace_Type_Location_NumberDetailView(generic.DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location_number."""
    model = T_Memory_Palace_Type_Location_Number


class T_Memory_Palace_Type_Location_DaytimeListView(generic.ListView):
    """Generic class-based view for a list of t_memory_palaces_type_location_daytime."""
    model = T_Memory_Palace_Type_Location_Daytime
    paginate_by = 10

class T_Memory_Palace_Type_Location_DaytimeDetailView(generic.DetailView):
    """Generic class-based detail view for a t_memory_palace_type_location_daytime."""
    model = T_Memory_Palace_Type_Location_Daytime



from django.contrib.auth.mixins import LoginRequiredMixin


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
