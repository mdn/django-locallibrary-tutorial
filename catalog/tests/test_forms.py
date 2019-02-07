from django.test import TestCase

# Create your tests here.

import datetime
from catalog.forms import RenewBookForm


class RenewBookFormTest(TestCase):

    def test_renew_form_date_in_past(self):
        """Test form is invalid if renewal_date is before today."""
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        """Test form is invalid if renewal_date more than 4 weeks from today."""
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        """Test form is valid if renewal_date is today."""
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        """Test form is valid if renewal_date is within 4 weeks."""
        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_field_label(self):
        """Test renewal_date label is 'renewal date'."""
        form = RenewBookForm()
        self.assertTrue(
            form.fields['renewal_date'].label is None or
            form.fields['renewal_date'].label == 'renewal date')

    def test_renew_form_date_field_help_text(self):
        """Test renewal_date help_text is as expected."""
        form = RenewBookForm()
        self.assertEqual(
            form.fields['renewal_date'].help_text,
            'Enter a date between now and 4 weeks (default 3).')
