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
│   ├── static/        # Static files
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
![Screenshot (120)](https://github.com/user-attachments/assets/80fc4a90-40d6-4ab7-a2be-cea8df8df3c2)

![Screenshot (121)](https://github.com/user-attachments/assets/29804dea-1abc-482e-aaab-e15abdd2efac)

![Screenshot (122)](https://github.com/user-attachments/assets/9e062bd7-f7c6-40c8-b280-e1e55b309f61)

![Screenshot (123)](https://github.com/user-attachments/assets/b12526a0-d5a4-4f81-8275-e265b241c641)

![Screenshot (124)](https://github.com/user-attachments/assets/31c457ce-4ab0-4524-82ea-17a3f5f65616)

![Screenshot (126)](https://github.com/user-attachments/assets/8e262c85-02f3-4ac4-b2b6-10bc77ac3d7d)

![Screenshot (127)](https://github.com/user-attachments/assets/b244a654-afc0-4900-993f-259201d3a708)


