#!/bin/bash

# Focused Life Tracker - Complete Setup Script
# This script automates the entire setup process

echo "🎯 Focused Life Tracker - Setup Guide"
echo "======================================"
echo ""

# Step 1: Navigate to project
echo "📍 Step 1: Navigate to project directory"
echo "cd /home/osama-bin/Focus-progress-tracker"
echo ""

# Step 2: Create virtual environment
echo "🔧 Step 2: Create Python virtual environment"
echo "python3 -m venv venv"
echo ""

# Step 3: Activate virtual environment
echo "✅ Step 3: Activate virtual environment"
echo "source venv/bin/activate"
echo ""

# Step 4: Install dependencies
echo "📦 Step 4: Install Django dependencies"
echo "pip install -r requirements.txt"
echo ""

# Step 5: Apply migrations
echo "🗄️  Step 5: Create database and apply migrations"
echo "python manage.py migrate"
echo ""

# Step 6: Create superuser
echo "👤 Step 6: Create admin superuser (follow prompts)"
echo "python manage.py createsuperuser"
echo ""
echo "   When prompted, enter:"
echo "   - Username: admin"
echo "   - Email: admin@example.com"
echo "   - Password: your-secure-password"
echo ""

# Step 7: Start development server
echo "🚀 Step 7: Start the development server"
echo "python manage.py runserver"
echo ""

echo "======================================"
echo "✨ Setup Complete!"
echo "======================================"
echo ""
echo "Access your application at:"
echo "  📱 Main App: http://127.0.0.1:8000"
echo "  🔐 Admin Panel: http://127.0.0.1:8000/admin"
echo ""
echo "First-time users should:"
echo "  1. Register at http://127.0.0.1:8000/auth/register/"
echo "  2. Login at http://127.0.0.1:8000/auth/login/"
echo "  3. Start with the Dashboard"
echo ""
