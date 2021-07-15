from unittest.mock import call, patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

# https://github.com/django/django/blob/11b8c30b9e02ef6ecb996ad3280979dfeab700fa/django/db/utils.py#L195
# https://stackoverflow.com/questions/52621819/django-unit-test-wait-for-database


class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        """TEST waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')

            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ TEST waiting for db """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # Side effect
            gi.side_effect = [OperationalError]*5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
