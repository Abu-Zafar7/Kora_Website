# Kora - A Q&A Platform

Kora is a question-and-answer platform built with Django, inspired by Quora. It allows users to ask questions, provide answers, and engage with content through upvotes and downvotes.

## Features

- **User Authentication**
  - User registration and login
  - Secure password handling
  - User profiles

- **Question Management**
  - Ask questions with titles and content
  - Upload images with questions
  - View all questions on the home page
  - Question detail pages

- **Answer System**
  - Answer questions
  - View all answers for a question
  - Upvote and downvote answers
  - Real-time vote count updates

- **UI/UX**
  - Responsive design using Bootstrap
  - Clean and modern interface
  - Dismissible notifications

## Prerequisites

- Python 3.x
- Django 5.x
- SQLite (default database)
- Required Python packages (see requirements.txt):
  - Django 5.2
  - Pillow 11.1.0 (for image handling)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Kora_website
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```
Kora_website/
├── kora/                 # Project settings
├── website/             # Main application
│   ├── templates/      # HTML templates
│   ├── models.py      # Database models
│   ├── views.py       # View functions
│   ├── forms.py       # Form classes
│   └── urls.py        # URL patterns
├── manage.py
└── requirements.txt
```

## Features in Detail

### User Authentication
- Users can register with username, email, and password
- Secure login system with CSRF protection
- User session management

### Questions
- Create questions with titles and content
- Support for image uploads
- Questions are displayed in reverse chronological order

### Answers
- Answer questions with rich text content
- Real-time upvote/downvote system
- Vote counts update without page refresh
- Answers are displayed in reverse chronological order

### UI Features
- Responsive navigation bar
- Bootstrap-styled forms and cards
- Dismissible success/error messages
- Clean and intuitive interface

## Acknowledgments

- Django framework
- Bootstrap for styling
- jQuery for AJAX functionality

## Screenshots of the working app

![Screenshot (120)](https://github.com/user-attachments/assets/b861e28e-f59f-43c8-aa3f-3ccee0da17db)

![Screenshot (121)](https://github.com/user-attachments/assets/29d6bec1-d191-49f3-9a95-929eb9d5fcf9)

![Screenshot (122)](https://github.com/user-attachments/assets/d27b9e2d-f0b7-48c8-ae60-37aae845f631)

![Screenshot (123)](https://github.com/user-attachments/assets/abe91646-f34e-4648-90f7-1c271cf1985f)

![Screenshot (124)](https://github.com/user-attachments/assets/d0b41b5a-9af2-4e60-bfdb-e0c2c1149e1c)

![Screenshot (126)](https://github.com/user-attachments/assets/55e0d81c-192d-4fa4-89bb-43d830953530)

![Screenshot (127)](https://github.com/user-attachments/assets/00ce86e8-618b-4295-90a3-d4381cabb827)

