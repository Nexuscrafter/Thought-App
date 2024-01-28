# Thought-App

Overview
This is a web application built with Django, HTML, CSS, and JavaScript that allows users to post and share their thoughts. The app includes features such as user authentication, profile pictures, email reminders, and password reset functionality. PostgreSQL is used as the database to store user information and thoughts. It is deployed on render.

Features
User Authentication: Users can create accounts, log in, and log out securely.

Profile Picture: Users can upload and manage their profile pictures.

Email Reminder: Users receive email reminders for important updates or events.

Password Reset: Implemented functionality to reset the password securely.

Thought Posting: Users can post their thoughts, ideas, or updates for others to see.

Technologies Used
Django: The web framework used to build the backend and manage server-side logic.

HTML/CSS/JavaScript: Frontend technologies for creating an interactive and responsive user interface.

PostgreSQL: A powerful open-source relational database used to store user information and thoughts.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/thought-posting-app.git
cd thought-posting-app
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
python manage.py migrate
Create a superuser account:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/ to access the app.

Configuration
Make sure to configure the following settings in your settings.py file:

Email Settings: Configure email settings for email reminders and password reset.

Database Settings: Update the database configurations for PostgreSQL.

Contributing
Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and suggestions are always welcome!

License
This project is licensed under the MIT License.

