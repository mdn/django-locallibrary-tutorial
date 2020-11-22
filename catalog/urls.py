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
    path('t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemts/', views.T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtListView.as_view(), name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemts'),
    path('t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt/<int:pk>', views.T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtDetailView.as_view(), name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt-detail'),
    path('t_ausatemmuskulatur_strategyrefinement_conflict_phases/', views.T_Ausatemmuskulatur_Strategyrefinement_Conflict_PhaseListView.as_view(), name='t_ausatemmuskulatur_strategyrefinement_conflict_phases'),
    path('t_ausatemmuskulatur_strategyrefinement_conflict_phase/<int:pk>', views.T_Ausatemmuskulatur_Strategyrefinement_Conflict_PhaseDetailView.as_view(), name='t_ausatemmuskulatur_strategyrefinement_conflict_phase-detail'),
    path('t_information_items_tobeoperationalized/', views.T_Information_Item_TobeoperationalizedListView.as_view(), name='t_information_items_tobeoperationalized'),
    path('t_information_item_tobeoperationalized/<int:pk>', views.T_Information_Item_TobeoperationalizedDetailView.as_view(), name='t_information_item_tobeoperationalized-detail'),
    path('t_memorization_package_memory_palace_or_cards_technique/', views.T_Memorization_Package_Memory_Palace_Or_Cards_TechniqueListView.as_view(), name='t_memorization_packages_memory_palace_or_cards_technique'),
    path('t_memorization_package_memory_palace_or_cards_technique/<int:pk>', views.T_Memorization_Package_Memory_Palace_Or_Cards_TechniqueDetailView.as_view(), name='t_memorization_package_memory_palace_or_cards_technique-detail'),
    path('t_memory_palace_type/', views.T_Memory_Palace_TypeListView.as_view(), name='t_memory_palaces_type'),
    path('t_memory_palace_type/<int:pk>', views.T_Memory_Palace_TypeDetailView.as_view(), name='t_memory_palace_type-detail'),
    path('t_memory_palaces_type_location/', views.T_Memory_Palace_Type_LocationListView.as_view(), name='t_memory_palaces_type_location'),
    path('t_memory_palace_type_location/<int:pk>', views.T_Memory_Palace_Type_LocationDetailView.as_view(), name='t_memory_palace_type_location-detail'),
    path('t_memory_palaces_type_location_packageassignment_timeseries/', views.T_Memory_Palace_Type_Location_Packageassignment_TimeseriesListView.as_view(), name='t_memory_palaces_type_location_packageassignment_timeseries'),
    path('t_memory_palace_type_location_packageassignment_timeseries/<int:pk>', views.T_Memory_Palace_Type_Location_Packageassignment_TimeseriesDetailView.as_view(), name='t_memory_palace_type_location_packageassignment_timeseries-detail'),
    path('t_memory_palaces_type_location_number/', views.T_Memory_Palace_Type_Location_NumberListView.as_view(), name='t_memory_palaces_type_location_number'),
    path('t_memory_palace_type_location_number/<int:pk>', views.T_Memory_Palace_Type_Location_NumberDetailView.as_view(), name='t_memory_palace_type_location_number-detail'),
    path('t_memory_palaces_type_location_daytime/', views.T_Memory_Palace_Type_Location_DaytimeListView.as_view(), name='t_memory_palaces_type_location_daytime'),
    path('t_memory_palace_type_location_daytime/<int:pk>', views.T_Memory_Palace_Type_Location_DaytimeDetailView.as_view(), name='t_memory_palace_type_location_daytime-detail'),
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
