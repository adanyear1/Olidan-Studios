"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 301)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 301)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 301)

    def test_gallery(self):
        """Tests the about page."""
        response = self.client.get('/gallery')
        self.assertContains(response, 'Gallery', 3, 301)

    def test_guests(self):
        """Tests the about page."""
        response = self.client.get('/guests')
        self.assertContains(response, 'Guests', 3, 301)

    def test_media(self):
        """Tests the about page."""
        response = self.client.get('/episodes')
        self.assertContains(response, 'Media', 3, 301)



