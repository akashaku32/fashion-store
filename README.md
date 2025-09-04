# 🌸 Luna & Lace - Kerala Fashion Ecommerce Store

A beautiful, responsive ecommerce website for traditional Kerala women's fashion, featuring modern design with cultural authenticity.

## ✨ Features

### 🛍️ Ecommerce Functionality
- **Product Catalog** - Browse by categories with advanced filtering
- **Shopping Cart** - Add, remove, and update quantities
- **Checkout Process** - Complete order management
- **Order History** - Track past purchases
- **User Accounts** - Registration, login, and profile management

### 🎨 Design & User Experience
- **Kerala Traditional Theme** - Authentic cultural design elements
- **Mobile-First Design** - Optimized for all devices
- **Responsive Layout** - Beautiful on desktop, tablet, and mobile
- **Smooth Animations** - Engaging user interactions
- **High-Quality Imagery** - Professional product photography

### 🏛️ Technical Features
- **Django 3.2** - Robust Python web framework
- **Bootstrap 5** - Modern responsive design
- **PostgreSQL** - Reliable database management
- **Static File Optimization** - Fast loading times
- **SEO Optimized** - Search engine friendly

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ladies-clothing-store
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data**
   ```bash
   python manage.py add_kerala_products
   python manage.py add_diverse_fashion
   python manage.py add_seasonal_galleries
   python manage.py add_all_product_images
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Open http://127.0.0.1:8000 in your browser
   - Admin panel: http://127.0.0.1:8000/admin

## 📱 Pages & Functionality

### 🏠 Homepage
- **Hero Section** - Stunning Kerala traditional imagery
- **Featured Products** - Highlighted items
- **Category Showcase** - Easy navigation
- **Seasonal Gallery** - Dynamic content

### 🛍️ Product Pages
- **Product List** - Filtered browsing with search
- **Product Detail** - Comprehensive product information
- **Image Gallery** - Multiple product views
- **Add to Cart** - Seamless shopping experience

### 🛒 Shopping Cart
- **Cart Management** - Add, remove, update quantities
- **Price Calculation** - Automatic totals and taxes
- **Checkout Process** - Secure order completion

### 👤 User Accounts
- **Registration** - Easy account creation
- **Profile Management** - Personal information
- **Address Book** - Multiple shipping addresses
- **Order History** - Track all purchases

## 🎨 Design Philosophy

### Kerala Traditional Elements
- **Color Palette** - Inspired by Kerala's vibrant culture
- **Typography** - Elegant and readable fonts
- **Imagery** - Traditional Kerala fashion and jewelry
- **Cultural Integration** - Multi-religious fashion support

### Modern UX Principles
- **Mobile-First** - Designed for mobile users
- **Accessibility** - Inclusive design
- **Performance** - Fast loading and smooth interactions
- **Intuitive Navigation** - Easy to use interface

## 🛠️ Technical Stack

### Backend
- **Django 3.2** - Web framework
- **PostgreSQL** - Database
- **Django Admin** - Content management

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **JavaScript** - Interactive functionality
- **Bootstrap 5** - Responsive framework

### Development Tools
- **Git** - Version control
- **Pip** - Package management
- **Virtual Environment** - Isolated development

## 📊 Project Structure

```
ladies-clothing-store/
├── accounts/                 # User authentication
├── store/                   # Main ecommerce app
│   ├── management/commands/ # Custom management commands
│   ├── migrations/          # Database migrations
│   ├── models.py           # Data models
│   ├── views.py            # Business logic
│   └── urls.py             # URL routing
├── templates/              # HTML templates
│   ├── accounts/           # User account templates
│   └── store/              # Ecommerce templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
├── media/                  # User uploaded files
└── ladies_clothing/        # Project settings
```

## 🎯 Key Features

### Product Management
- **33 Products** across 16 categories
- **High-Quality Images** with fallbacks
- **Pricing in Rupees** (₹) for Indian market
- **Category Organization** for easy browsing

### Shopping Experience
- **Responsive Design** works on all devices
- **Smooth Animations** for better UX
- **Real-time Updates** for cart and orders
- **Secure Checkout** process

### Admin Features
- **Django Admin** for content management
- **Product Management** - Add, edit, delete products
- **Order Management** - Track and process orders
- **User Management** - Manage customer accounts

## 🌟 Highlights

- ✅ **Fully Functional** - Complete ecommerce functionality
- ✅ **Mobile Optimized** - Perfect on all devices
- ✅ **Kerala Theme** - Authentic cultural design
- ✅ **Modern Design** - Beautiful and professional
- ✅ **Easy to Use** - Intuitive user interface
- ✅ **Well Documented** - Clear code and documentation

## 📞 Support

For support or questions about this project, please contact:
- **Email:** akashaku32@gmail.com
- **Phone:** 7736970618

## 📄 License

This project is created for demonstration purposes. All rights reserved.

---

**Built with ❤️ for Kerala Fashion Lovers**