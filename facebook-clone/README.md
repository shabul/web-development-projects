# Facebook Clone - 3D Social Media Platform

A PHP-based social media platform that mimics Facebook's functionality with a 3D interface design.

## Features

- User registration and authentication
- Profile management
- Social media posting and interactions
- 3D interface design
- Admin panel for user management
- Database integration with MySQL

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: PHP
- **Database**: MySQL
- **Server**: Apache (XAMPP)

## Requirements

- System resolution: 1366x768 (recommended)
- Mozilla Firefox 17 or later
- XAMPP web server (latest version)
- PHP 7.0+
- MySQL 5.6+

## Installation

1. **Extract and Setup**
   ```bash
   # Extract the project files
   # Copy the facebook-clone folder to xampp/htdocs/
   ```

2. **Database Setup**
   - Open browser and navigate to `http://localhost/phpmyadmin/`
   - Create a new database
   - Click on "Import" tab
   - Browse and select `Database/faceback.sql` file
   - Click "Go" to import

3. **Run the Application**
   - Open browser and navigate to `http://localhost/facebook-clone/`
   - Create a new account
   - Login and explore the 3D Facebook experience

## Project Structure

```
facebook-clone/
├── Database/           # Database files
├── fb_files/          # Core application files
├── fb_users/          # User data and uploads
├── admin/             # Admin panel
├── Login.php          # Login functionality
├── index.php          # Main application entry
└── README.md          # This file
```

## Usage

1. **User Registration**: Create a new account with email and password
2. **Profile Setup**: Complete your profile information
3. **Social Features**: Post updates, interact with other users
4. **Admin Access**: Use admin panel for user management

## Contributing

Feel free to fork this project and submit pull requests for improvements.

## License

This project is for educational purposes. Please respect the original design credits.

## Support

For any issues or queries, please create an issue in this repository.
