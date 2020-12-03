import datetime
from django.utils import timezone
from catalog.models import Author, Book, BookInstance, Genre, Language
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time

class TestBorrowed(FunctionalTest):

    def setUp(self):
        super().setUp()

        self.admin = {
            'username': 'admin', 
            'password': '1X<ISRUkw+tuK',
            'is_staff': True,
            'is_active' : True,
            'is_superuser' : True,
        }

        self.user = {
            'username': 'testuser', 
            'password': '1X<ISRUkw+tuK',
        }

        User.objects.create_user(**self.admin).save()
        User.objects.create_user(**self.user).save()

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        # Create a book
        test_author = Author.objects.create(first_name='John', last_name='Smith')
        test_genre = Genre.objects.create(name='Fantasy')
        test_language = Language.objects.create(name='English')
        test_book = Book.objects.create(
            title='Book Title',
            summary='My book summary',
            isbn='ABCDEFG',
            author=test_author,
            language=test_language,
        )
        # Create genre as a post-step
        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(genre_objects_for_book)
        test_book.save()

        # Create 30 BookInstance objects
        number_of_book_copies = 30
        for book_copy in range(number_of_book_copies):
            return_date = timezone.now() + datetime.timedelta(days=book_copy % 5)
            if book_copy % 2:
                the_borrower = test_user1
            else:
                the_borrower = test_user2
            status = 'o'
            BookInstance.objects.create(book=test_book, imprint='Unlikely Imprint, 2016', due_back=return_date,
                                        borrower=the_borrower, status=status)


    def login(self, user):
        self.browser.get(self.live_server_url + "/catalog/borrowed/")
        username = self.browser.find_element_by_css_selector('input[name=username]')
        password = self.browser.find_element_by_css_selector('input[name=password]')
        submit = self.browser.find_element_by_css_selector('input[type=submit]')

        username.send_keys(user['username'])
        password.send_keys(user['password'])
        submit.send_keys(Keys.ENTER)
        time.sleep(1)

    def test_borrowed_user(self):
        self.login(self.user)
        self.assertEqual(self.browser.title, '403 Forbidden')


    def test_borrowed_admin(self):
        self.login(self.admin)
        self.assertEqual(self.browser.title, 'Local Library')

        lis = self.browser.find_elements_by_css_selector('div.col-sm-10 ul li')
        self.assertEqual(len(lis), 10)

        for li in lis[:10]:
            hrefs = li.find_elements_by_tag_name('a')
            if len(hrefs) > 0:
                href = hrefs[0]
                self.assertEqual(href.text, "Book Title")
