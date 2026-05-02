# 📚 Documentation Quick Reference

## You Now Have 2 Main Files

### 1. **PROJECT_GUIDE.md**
**Everything about the project itself**
- What is Focused Life Tracker?
- 5 Django apps explained
- 9 database models
- All features (CP, Deen, Study trackers)
- Project architecture
- Technology stack
- Security features
- FAQ

**Read this to:** Understand what the project does and how it works

---

### 2. **DEPLOYMENT_UPDATE_GUIDE.md**
**How to deploy and update your project**
- 7 free deployment options compared
- Step-by-step Railway.app deployment
- How to update code (3 methods)
- How to update database models
- Backup & recovery procedures
- Troubleshooting guide
- Deployment checklist

**Read this to:** Deploy your app online or make changes

---

## 🚀 Quick Start: Deploy in 10 Minutes

### Option 1: Railway.app (Recommended)
```bash
# 1. Add gunicorn to requirements
pip install gunicorn
pip freeze > requirements.txt

# 2. Create Procfile
echo "web: gunicorn config.wsgi" > Procfile

# 3. Create runtime.txt
echo "python-3.12.3" > runtime.txt

# 4. Push to GitHub
git add .
git commit -m "Deploy setup"
git push origin main

# 5. Go to Railway.app, connect GitHub repo
# 6. App deploys automatically, get your URL
```

**Done!** Your app is live at `yourdomain.railway.app`

---

### Option 2: PythonAnywhere (Simpler)
1. Go to https://www.pythonanywhere.com
2. Upload your code or clone from GitHub
3. Configure Django app
4. Click reload
5. Your app is at `username.pythonanywhere.com`

---

## 📝 How to Update Code

### Method A: Via GitHub (Auto-Deploy)
```bash
cd /project
# Make your changes
git add .
git commit -m "Your change"
git push origin main
# Done! Platform auto-deploys in 2-3 minutes
```

### Method B: Direct SSH (VPS)
```bash
ssh user@server
cd /project
git pull origin main
python manage.py migrate
# Restart your server
```

---

## 🗄️ How to Update Database

### Add New Field
```python
# Edit model: apps/tracker/models.py
class CPEntry(models.Model):
    new_field = models.CharField(max_length=255, default='')  # Add this
```

```bash
python manage.py makemigrations
python manage.py migrate
git add .
git push origin main
# Auto-deployed and database updated
```

### Rename Field
```bash
python manage.py makemigrations
# Django asks: "Did you rename old_field to new_field?" → y (yes)
python manage.py migrate
git push origin main
```

---

## 💾 Backup Your Data

### Local Backup
```bash
cp db.sqlite3 db.sqlite3.backup.$(date +%Y%m%d_%H%M%S)
```

### Remote Backup (PythonAnywhere)
- SSH console: `cp db.sqlite3 ~/backup.sqlite3`
- Download from Files tab

### Restore
```bash
cp db.sqlite3.backup.YYYYMMDD db.sqlite3
python manage.py runserver
```

---

## 🔧 Running Locally

```bash
cd /home/osama-bin/Focus-progress-tracker
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

Access at: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin/

---

## 🎯 Files Structure

```
Your Project/
├── PROJECT_GUIDE.md              ← Read: What is this project?
├── DEPLOYMENT_UPDATE_GUIDE.md    ← Read: How to deploy & update?
├── README.md                     ← Project overview
├── requirements.txt              ← Dependencies (Django, etc)
├── Procfile                      ← Deployment config
├── manage.py                     ← Django CLI
├── config/                       ← Django settings
├── apps/                         ← 5 apps (users, dashboard, cp_tracker, deen_tracker, study_tracker)
├── templates/                    ← 25 HTML templates
└── db.sqlite3                    ← Your database (local)
```

---

## 📊 All 5 Apps at a Glance

| App | Purpose | Models |
|-----|---------|--------|
| **users** | Authentication, profiles | User, UserProfile |
| **dashboard** | Main overview page | - |
| **cp_tracker** | Continuous progress daily habits | CPEntry, CPStreak |
| **deen_tracker** | Islamic practices tracking | DeenEntry, DeenGoal |
| **study_tracker** | Study session logging | Subject, StudyEntry, StudyGoal |

---

## 🔐 Default Login

```
Username: admin
Password: Password123
```

**Create users at:** http://127.0.0.1:8000/auth/register/

---

## ❓ Answers to Common Questions

**Q: How do I change something?**  
A: Edit the file, push to GitHub, done. See DEPLOYMENT_UPDATE_GUIDE.md

**Q: How do I add a new feature?**  
A: Edit model → makemigrations → migrate → push. See "How to Update Database" above

**Q: How do I backup my data?**  
A: `cp db.sqlite3 db.sqlite3.backup` - See "Backup Your Data" above

**Q: Can I host this for free?**  
A: Yes! Railway, PythonAnywhere, Render all have free tiers. See DEPLOYMENT_UPDATE_GUIDE.md

**Q: How do I reset my password?**  
A: `python manage.py changepassword admin`

**Q: Can multiple people use this?**  
A: Yes! Each person creates account at /auth/register/

---

## 📞 Need More Help?

- **For project info:** Read `PROJECT_GUIDE.md`
- **For deployment/updates:** Read `DEPLOYMENT_UPDATE_GUIDE.md`
- **Django docs:** https://docs.djangoproject.com/
- **Railway docs:** https://docs.railway.app/
- **PythonAnywhere docs:** https://help.pythonanywhere.com/

---

## ✅ Status

| Component | Status |
|-----------|--------|
| Server | ✅ Running |
| Database | ✅ Ready |
| Code | ✅ Clean |
| Documentation | ✅ Complete |
| Security | ✅ Verified |

---

## 🎯 Next Steps

1. **Read PROJECT_GUIDE.md** to understand your project
2. **Read DEPLOYMENT_UPDATE_GUIDE.md** to learn deployment
3. **Start using:** Go to http://127.0.0.1:8000
4. **Deploy:** Follow Railway.app steps when ready
5. **Make changes:** Edit code → push → auto-deployed

---

**Everything you need is in these 2 files!**  
**Happy coding! 🚀**
