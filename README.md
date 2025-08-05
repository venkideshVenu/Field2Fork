# Field2Fork - Farm-to-Table E-commerce Platform

![Django](https://img.shields.io/badge/Django-5.0.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Field2Fork is a comprehensive Django-based e-commerce platform designed to connect farmers and producers directly with consumers, enabling a farm-to-table marketplace experience. The platform features user authentication, product management, shopping cart functionality, and health information resources.

## 🌟 Features

### Core Functionality

- **User Account Management** - Custom user authentication and profile management
- **Product Catalog** - Browse and search farm-fresh products
- **Shopping Cart** - Add, modify, and manage cart items
- **Marketplace** - Dedicated marketplace for farmers and producers
- **Health Information** - Educational articles about nutrition and healthy eating
- **Category Management** - Organized product categorization
- **Admin Panel** - Comprehensive Django admin interface

### Key Modules

- **Homepage** - Landing page with navigation and information
- **Store** - Main product browsing and purchasing interface
- **Marketplace** - Farmer/producer marketplace functionality
- **Cart** - Shopping cart management
- **Accounts & Login** - User authentication and profile management
- **Health Info** - Health and nutrition articles
- **Categories** - Product categorization system

## 🏗️ Project Structure

```
Field2Fork/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database
├── README.md                # Project documentation
│
├── Field2Fork/              # Main project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── accountsAndLogin/        # User authentication module
│   ├── models.py            # Custom user model
│   ├── views.py             # Authentication views
│   ├── forms.py             # User forms
│   ├── urls.py              # Auth URL patterns
│   └── migrations/          # Database migrations
│
├── store/                   # Product store module
│   ├── models.py            # Product models
│   ├── views.py             # Store views
│   ├── admin.py             # Admin configuration
│   └── migrations/          # Database migrations
│
├── marketplace/             # Marketplace module
│   ├── models.py            # Marketplace product models
│   ├── views.py             # Marketplace views
│   └── migrations/          # Database migrations
│
├── cart/                    # Shopping cart module
│   ├── models.py            # Cart and CartItem models
│   ├── views.py             # Cart management views
│   └── migrations/          # Database migrations
│
├── categories/              # Product categorization
│   ├── models.py            # Category models
│   ├── context_processor.py # Category context processor
│   └── migrations/          # Database migrations
│
├── healthinfo/              # Health information module
│   ├── models.py            # Article models
│   ├── views.py             # Health info views
│   └── migrations/          # Database migrations
│
├── homepage/                # Homepage module
│   ├── views.py             # Homepage views
│   ├── urls.py              # Homepage URL patterns
│   └── forms.py             # Contact forms
│
├── templates/               # HTML templates
│   ├── store/               # Store templates
│   ├── temp_homepage/       # Homepage templates
│   ├── temp_login/          # Authentication templates
│   ├── temp_marketplace/    # Marketplace templates
│   └── temp_healthinfo/     # Health info templates
│
└── static/                  # Static files
    ├── homepage/            # Homepage assets
    ├── marketplace/         # Marketplace assets
    ├── healthinfo/          # Health info assets
    ├── media/               # User uploaded media
    └── photo/               # Product images
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/venkideshVenu/Field2Fork.git
   cd Field2Fork
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

4. **Run database migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## 📦 Dependencies

The project uses the following main dependencies:

- **Django 5.0.7** - Web framework
- **Pillow 10.4.0** - Image processing library
- **python-dotenv 1.0.1** - Environment variable management
- **asgiref 3.8.1** - ASGI utilities
- **sqlparse 0.5.1** - SQL parsing
- **tzdata 2024.1** - Timezone data

## 🗃️ Database Models

### Account Model (Custom User)

- Extended Django's AbstractBaseUser
- Fields: username, email, phone_number, first_name, last_name, billing_address
- Custom user manager for user creation

### Product Models

- **Store.Product** - Main store products
- **Marketplace.Product** - Marketplace products
- Fields: product_name, slug, description, price, image, stock, category

### Cart Models

- **Cart** - Shopping cart container
- **CartItem** - Individual cart items with quantity

### Category Model

- Product categorization with slug and image support

### Article Model (Health Info)

- Health and nutrition articles with subject, title, date, and content

## 🛣️ URL Patterns

- `/` - Homepage
- `/admin/` - Django admin panel
- `/account/` - User authentication and profile management
- `/store/` - Product store
- `/market/` - Marketplace
- `/cart/` - Shopping cart management
- `/about/` - About page
- `/contact/` - Contact page
- `/faqs/` - Frequently asked questions
- `/help/` - Help page

## 🎨 Frontend

The project uses:

- HTML templates with Django template language
- Static CSS and JavaScript files
- Responsive design for various screen sizes
- Image handling for products and categories

## 📱 Key Features Detail

### User Authentication

- Custom user model with extended fields
- Registration and login functionality
- Profile management
- Billing address storage

### Product Management

- Dual product systems (Store and Marketplace)
- Category-based organization
- Image upload support
- Stock management
- Slug-based URLs for SEO

### Shopping Cart

- Session-based cart for anonymous users
- User-linked cart for authenticated users
- Quantity management
- Cart persistence

### Health Information

- Educational articles
- Date-based organization
- Subject categorization

## 🔧 Configuration

### Settings Configuration

- Debug mode enabled for development
- SQLite database (default)
- Media and static files configuration
- Template directories setup
- Custom user model configuration

### Security Notes

- Secret key should be moved to environment variables for production
- Debug should be set to False in production
- ALLOWED_HOSTS should be configured for production deployment

## 🚀 Deployment

For production deployment:

1. **Environment Variables**

   - Move SECRET_KEY to environment variables
   - Set DEBUG = False
   - Configure ALLOWED_HOSTS

2. **Database**

   - Consider migrating to PostgreSQL or MySQL
   - Update database configuration in settings.py

3. **Static Files**

   - Configure static file serving for production
   - Use a CDN for better performance

4. **Security**
   - Implement HTTPS
   - Configure proper security headers
   - Set up proper backup strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **venkideshVenu** - _Initial work_ - [GitHub Profile](https://github.com/venkideshVenu)

## 🆘 Support

If you encounter any issues or have questions:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Contact the maintainers

## 📊 Project Status

This project is currently in active development. Features are being added and refined regularly.

## 🔮 Future Enhancements

- Payment integration
- Order management system
- Inventory tracking
- Email notifications
- Advanced search and filtering
- User reviews and ratings
- Multi-vendor support
- Mobile application
- API development for third-party integrations

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

---

_Built with ❤️ using Django and Python_
