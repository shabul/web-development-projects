# Pharmacy Management System

A comprehensive web-based pharmacy management system built with Flask (Python) for managing medicines, inventory, and customer transactions.

## Features

- **Medicine Management**: Add, update, and track medicine inventory
- **User Authentication**: Secure login and registration system
- **Dashboard**: Real-time statistics and analytics
- **Purchase Management**: Handle medicine purchases and billing
- **Inventory Tracking**: Monitor stock levels and expiry dates
- **Responsive Design**: Mobile-friendly interface

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Charts**: Chart.js for data visualization
- **Styling**: Custom CSS with DataTables integration

## Requirements

- Python 3.7+
- Flask
- SQLite
- Web browser (Chrome, Firefox, Safari)

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd pharmacy-management-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Database**
   ```bash
   python install.py
   ```
   You should see: "Successfully DB created......!!! Thank you"

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   - Open browser and navigate to `http://localhost:5000`
   - Sign up for a new account
   - Login and start using the system

## Project Structure

```
pharmacy-management-system/
├── app.py                 # Main Flask application
├── install.py            # Database initialization
├── data_prep.py          # Data preparation utilities
├── manage.py             # Management utilities
├── requirements.txt      # Python dependencies
├── utils/                # Utility modules
│   ├── models.py         # Database models
│   ├── login_auth.py     # Authentication logic
│   ├── dashboard.py      # Dashboard functionality
│   ├── add_medicine.py   # Medicine management
│   └── buy_medicine.py   # Purchase management
├── templates/            # HTML templates
├── static/              # CSS, JS, and images
├── data/                # Data files
└── instance/            # Instance-specific files
```

## Usage

### First Time Setup
1. **Register**: Create a new account with your details
2. **Login**: Use your credentials to access the system
3. **Dashboard**: View system statistics and overview

### Medicine Management
1. **Add Medicine**: Navigate to "Add Medicine" to add new inventory
2. **View Inventory**: Check current stock levels and medicine details
3. **Update Stock**: Modify quantities and medicine information

### Purchase Management
1. **Buy Medicine**: Process customer purchases
2. **Generate Bills**: Create and print purchase receipts
3. **Track Sales**: Monitor sales statistics and revenue

## Features in Detail

### Dashboard
- Real-time inventory statistics
- Sales analytics with charts
- Low stock alerts
- Recent transactions overview

### Medicine Management
- Add new medicines with details (name, price, quantity, expiry)
- Update existing medicine information
- Delete discontinued medicines
- Search and filter functionality

### User Management
- Secure user registration and authentication
- Profile management
- Role-based access control

## API Endpoints

- `/` - Home/Dashboard
- `/login` - User login
- `/register` - User registration
- `/add_medicine` - Add new medicine
- `/buy_medicine` - Purchase medicines
- `/dashboard` - Statistics dashboard
- `/logout` - User logout

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support and questions, please create an issue in this repository.
