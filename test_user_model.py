"""User model tests."""

# run these tests like:
#
#    python3 -m unittest test_user_model.py


import os
from unittest import TestCase
from flask_bcrypt import Bcrypt
from models import db, User, Message, Follows

bcrypt = Bcrypt()

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """Clean up fouled transactions"""

        db.session.rollback()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_repr_method(self):
        """Testing repr method"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        actual_repr = repr(u)
        expected_repr = f'<User #{u.id}: testuser, test@test.com>'
        self.assertEqual(actual_repr, expected_repr)

    def test_is_following(self):
        """Test if user1 following user2 """

        user1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD1"
        )

        user2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2"
        )

        db.session.add_all([user1, user2])
        db.session.commit()

        user1.following.append(user2)
        db.session.commit()

        # user1 should following user2
        self.assertIn(user2, user1.following)

    def test_is_followed_by(self):
        """Test if user2 is not following user1"""

        user1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD1"
        )

        user2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2"
        )

        db.session.add_all([user1, user2])
        db.session.commit()

        # user2 should not be following user1
        self.assertNotIn(user1, user2.following)

    def test_authenticate(self):
        """Test if authentication is succesful"""

        # encrypt password 
        password="HASHED_PASSWORD"
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        u = User(
            email="test@test.com",
            username="testuser",
            password=hashed_pwd
        )

        db.session.add(u)
        db.session.commit()

        authenticated_user = User.authenticate("testuser", "HASHED_PASSWORD")

        # authentication should pass meaning user will be returned
        self.assertIs(u, authenticated_user)


