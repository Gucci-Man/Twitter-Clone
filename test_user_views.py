"""User View tests."""

# run these tests like:
#
#    FLASK_ENV=production python3 -m unittest test_user_views.py


import os
from unittest import TestCase

from models import db, connect_db, Message, User

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)

        db.session.commit()

    def tearDown(self):
        """Clean up fouled transactions"""

        db.session.rollback()

    def test_add_user(self):
        """Test to create a new user"""

        with self.client as c:
            with c.session_transaction() as sess:
                
                resp = c.post('/signup', data={'username':"testuser1",
                                    'email':"test1@test.com",
                                    'password':"testuser1",
                                    'image_url':None}, follow_redirects=True)

                # Response after creating new user should be good
                self.assertEqual(resp.status_code, 200)

                # Assert that newly created user is in database
                user = User.query.filter(User.username=='testuser1').first()
                self.assertEqual(user.username, "testuser1")


    