# Elegance Boutique - Ladies Clothing E-commerce Website

A modern, responsive e-commerce website built with Django for a premium ladies clothing brand. Features a unique design with flexible layouts, advanced shopping cart functionality, and comprehensive user management.

## 🚀 Quick Deploy for Demo

Deploy this application instantly for remote demonstration:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/django)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

> **Perfect for client demos!** The application includes sample data and is ready to showcase immediately after deployment.

## Features

### 🛍️ E-commerce Features
- **Product Catalog**: Browse products by categories with advanced filtering
- **Product Details**: Detailed product pages with image galleries and reviews
- **Shopping Cart**: Session-based cart with real-time updates
- **Checkout Process**: Complete order placement with address management
- **Order Management**: Order history, tracking, and status updates
- **User Reviews**: Product rating and review system

### 👤 User Management
- **User Registration & Authentication**: Secure user accounts
- **Profile Management**: Personal information and address management
- **Order History**: Complete order tracking and history
- **Address Book**: Multiple saved addresses for quick checkout

### 🎨 Design & UI/UX
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI**: Clean, elegant design with custom CSS animations
- **Unique Branding**: Custom color scheme and typography
- **Interactive Elements**: Smooth animations and hover effects
- **Accessibility**: WCAG compliant design patterns

### 🔧 Technical Features
- **Django Admin**: Comprehensive admin interface for product management
- **Image Management**: Multiple product images with primary image selection
- **Search & Filtering**: Advanced product search and filtering
- **Newsletter**: Email subscription system
- **Security**: CSRF protection, secure forms, and user authentication

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Playfair Display, Inter)
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Image Processing**: Pillow
- **Forms**: Django Crispy Forms with Bootstrap 5

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ladies-clothing-ecommerce
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
ladies-clothing-ecommerce/
├── ladies_clothing/          # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── store/                   # Main e-commerce app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   └── context_processors.py # Template context processors
├── accounts/                # User management app
│   ├── models.py            # User-related models
│   ├── views.py             # Authentication views
│   ├── urls.py              # Account URL patterns
│   └── forms.py             # User forms
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── store/               # Store templates
│   └── accounts/            # Account templates
├── static/                  # Static files
│   ├── css/                 # Custom CSS
│   ├── js/                  # JavaScript files
│   └── images/              # Static images
├── media/                   # User uploaded files
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```

## Key Models

### Product Models
- **Category**: Product categories with images and descriptions
- **Product**: Main product model with pricing, inventory, and details
- **ProductImage**: Multiple images per product with primary selection

### User Models
- **Customer**: Extended user profile with additional information
- **Address**: Multiple addresses per customer for shipping/billing

### Order Models
- **Order**: Complete order information with status tracking
- **OrderItem**: Individual items within an order
- **Cart**: Shopping cart for authenticated and anonymous users
- **CartItem**: Items in the shopping cart

### Additional Models
- **Review**: Product reviews and ratings
- **Newsletter**: Email subscription management

## Customization

### Styling
The website uses a custom CSS framework with:
- CSS Custom Properties (variables) for consistent theming
- Modern CSS features (Grid, Flexbox, animations)
- Responsive design patterns
- Custom component styles

### Branding
- Primary Color: Purple (#8B5CF6)
- Secondary Color: Orange (#F59E0B)
- Accent Color: Pink (#EC4899)
- Typography: Playfair Display (headings), Inter (body)

### Adding New Features
1. Create new models in `store/models.py`
2. Add corresponding views in `store/views.py`
3. Create URL patterns in `store/urls.py`
4. Design templates in `templates/store/`
5. Update admin interface in `store/admin.py`

## Admin Features

The Django admin interface provides:
- **Product Management**: Add, edit, and organize products
- **Category Management**: Create and manage product categories
- **Order Management**: View and update order statuses
- **User Management**: Manage customer accounts and addresses
- **Review Management**: Moderate product reviews
- **Newsletter Management**: Manage email subscriptions

## Deployment

### Production Settings
1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure email settings
5. Set up SSL certificate
6. Configure domain and hosting

### Environment Variables
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/database
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact: info@eleganceboutique.com

## Acknowledgments

- Django framework and community
- Bootstrap team for the CSS framework
- Font Awesome for the icon library
- Google Fonts for typography
- All contributors and testers

---

**Elegance Boutique** - Where style meets sophistication.


