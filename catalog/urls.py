from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
    path('t_calendars/', views.T_CalendarListView.as_view(), name='t_calendars'),
    path('t_calendar/<int:pk>', views.T_CalendarDetailView.as_view(), name='t_calendar-detail'),
    path('t_conflicts/', views.T_ConflictListView.as_view(), name='t_conflicts'),
    path('t_conflict/<int:pk>', views.T_ConflictDetailView.as_view(), name='t_conflict-detail'),
    path('t_information_items_tobeoperationalized/', views.T_Information_Item_TobeoperationalizedListView.as_view(), name='t_information_items_tobeoperationalized'),
    path('t_information_item_tobeoperationalized/<int:pk>', views.T_Information_Item_TobeoperationalizedDetailView.as_view(), name='t_information_item_tobeoperationalized-detail'),
]


urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]
