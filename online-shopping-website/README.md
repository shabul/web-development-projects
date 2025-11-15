# Online Shopping Website

A comprehensive e-commerce platform built with PHP and MySQL, featuring a complete online shopping experience with product catalog, shopping cart, and order management.

## Features

- **Product Catalog**: Browse products by categories (clothing, shoes, accessories, etc.)
- **User Authentication**: Registration and login system
- **Shopping Cart**: Add/remove items, quantity management
- **Order Management**: Place orders and track purchases
- **Admin Panel**: Product and order management
- **Search Functionality**: Find products quickly
- **Responsive Design**: Mobile-friendly interface
- **Image Gallery**: Product image viewer with lightbox
- **Contact System**: Customer support contact form

## Technology Stack

- **Backend**: PHP
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Database**: MySQL
- **Image Gallery**: jQuery Lightbox
- **Styling**: Custom CSS with responsive design

## Requirements

- PHP 7.0+
- MySQL 5.6+
- Apache Web Server (XAMPP/WAMP/LAMP)
- Web browser with JavaScript enabled

## Installation

1. **Setup Web Server**
   - Install XAMPP/WAMP/LAMP
   - Start Apache and MySQL services

2. **Database Setup**
   - Open phpMyAdmin (`http://localhost/phpmyadmin`)
   - Create a new database named `shop`
   - Import `database/shop.sql` file

3. **Configure Database Connection**
   - Edit `config.php` with your database credentials
   ```php
   $host = "localhost";
   $username = "root";
   $password = "";
   $database = "shop";
   ```

4. **Deploy Application**
   - Copy project files to `htdocs/online-shopping-website/`
   - Access via `http://localhost/online-shopping-website/`

## Project Structure

```
online-shopping-website/
├── index.php              # Homepage
├── login.php              # User login
├── register.php           # User registration
├── config.php             # Database configuration
├── order.php              # Order processing
├── contact.php            # Contact form
├── search.php             # Product search
├── database/              # Database files
│   └── shop.sql          # Database schema
├── admin/                 # Admin panel
│   ├── index.php         # Admin login
│   ├── additem.php       # Add products
│   ├── viewtable.php     # View orders
│   └── delitem.php       # Delete products
├── images/                # Product images
├── css/                   # Stylesheets
├── js/                    # JavaScript files
├── gallery in jQuery/     # Image gallery
└── documentation/         # Project documentation
```

## Product Categories

- **Men's Clothing**: T-shirts, Jeans, Suits, Casual wear
- **Women's Clothing**: Dresses, Kurtas, Office wear
- **Kids**: Boys and Girls clothing, Baby items
- **Footwear**: Shoes, Sandals for all ages
- **Accessories**: Watches, Jewelry
- **Toys**: Baby toys and games

## Admin Features

### Admin Login
- URL: `http://localhost/online-shopping-website/admin/`
- Manage products, orders, and customers

### Product Management
- Add new products with images
- Update product details and pricing
- Delete discontinued products
- Manage inventory levels

### Order Management
- View customer orders
- Process order status
- Generate order reports

## User Features

### Shopping Experience
1. **Browse Products**: Navigate through categories
2. **Product Details**: View detailed product information
3. **Add to Cart**: Select items and quantities
4. **Checkout**: Complete purchase with customer details
5. **Order Confirmation**: Receive order confirmation

### Account Management
- User registration with personal details
- Secure login system
- Profile management
- Order history

## Key Files

- `index.php` - Main homepage with product showcase
- `login.php` - User authentication
- `register.php` - New user registration
- `order.php` - Shopping cart and checkout
- `viewitem.php` - Product detail view
- `gallery.php` - Product image gallery
- `contact.php` - Customer support contact

## Database Schema

The system uses MySQL with tables for:
- Users and authentication
- Product catalog and categories
- Shopping cart and orders
- Admin management

## Customization

### Adding New Products
1. Access admin panel
2. Use "Add Item" functionality
3. Upload product images to `/images/` directory
4. Set product details and pricing

### Styling
- Modify CSS files in `/css/` directory
- Update templates in main PHP files
- Customize color scheme and layout

## Security Features

- SQL injection prevention
- Session management
- Input validation and sanitization
- Secure password handling

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Internet Explorer 9+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project includes design elements by Sunlight webdesign. Please maintain attribution as required.

## Support

For technical support or questions:
1. Check the documentation in `/documentation/`
2. Create an issue in this repository
3. Review the installation guide

## Future Enhancements

- Payment gateway integration
- Wishlist functionality
- Product reviews and ratings
- Advanced search filters
- Email notifications
- Inventory management system
