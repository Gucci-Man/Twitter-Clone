"""Message model tests."""

# run these tests like:
#
#    python3 -m unittest test_message_model.py


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

class MessageModelTestCase(TestCase):
    """Test Message model"""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """Clean up fouled transactions"""

        db.session.rollback()

    def test_message_model(self):
        """Test creating new message"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        m = Message(
            text='test message',
            user_id=u.id
        )

        db.session.add(m)
        db.session.commit()

        # User should contain message
        self.assertIn(m, u.messages)

    def test_show_message(self):
        """Test showing message contents"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        m = Message(
            text='test message',
            user_id=u.id
        )

        db.session.add(m)
        db.session.commit()

        # message content should be the same from user
        self.assertEqual('test message', u.messages[0].text)

    def test_delete_message(self):
        """Test deleting a message"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        m = Message(
            text='test message',
            user_id=u.id
        )

        db.session.add(m)
        db.session.commit()

        # delete message
        db.session.delete(m)
        db.session.commit()

        # user should have no messages
        self.assertTrue(len(u.messages) == 0)
        