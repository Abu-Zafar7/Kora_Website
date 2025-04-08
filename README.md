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

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django framework
- Bootstrap for styling
- jQuery for AJAX functionality