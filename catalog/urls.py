from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('bookinstance/<int:pk>', views.BookInstanceDetailView.as_view(), name='bookinstance-detail'),
    path('t_workpackages_actual_duration_timeseries/', views.T_Workpackage_Actual_Duration_TimeseriesListView.as_view(), name='t_workpackages_actual_duration_timeseries'),
    path('t_workpackage_actual_duration_timeseries/<int:pk>', views.T_Workpackage_Actual_Duration_TimeseriesDetailView.as_view(), name='t_workpackage_actual_duration_timeseries-detail'),
    path('t_memorization_package_mp_technique_assignmenttype_categorys/', views.T_Memorization_Package_MP_Technique_Assignmenttype_CategoryListView.as_view(), name='t_memorization_package_mp_technique_assignmenttype_categorys'),
    path('t_memorization_package_mp_technique_assignmenttype_category/<int:pk>', views.T_Memorization_Package_MP_Technique_Assignmenttype_CategoryDetailView.as_view(), name='t_memorization_package_mp_technique_assignmenttype_category-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
    path('t_calendars/', views.T_CalendarListView.as_view(), name='t_calendars'),
    path('t_calendar/<int:pk>', views.T_CalendarDetailView.as_view(), name='t_calendar-detail'),
    path('t_wt_is_excluded_from_dt_mp_assignment_on_weekdays_timeseries/', views.T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_TimeseriesListView.as_view(), name='t_wt_is_excluded_from_dt_mp_assignment_on_weekdays_timeseries'),
    path('t_wt_is_excluded_from_dt_mp_assignment_on_weekday_timeseries/<int:pk>', views.T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_TimeseriesDetailView.as_view(), name='t_wt_is_excluded_from_dt_mp_assignment_on_weekday_timeseries-detail'),
    path('t_day_targets_sequence_timeseries/', views.T_Day_Target_Sequence_TimeseriesListView.as_view(), name='t_day_targets_sequence_timeseries'),
    path('t_day_target_sequence_timeseries/<int:pk>', views.T_Day_Target_Sequence_TimeseriesDetailView.as_view(), name='t_day_target_sequence_timeseries-detail'),
    path('t_conflicts/', views.T_ConflictListView.as_view(), name='t_conflicts'),
    path('t_conflict/<int:pk>', views.T_ConflictDetailView.as_view(), name='t_conflict-detail'),
    path('t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemts/', views.T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtListView.as_view(), name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemts'),
    path('t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt/<int:pk>', views.T_Ausatemmuskulatur_Isnot_Entspannt_Dueto_StrategyrefinemtDetailView.as_view(), name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt-detail'),
    path('t_ausatemmuskulatur_strategyrefinement_conflict_phases/', views.T_Ausatemmuskulatur_Strategyrefinement_Conflict_PhaseListView.as_view(), name='t_ausatemmuskulatur_strategyrefinement_conflict_phases'),
    path('t_ausatemmuskulatur_strategyrefinement_conflict_phase/<int:pk>', views.T_Ausatemmuskulatur_Strategyrefinement_Conflict_PhaseDetailView.as_view(), name='t_ausatemmuskulatur_strategyrefinement_conflict_phase-detail'),
    path('t_conflict_strategy_categorys/', views.T_Conflict_Strategy_CategoryListView.as_view(), name='t_conflict_strategy_categorys'),
    path('t_conflict_strategy_category/<int:pk>', views.T_Conflict_Strategy_CategoryDetailView.as_view(), name='t_conflict_strategy_category-detail'),
    path('t_conflict_strategy_category_measures/', views.T_Conflict_Strategy_Category_MeasureListView.as_view(), name='t_conflict_strategy_category_measures'),
    path('t_conflict_strategy_category_measure/<int:pk>', views.T_Conflict_Strategy_Category_MeasureDetailView.as_view(), name='t_conflict_strategy_category_measure-detail'),
    path('t_information_items_tobeoperationalized/', views.T_Information_Item_TobeoperationalizedListView.as_view(), name='t_information_items_tobeoperationalized'),
    path('t_information_item_tobeoperationalized/<int:pk>', views.T_Information_Item_TobeoperationalizedDetailView.as_view(), name='t_information_item_tobeoperationalized-detail'),
    path('t_information_items_tobeoperationalized_memor_timeseries/', views.T_Information_Item_Tobeoperationalized_Memor_TimeseriesListView.as_view(), name='t_information_items_tobeoperationalized_memor_timeseries'),
    path('t_information_item_tobeoperationalized_memor_timeseries/<int:pk>', views.T_Information_Item_Tobeoperationalized_Memor_TimeseriesDetailView.as_view(), name='t_information_item_tobeoperationalized_memor_timeseries-detail'),
    path('t_information_items_tobeoperationalized_memor_timeseries_act/', views.T_Information_Item_Tobeoperationalized_Memor_Timeseries_ActListView.as_view(), name='t_information_items_tobeoperationalized_memor_timeseries_act'),
    path('t_information_item_tobeoperationalized_memor_timeseries_act/<int:pk>', views.T_Information_Item_Tobeoperationalized_Memor_Timeseries_ActDetailView.as_view(), name='t_information_item_tobeoperationalized_memor_timeseries_act-detail'),
    path('t_category_tables/', views.T_Category_TableListView.as_view(), name='t_category_tables'),
    path('t_category_table/<int:pk>', views.T_Category_TableDetailView.as_view(), name='t_category_table-detail'),
    path('t_category_table_entries/', views.T_Category_Table_EntryListView.as_view(), name='t_category_table_entries'),
    path('t_category_table_entry/<int:pk>', views.T_Category_Table_EntryDetailView.as_view(), name='t_category_table_entry-detail'),
    path('t_category_table_predicates_asverb/', views.T_Category_Table_Predicate_AsverbListView.as_view(), name='t_category_table_predicates_asverb'),
    path('t_category_table_predicate_asverb/<int:pk>', views.T_Category_Table_Predicate_AsverbDetailView.as_view(), name='t_category_table_predicate_asverb-detail'),
    path('t_categorys_timeseries/', views.T_Category_TimeseriesListView.as_view(), name='t_categorys_timeseries'),
    path('t_category_timeseries/<int:pk>', views.T_Category_TimeseriesDetailView.as_view(), name='t_category_timeseries-detail'),
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
    path('t_memory_palaces_or_cards_memorization_timeseries/', views.T_Memory_Palace_Or_Cards_Memorization_TimeseriesListView.as_view(), name='t_memory_palaces_or_cards_memorization_timeseries'),
    path('t_memory_palace_or_cards_memorization_timeseries/<int:pk>', views.T_Memory_Palace_Or_Cards_Memorization_TimeseriesDetailView.as_view(), name='t_memory_palace_or_cards_memorization_timeseries-detail'),
    path('t_memory_palace_or_cards_memorization_timeseries_actions/', views.T_Memory_Palace_Or_Cards_Memorization_Timeseries_ActionListView.as_view(), name='t_memory_palace_or_cards_memorization_timeseries_actions'),
    path('t_memory_palace_or_cards_memorization_timeseries_action/<int:pk>', views.T_Memory_Palace_Or_Cards_Memorization_Timeseries_ActionDetailView.as_view(), name='t_memory_palace_or_cards_memorization_timeseries_action-detail'),
]


urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<int:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
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
    path('book/<int:pk>/create/', views.book_create_proposed_week_target, name='book-create-proposed-week-target'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

# Add URLConf to create bookinstances
urlpatterns += [
    path('bookinstance/<int:pk>/create/', views.bookinstance_create_proposed_workpackage, name='bookinstance-create-proposed-workpackage'),
]

#Assign memorizables to memory palaces:
# Add URLConf to assign bookinstances to memorypalace location and number for specific workpackage
urlpatterns += [
    path('bookinstance/<int:pk>/assign/', views.book_bookinstance_assign_memorypalace_location_and_number_for_specific_workpackage, name='book-bookinstance-assign-memorypalace-location-and-number-for-specific-workpackage'),
]
# Add URLConf to assign week_targets to memorypalace location and numbers
urlpatterns += [
    path('week_target/<int:pk>/assign/', views.assign_memorizables_to_mp_locations_and_numbers_week_target_fixed_category, name='assign-memorizables-to-mp-locations-and-numbers-week-target-fixed-category'),
]
# Add URLConf to assign relevant_information_tobememorized to memorypalace location and numbers
urlpatterns += [
    path('workpackage_relevantinformation/<int:pk>/assign/', views.assign_memorizables_to_mp_locations_and_numbers_workpackage_relevantinformation_tobememorized_fixed_category, name='assign-memorizables-to-mp-locations-and-numbers-workpackage-relevantinformation-tobememorized-fixed-category'),
]

#Change memorization sequences:
# URLConf to change memorization sequence of week_targets
urlpatterns += [
    path('week_target/<int:pk>/sequence/', views.change_memorization_sequence_week_targets_fixed_category, name='change-memorization-sequence-week-targets-fixed-category'),
]
# URLConf to change memorization sequence of relevantinformation_tobememorized
urlpatterns += [
    path('relevantinformation_tobememorized/<int:pk>/sequence/', views.change_memorization_sequence_workpackage_relevantinformation_tobememorized_fixed_category, name='change-memorization-sequence-workpackage-relevantinformation-tobememorized-fixed-category'),
]

#Memorize:
# URLConf to memorize week_targets
urlpatterns += [
    path('week_target/<int:pk>/memorization/', views.memorize_week_targets_fixed_category_list, name='memorize-week-targets-fixed-category-list'),
#    path('week_target/<int:pk>/memorize/<int:pkwt>', views.memorize_week_targets_fixed_category_memorycard, name='memorize-week-targets-fixed-category-memorycard'),
]
# URLConf to memorize relevantinformation_tobememorized
urlpatterns += [
#    path('relevantinformation_tobememorized/<int:pk>/memorization/', views.memorize_workpackage_relevantinformation_tobememorized_fixed_category_list, name='memorize-workpackage-relevantinformation-tobememorized-fixed-category-list'),
#    path('relevantinformation_tobememorized/<int:pk>/memorize/<int:pkwt>', views.memorize_workpackage_relevantinformation_tobememorized_fixed_category_memorycard, name='memorize-workpackage-relevantinformation-tobememorized-fixed-category-memorycard'),
]


# Add URLConf to create, update, and delete t_category_tables
urlpatterns += [
    path('t_category_table/create/', views.T_Category_TableCreate.as_view(), name='t_category_table_create'),
    path('t_category_table/<int:pk>/update/', views.T_Category_TableUpdate.as_view(), name='t_category_table_update'),
    path('t_category_table/<int:pk>/delete/', views.T_Category_TableDelete.as_view(), name='t_category_table_delete'),
]
