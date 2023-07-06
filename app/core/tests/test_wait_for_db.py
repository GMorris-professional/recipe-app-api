"""
Tests for Core Commands
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psychopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError as OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Tests commands."""

    def test_wait_for_db_ready(self, patched_check):
        """ Test that the application does \
         not wait for the DB when the DB is ready"""
        patched_check.return_value = True
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=["default"])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """ Test that the application waits for DB when \
        getting OperationalError"""
        patched_check.side_effect = [Psychopg2Error] * 2 + \
                                    [OperationalError] * 3 + \
                                    [True]
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=["default"])
