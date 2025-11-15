# Online Voting System

A secure web-based voting system built with PHP and MySQL, designed for conducting online elections with real-time results and comprehensive admin management.

## Features

- **Secure Voting**: One-time voting per registered user
- **Real-time Results**: Live vote counting and result display
- **Admin Panel**: Complete election management system
- **Candidate Management**: Add, edit, and manage candidates
- **Position Management**: Create different voting positions
- **User Registration**: Secure voter registration system
- **Result Analytics**: Charts and graphs for result visualization
- **Access Control**: Role-based permissions for admin and voters

## Technology Stack

- **Backend**: PHP
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Database**: MySQL
- **Charts**: Highcharts.js for result visualization
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
   - Create a new database named `poll`
   - Import `poll.sql` file from the project root

3. **Deploy Application**
   - Copy project files to `htdocs/online-voting-system/`
   - Ensure proper file permissions

4. **Access the System**
   - Voter Interface: `http://localhost/online-voting-system/`
   - Admin Panel: `http://localhost/online-voting-system/admin/`

## Default Admin Credentials

- **URL**: `http://localhost/online-voting-system/admin/`
- **Username**: `admin@example.com`
- **Password**: `admin`

**⚠️ Important**: Change default admin credentials after first login!

## Project Structure

```
online-voting-system/
├── index.php              # Voter login page
├── vote.php               # Voting interface
├── registeracc.php        # Voter registration
├── checklogin.php         # Authentication logic
├── connection.php         # Database connection
├── poll.sql               # Database schema
├── student.php            # Voter dashboard
├── manage-profile.php     # Profile management
├── results.php            # Public results page
├── admin/                 # Admin panel
│   ├── index.php         # Admin login
│   ├── admin.php         # Admin dashboard
│   ├── candidates.php    # Candidate management
│   ├── positions.php     # Position management
│   ├── manage-admins.php # Admin user management
│   ├── results.php       # Admin results view
│   └── refresh.php       # Data refresh utilities
├── css/                   # Stylesheets
├── js/                    # JavaScript files
├── images/                # System images and logos
└── LICENSE.txt            # License information
```

## Admin Features

### Election Management
- **Create Positions**: Set up different voting categories (President, Secretary, etc.)
- **Manage Candidates**: Add candidates with photos and descriptions
- **Monitor Voting**: Real-time voting statistics and progress
- **Generate Reports**: Export results and voting data

### User Management
- **Admin Accounts**: Create and manage admin users
- **Voter Registration**: Approve or manage voter registrations
- **Access Control**: Set permissions and roles

### Results & Analytics
- **Live Results**: Real-time vote counting
- **Visual Charts**: Graphical representation of results
- **Export Data**: Download results in various formats

## Voter Features

### Registration & Login
1. **Register**: Create voter account with personal details
2. **Login**: Secure authentication system
3. **Profile**: Manage personal information

### Voting Process
1. **View Positions**: See all available voting positions
2. **Select Candidates**: Choose preferred candidates
3. **Cast Vote**: Submit secure ballot
4. **Confirmation**: Receive voting confirmation

### Results Access
- View live results (if enabled by admin)
- See voting statistics and charts

## Security Features

- **One Vote Per User**: Prevents multiple voting
- **Session Management**: Secure user sessions
- **SQL Injection Protection**: Parameterized queries
- **Input Validation**: Sanitized user inputs
- **Access Control**: Role-based permissions
- **Audit Trail**: Voting activity logging

## Database Schema

### Main Tables
- `admin` - Admin user accounts
- `voters` - Registered voter information
- `positions` - Voting positions/categories
- `candidates` - Candidate information
- `votes` - Cast votes (anonymized)
- `logs` - System activity logs

## Configuration

### Database Connection
Edit `connection.php`:
```php
$host = "localhost";
$username = "root";
$password = "";
$database = "poll";
```

### System Settings
- Voting period configuration
- Result visibility settings
- Registration requirements
- Admin permissions

## Usage Guide

### For Administrators

1. **Initial Setup**
   - Login with default credentials
   - Change admin password
   - Configure system settings

2. **Create Election**
   - Add voting positions
   - Register candidates
   - Set voting period

3. **Monitor Election**
   - Track voting progress
   - View real-time statistics
   - Manage any issues

4. **Post-Election**
   - Generate final results
   - Export data for records
   - Archive election data

### For Voters

1. **Registration**
   - Complete voter registration form
   - Wait for admin approval (if required)

2. **Voting**
   - Login to the system
   - Review candidates and positions
   - Cast your vote securely

3. **Results**
   - View results when available
   - Check voting statistics

## API Endpoints

- `/vote.php` - Cast vote
- `/results.php` - Get results
- `/admin/candidates.php` - Manage candidates
- `/admin/positions.php` - Manage positions
- `/checklogin.php` - Authentication

## Customization

### Styling
- Modify CSS files in `/css/` directory
- Update logos and images in `/images/`
- Customize color schemes and layouts

### Functionality
- Add new voting features
- Modify result calculations
- Enhance security measures
- Add notification systems

## Troubleshooting

### Common Issues
1. **Database Connection Error**
   - Check database credentials in `connection.php`
   - Ensure MySQL service is running

2. **Login Issues**
   - Verify user credentials
   - Check session configuration

3. **Voting Problems**
   - Ensure user hasn't already voted
   - Check database permissions

### Error Logs
- Check Apache error logs
- Review PHP error messages
- Monitor database query logs

## Security Best Practices

1. **Change Default Passwords**: Update all default credentials
2. **Regular Updates**: Keep system components updated
3. **Backup Data**: Regular database backups
4. **Monitor Access**: Review access logs regularly
5. **Secure Hosting**: Use HTTPS in production

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## License

This project is open source. See `LICENSE.txt` for details.

## Support

For support and questions:
1. Create an issue in this repository
2. Check the documentation
3. Review the installation guide

## Future Enhancements

- Mobile app integration
- Blockchain voting verification
- Multi-language support
- Advanced analytics dashboard
- Email notification system
- Biometric authentication
