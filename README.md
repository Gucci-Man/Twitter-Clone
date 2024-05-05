# Warbler

## Created by Adel Ngo

### Description

**Deployed Link**: https://gothamcloud.onrender.com/

This is a Twitter clone web app called Warbler. Built with Python and Flask using data from a local database with PostgreSQL. 

#### Welcome Page:
![welcome page](/pics/welcome_page.png)

#### Main Page:
![main page](/pics/main_page.png)

#### User Profile:
![user page](/pics/profile.png)

## Features

- **Creating new users:** Users can create new accounts with a unique username, password and optional profile picture. Returning users are able to log back in.

- **Creating posts and main page**: Users may create Twitter like messages (posts) and may edit and delete them. Posts are composed of a the author, message and time stamp. Logged in users have access to the main page where they may see other user's posts and 'like' them.

- **Followers/Following:** Users may gain followers from other users while also being able to follow other accounts as well. This will reflect on their profiles. 

- **User profiles:** User's have a profile page that displays information about them such as a bio, followers, accounts followed and their messages. Users may edit and delete their profile.

- **Restricted Access**: Only logged in users have access to the web app. A user cannot edit or delete another user's profile.

- **Search Bar:** Users may search for other users by searching their partial or full usernames.

## Technology Stack

- **Python, HTML, and CSS**
- **PostgreSQL**
- **Bootstrap**
- **Flask**
- **SQLAlchemy**
- **WTForms**
- **Bcrypt**
- **Jinja**
