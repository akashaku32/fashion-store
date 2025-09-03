# Ladies Clothing Store - Deployment Guide

## Quick Deploy Options

### Option 1: Railway (Recommended - Free Tier Available)

1. Go to [Railway.app](https://railway.app)
2. Sign up/login with GitHub
3. Click "New Project" > "Deploy from GitHub repo"
4. Connect your GitHub account and select this repository
5. Railway will automatically detect Django and deploy using the railway.json configuration
6. Your app will be available at: `https://your-app-name.up.railway.app`

### Option 2: Render (Free Tier Available)

1. Go to [Render.com](https://render.com)
2. Sign up/login with GitHub
3. Click "New" > "Web Service"
4. Connect your GitHub repository
5. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn ladies_clothing.wsgi:application --bind 0.0.0.0:$PORT`
6. Deploy and get your URL

### Option 3: PythonAnywhere (Free Tier Available)

1. Sign up at [PythonAnywhere.com](https://pythonanywhere.com)
2. Upload your project files
3. Create a web app with Django
4. Configure the WSGI file
5. Install requirements in the console

## Local Testing

To test the deployment configuration locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Test with gunicorn
gunicorn ladies_clothing.wsgi:application --bind 127.0.0.1:8000
```

## Environment Variables (if needed)

- `DEBUG=False` (for production)
- `SECRET_KEY=your-secret-key`
- `ALLOWED_HOSTS=your-domain.com`

## Features Included

✅ Django 4.2.7 with modern UI
✅ User authentication and profiles
✅ Product catalog with categories
✅ Shopping cart functionality
✅ Order management
✅ Responsive design
✅ Admin panel
✅ Static file serving configured
✅ Database migrations ready

## Demo Credentials

After deployment, you can create a superuser:
```bash
python manage.py createsuperuser
```

The app includes sample data with categories and products ready for demonstration.

## Support

If you encounter any issues during deployment, check:
1. Requirements.txt has all dependencies
2. Environment variables are set correctly
3. Database migrations have been applied
4. Static files are collected

Your app is now ready for remote demonstration! 🚀
