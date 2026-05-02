# Focused Life Tracker - Complete Setup Guide

## 🎯 Project Overview
A comprehensive Django web application for tracking three key areas of life:
- **CP Tracker**: Continuous Progress tracking with streaks
- **Deen Tracker**: Spiritual/Islamic practices tracking
- **Study Tracker**: Academic and self-study progress tracking

## 📋 Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git (optional)

## 🚀 Complete Setup Instructions

### Step 1: Navigate to Project Directory
```bash
cd /home/osama-bin/Focus-progress-tracker
```

### Step 2: Create Virtual Environment
```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Database and Run Migrations
```bash
# Create database and tables
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### Step 5: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000**

## 🔐 Admin Access
- Admin URL: http://127.0.0.1:8000/admin
- Use the credentials created with `createsuperuser` command

## 📱 Features

### CP Tracker
- Track continuous progress across different categories
- Mark entries as complete
- Progress percentage tracking
- Streak management (current and longest streaks)
- Category filtering (Exercise, Diet, Sleep, Meditation, Reading, Goal, Other)

### Deen Tracker
- Record Islamic activities (Salah, Quran, Dhikr, Dua, Charity, Knowledge)
- Add personal reflections for each activity
- Track daily and weekly spiritual goals
- Activity statistics dashboard

### Study Tracker
- Create custom subjects with colors
- Log study sessions with topics and notes
- Track study duration
- Difficulty levels (Easy, Medium, Hard)
- Self-rating system (1-5 stars)
- Daily and weekly study goals
- Subject-based organization

### User Management
- User registration and authentication
- User profiles with bio
- Session management
- Secure login/logout

## 🎨 Frontend
- Responsive design using Tailwind CSS (via CDN)
- Mobile-friendly interface
- Modern, clean UI
- Intuitive navigation

## 📊 Database
- SQLite (default Django database)
- Located at `db.sqlite3` in project root
- Auto-created during migration

## 🔧 Project Structure
```
focused-life-tracker/
├── manage.py
├── requirements.txt
├── db.sqlite3 (auto-created)
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   ├── dashboard/
│   ├── cp_tracker/
│   ├── deen_tracker/
│   └── study_tracker/
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── auth/
    ├── cp_tracker/
    ├── deen_tracker/
    └── study_tracker/
```

## 🌐 URL Routes
- `/` - Dashboard (requires login)
- `/auth/register/` - User registration
- `/auth/login/` - User login
- `/auth/logout/` - User logout
- `/auth/profile/` - User profile
- `/cp/` - CP Tracker list
- `/cp/create/` - Create CP entry
- `/deen/` - Deen Tracker dashboard
- `/deen/create/` - Create Deen entry
- `/study/` - Study Tracker dashboard
- `/study/create/` - Create Study entry
- `/admin/` - Django admin panel

## 💡 Usage Tips

### For CP Tracker
1. Create an entry with a category and title
2. Update progress percentage as you work
3. Mark as complete when finished
4. View streak statistics to maintain motivation

### For Deen Tracker
1. Set your daily and weekly spiritual goals
2. Log each Islamic activity with reflection
3. Track different types of worship
4. Review your activity statistics

### For Study Tracker
1. Create subjects for your study areas
2. Assign colors to each subject
3. Log study sessions with topics and difficulty
4. Rate your study sessions
5. Set daily/weekly study targets

## 🐛 Troubleshooting

### Database Issues
```bash
# Reset database (WARNING: deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Port Already in Use
```bash
# Run on different port
python manage.py runserver 8001
```

### Static Files Issues
```bash
# Collect static files
python manage.py collectstatic --noinput
```

## 📝 Notes
- All timestamps are auto-generated
- User data is completely isolated (each user sees only their own data)
- The app uses Django's built-in authentication
- Sessions expire at browser close (configurable in settings)

## 🚀 Deployment
For production deployment:
1. Set `DEBUG = False` in `config/settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Change `SECRET_KEY` to a secure value
4. Use a production database (PostgreSQL recommended)
5. Serve static files through a web server (Nginx/Apache)

## 📞 Support
For issues or questions, check Django documentation at https://docs.djangoproject.com/
