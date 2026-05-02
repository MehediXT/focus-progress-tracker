# 🚀 Deployment & Update Guide

## 📋 Table of Contents
1. [Free Deployment Options](#free-deployment)
2. [How to Deploy](#deployment-steps)
3. [How to Update Code](#updating-code)
4. [How to Update Database](#updating-database)
5. [Backup & Recovery](#backup--recovery)
6. [Troubleshooting](#troubleshooting)

---

## 🆓 Free Deployment Options

### Option 1: **Heroku** (Easiest - Free Tier Ended, But Still Options)
- Previously free, now charges ($5/month minimum)
- Best for learning
- Automatic deploys from GitHub

### Option 2: **Railway.app** ⭐ RECOMMENDED
- **Free tier:** 500 hours/month (plenty for personal use)
- Credit card required but charges only if you exceed limits
- Django support out of box
- PostgreSQL database included
- Custom domain support
- Deploy in 5 minutes

### Option 3: **PythonAnywhere**
- **Free tier:** Limited but usable
- Easy Django deployment
- Free subdomain (example.pythonanywhere.com)
- No credit card required
- Good for learning

### Option 4: **Replit**
- **Free tier:** Full stack available
- Requires credit card for custom domain
- Can host for free with .repl.co domain
- 5-minute setup

### Option 5: **Render.com** (NEW)
- **Free tier:** 750 hours/month + PostgreSQL
- Generous free tier
- Auto-deploy from GitHub
- Good performance

### Option 6: **DigitalOcean App Platform**
- **Free tier:** $12/month free credit (lasts 2 months)
- Then ~$5/month for basic app
- Very reliable
- Great documentation

### Option 7: **Self-Hosted (VPS)**
- **Cheapest Option:** $2.50-5/month VPS
- Providers: Linode, Vultr, DigitalOcean, Hetzner
- Full control
- Steeper learning curve

---

## 🚀 Deployment Steps (Railway.app - Recommended)

### Step 1: Prepare Your Code

Create a file named `Procfile` in project root:
```
web: gunicorn config.wsgi
```

Update `requirements.txt` to include gunicorn:
```bash
cd /home/osama-bin/Focus-progress-tracker
source venv/bin/activate
pip install gunicorn
pip freeze > requirements.txt
```

Create a file named `runtime.txt`:
```
python-3.12.3
```

### Step 2: Create `.gitignore`

Create file `.gitignore` in project root:
```
venv/
*.pyc
__pycache__/
.env
db.sqlite3
.DS_Store
*.log
```

### Step 3: Initialize Git Repository

```bash
cd /home/osama-bin/Focus-progress-tracker
git init
git add .
git commit -m "Initial commit: Focused Life Tracker"
```

### Step 4: Create GitHub Repository

1. Go to https://github.com/new
2. Create repo named `focused-life-tracker`
3. Don't initialize with README
4. Copy commands shown

```bash
git remote add origin https://github.com/YOUR_USERNAME/focused-life-tracker.git
git branch -M main
git push -u origin main
```

### Step 5: Connect to Railway

1. Go to https://railway.app
2. Sign up (GitHub or email)
3. Click "New Project"
4. Select "Deploy from GitHub"
5. Authorize GitHub access
6. Select `focused-life-tracker` repo
7. Railway auto-detects Django

### Step 6: Configure Environment

In Railway dashboard, set variables:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.railway.app
DATABASE_URL=postgresql://...  # Auto-provided
```

### Step 7: Deploy

```bash
# Push to GitHub
git push origin main

# Railway auto-deploys on push
# Check railway.app dashboard
```

Get your URL from Railway dashboard (example: `myapp.railway.app`)

---

## 📝 Alternative: PythonAnywhere Deployment (Simplest)

### Step 1: Create Account
- Go to https://www.pythonanywhere.com
- Sign up free
- No credit card needed

### Step 2: Upload Code
- Use Web tab → Upload files
- Or use Git: `git clone your-repo/`

### Step 3: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.12 myapp
workon myapp
pip install -r requirements.txt
```

### Step 4: Configure Django App
- Web tab → Add new web app → Python 3.12
- Source code: `/home/username/focused-life-tracker`
- WSGI file: `/home/username/focused-life-tracker/config/wsgi.py`
- Virtual env: `/home/username/.virtualenvs/myapp`

### Step 5: Update settings.py
```python
# Add to settings.py
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
DEBUG = False
```

### Step 6: Reload
- Click "Reload" in Web tab
- Your app is live at `yourusername.pythonanywhere.com`

---

## 🔄 How to Update Code

### Method 1: Push to GitHub (Auto-Deploy)
```bash
cd /home/osama-bin/Focus-progress-tracker

# Make changes to code files
# Edit app/users/views.py or any file

# Stage changes
git add .

# Commit with message
git commit -m "Fix: Update login view"

# Push to GitHub
git push origin main

# Platform auto-deploys (wait 2-3 minutes)
```

### Method 2: Manual Update in Terminal

```bash
# SSH into server (if using VPS)
ssh user@your-server.com

# Go to project
cd /focused-life-tracker

# Pull latest from GitHub
git pull origin main

# Activate virtual environment
source venv/bin/activate

# Install any new dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files (if needed)
python manage.py collectstatic --noinput

# Restart application
# (depends on hosting platform)
```

### Method 3: Update via Web Interface (PythonAnywhere)

1. SSH console in PythonAnywhere
2. `cd /home/username/focused-life-tracker`
3. `git pull origin main`
4. `source /home/username/.virtualenvs/myapp/bin/activate`
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. Reload web app from Web tab

---

## 🗄️ How to Update Database

### Scenario 1: Add New Field to Model

```python
# Edit model in apps/tracker/models.py
class CPEntry(models.Model):
    # ... existing fields ...
    new_field = models.CharField(max_length=255, default='')  # Add this
```

### Apply Changes:

```bash
# Create migration
python manage.py makemigrations

# Apply migration locally first
python manage.py migrate

# Test locally
python manage.py runserver

# If good, push to GitHub
git add .
git commit -m "Add new_field to CPEntry"
git push origin main

# Platform auto-applies migrations
# Or manually: python manage.py migrate (on server)
```

### Scenario 2: Modify Existing Field

```python
# Old
progress = models.IntegerField(default=0)

# New - change to PositiveIntegerField
progress = models.PositiveIntegerField(default=0)
```

```bash
python manage.py makemigrations
python manage.py migrate
```

### Scenario 3: Delete a Field

```python
# Remove the line from model
# Don't just comment it

class CPEntry(models.Model):
    # Remove: old_field = models.CharField(...)
```

```bash
python manage.py makemigrations
python manage.py migrate
```

### Scenario 4: Rename a Field

```bash
# Django detects and asks
python manage.py makemigrations

# It will ask: "Did you rename CPEntry.old_field to CPEntry.new_field?"
# Answer: y (yes)

python manage.py migrate
```

---

## 💾 Backup & Recovery

### Backup Database Locally

```bash
cd /home/osama-bin/Focus-progress-tracker

# Copy database
cp db.sqlite3 db.sqlite3.backup.$(date +%Y%m%d_%H%M%S)

# Keep multiple backups
ls -la db.sqlite3.backup.*
```

### Download Database from Server (PythonAnywhere)

```bash
# In PythonAnywhere SSH
cd /home/username/focused-life-tracker
cp db.sqlite3 ~/db.backup.sqlite3

# Then download from Files tab
```

### Download from Database URL (Railway)

Railway provides PostgreSQL connection string. Use:
```bash
pg_dump postgresql://user:pass@host/dbname > backup.sql
```

### Restore Database

```bash
# Replace corrupted database
cp db.sqlite3.backup.YYYYMMDD_HHMMSS db.sqlite3

# Restart server
python manage.py runserver
```

---

## 🔄 Full Update Workflow Example

### Scenario: Add new feature to Study Tracker

**Step 1: Local Development**
```bash
cd /home/osama-bin/Focus-progress-tracker
source venv/bin/activate

# Make changes
# Edit apps/study_tracker/models.py
# Edit apps/study_tracker/views.py
# Edit apps/study_tracker/forms.py
# Edit templates/study_tracker/...

# Test locally
python manage.py runserver
# Visit http://127.0.0.1:8000
```

**Step 2: Run Django Checks**
```bash
python manage.py check
# Should say: System check identified no issues (0 silenced).
```

**Step 3: Create Migrations (if model changed)**
```bash
python manage.py makemigrations
# Creates migration files in migrations/

python manage.py migrate
# Applies to local database
```

**Step 4: Test Thoroughly**
```bash
# Test the feature manually in browser
# Test with multiple browsers/devices
# Check admin panel
# Check forms validate correctly
```

**Step 5: Git Commit**
```bash
git add .
git commit -m "Feature: Add new study tracking feature"
# Good commit messages:
# - Fix: ...
# - Feature: ...
# - Docs: ...
# - Refactor: ...
```

**Step 6: Push to GitHub**
```bash
git push origin main
```

**Step 7: Platform Deploys**
- Railway auto-deploys (~2 min)
- Visit your-app.railway.app
- Test on live server
- Check admin panel

---

## 🆘 Troubleshooting

### Problem: "No module named 'django'"
**Solution:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Problem: "ModuleNotFoundError: No module named 'apps'"
**Solution:** Remote server might not have PYTHONPATH set
```bash
# In Procfile or app config, add:
export PYTHONPATH=/app:$PYTHONPATH
```

### Problem: "Static files not loading"
**Solution:**
```bash
python manage.py collectstatic --noinput
# Then restart server
```

### Problem: "Database locked"
**Solution:**
```bash
rm db.sqlite3
python manage.py migrate
# Loses data but fixes corruption
```

### Problem: "Migrations not applying"
**Solution:**
```bash
# Check status
python manage.py showmigrations

# Apply specific migration
python manage.py migrate app_name 0001_initial

# Or reset all
python manage.py migrate --zero app_name
python manage.py migrate app_name
```

### Problem: "Import Error on Deploy"
**Solution:**
- Verify all files pushed to GitHub
- Check `requirements.txt` includes all packages
- Verify no relative imports in views.py
- Use absolute imports: `from apps.models import ...`

### Problem: "500 Error on Production"
**Solution:**
```python
# In settings.py for debugging
DEBUG = True  # Temporarily

# Check logs:
# Railway: Deployments tab → View Logs
# PythonAnywhere: Web tab → Error log
# VPS: tail -f logs/error.log
```

### Problem: "ALLOWED_HOSTS error"
**Solution:**
```python
# In settings.py
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'localhost']
```

---

## 📊 Comparison: Free Hosting Options

| Platform | Free Tier | Setup Time | Database | Python | Best For |
|----------|-----------|-----------|----------|--------|----------|
| **Railway** | 500 hrs/mo | 5 min | PostgreSQL | 3.12 | Beginners |
| **PythonAnywhere** | Limited | 10 min | SQLite/MySQL | 3.12 | Learning |
| **Replit** | Yes | 3 min | SQLite | 3.12 | Quick demos |
| **Render** | $12 credit | 8 min | PostgreSQL | 3.12 | Production |
| **VPS** ($5/mo) | No | 30 min | Any | 3.12 | Full control |

---

## 🎯 Recommended Workflow

### For Learning
1. Develop locally
2. Test thoroughly
3. Deploy to Railway.app
4. Share with others

### For Production
1. Use secure secrets management
2. Enable HTTPS (all platforms have this)
3. Set up automated backups
4. Monitor error logs
5. Update regularly

### Regular Maintenance
```bash
# Weekly
git push updates
check logs

# Monthly
update dependencies
backup database
test recovery

# Quarterly
update Django version
security patches
code review
```

---

## 📝 Deployment Checklist

Before deploying to production:

- [ ] Set `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to new random string
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Move sensitive data to environment variables
- [ ] Enable HTTPS (automatic on most platforms)
- [ ] Test all features on staging
- [ ] Set up error logging
- [ ] Plan backup strategy
- [ ] Test disaster recovery
- [ ] Monitor performance after deploy

---

## 🔐 Security on Production

```python
# settings.py for production
DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
```

---

## 📞 Getting Help

### If Deployment Fails
1. Check platform logs (Railway/PythonAnywhere web interface)
2. Check requirements.txt has all packages
3. Verify git status: `git status`
4. Test locally first: `python manage.py runserver`

### Common Sources
- **Django Docs:** https://docs.djangoproject.com/
- **Railway Docs:** https://docs.railway.app/
- **PythonAnywhere Docs:** https://help.pythonanywhere.com/
- **Stack Overflow:** Tag your questions [django] + [deployment]

---

## ✨ Summary

**To Update:**
```bash
git commit -m "your changes"
git push origin main
# That's it. Platform auto-deploys
```

**To Add Database Field:**
```bash
# Edit model
python manage.py makemigrations
python manage.py migrate
git push origin main
```

**To Backup:**
```bash
cp db.sqlite3 db.sqlite3.backup.$(date +%Y%m%d)
```

---

**Happy Deploying! 🚀**
