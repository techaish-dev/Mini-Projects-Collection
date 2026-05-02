# Rent2Own - E-Commerce Rental Platform

## Overview

Rent2Own is a comprehensive full-stack e-commerce application built with .NET 6.0, designed to facilitate renting and purchasing products. The platform provides a seamless experience for users to browse products, manage orders, and complete transactions, while offering administrators tools to manage inventory and operations.

## Features

### User Features
- **User Registration & Authentication**: Secure login/signup with JWT token-based authentication
- **Product Browsing**: Explore products by categories with detailed descriptions and pricing
- **Shopping Cart**: Add/remove items, view cart summary
- **Order Management**: Place orders, track order history
- **Payment Integration**: Secure payments via Stripe (test mode)
- **Email Notifications**: Automated emails for order confirmations and updates

### Admin Features
- **Product Management**: Add, edit, delete products and categories
- **Order Oversight**: View and manage customer orders
- **User Management**: Handle user accounts and roles
- **Dashboard**: Administrative interface with data grids and rich text editing

### Technical Features
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Updates**: Dynamic UI updates using Blazor
- **Database Integration**: SQL Server with Entity Framework Core
- **API-Driven Architecture**: RESTful API for backend operations
- **Modular Architecture**: Separated layers for business logic, data access, and presentation

## Architecture

The application follows a clean, layered architecture:

- **Rent2Own_API**: ASP.NET Core Web API providing REST endpoints
- **Rent2Own_Server**: Blazor Server app for admin interface
- **Rent2Own_Client**: Blazor WebAssembly app for user-facing client
- **Rent2Own_Business**: Business logic layer
- **Rent2Own_DataAccess**: Data access layer with EF Core
- **Rent2Own_Models**: Entity models and DTOs
- **Rent2Own_Common**: Shared utilities and constants

## Technologies Used

### Backend
- **.NET 6.0**: Runtime framework
- **ASP.NET Core**: Web framework for API and server apps
- **Entity Framework Core**: ORM for database operations
- **SQL Server**: Relational database
- **ASP.NET Identity**: User authentication and authorization
- **JWT Bearer**: Token-based authentication

### Frontend
- **Blazor WebAssembly**: Client-side web app
- **Blazor Server**: Server-side admin interface
- **Radzen Blazor**: UI components for admin
- **Syncfusion**: Advanced grids and rich text editor
- **Bootstrap**: CSS framework for responsive design

### Integrations
- **Stripe**: Payment processing
- **MailKit/MimeKit**: Email sending
- **Swashbuckle**: API documentation (Swagger)

## Prerequisites

- .NET 6.0 SDK (download from Microsoft)
- SQL Server (Express edition is sufficient)
- Git for version control
- Visual Studio 2022 or VS Code with C# extensions

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <your-github-repo-url>
   cd Rent2Own
   ```

2. **Database Setup**
   - Ensure SQL Server is running
   - Create a new database named `Rent2Own`
   - Execute the SQL scripts in order:
     - `Category.sql` (creates categories table)
     - `Products.sql` (creates products table)
     - `ProductPrice.sql` (creates pricing table)
   - Run Entity Framework migrations:
     ```bash
     dotnet ef database update --project Rent2Own_DataAccess --context DBHelper
     ```

3. **Configuration**
   - Update `appsettings.json` in `Rent2Own_API` with your SQL Server connection string if different
   - Configure Stripe API keys (test keys are provided)
   - Adjust JWT settings for your domain if deploying

4. **Build the Solution**
   ```bash
   dotnet build
   ```

## Running the Application

The solution has multiple entry points. Run them in separate terminals:

1. **API Backend**
   ```bash
   dotnet run --project Rent2Own_API
   ```
   - Access API at: `https://localhost:44307`
   - Swagger documentation: `https://localhost:44307/swagger`

2. **Admin Server**
   ```bash
   dotnet run --project Rent2Own_Server
   ```
   - Access admin interface at the displayed URL (typically `https://localhost:5001`)

3. **User Client**
   ```bash
   dotnet run --project Rent2Own_Client
   ```
   - Access user interface at the displayed URL (typically `https://localhost:5000`)

### Alternative: Visual Studio
- Open `Rent2Own.sln`
- Set multiple startup projects (API, Server, Client)
- Press F5 to run

## API Endpoints

Key endpoints (accessible via Swagger):

- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `GET /api/products` - Get products
- `POST /api/orders` - Create order
- `GET /api/orders/{userId}` - Get user orders

## Usage

1. **As a User**:
   - Register/login via the client app
   - Browse products, add to cart
   - Checkout with Stripe payment
   - View order history

2. **As an Admin**:
   - Login to the server app
   - Manage products, categories, and orders
   - View analytics and user data

## Database Schema

- **Categories**: Product categories
- **Products**: Product catalog
- **ProductPrices**: Pricing tiers
- **OrderHeaders**: Order summaries
- **OrderDetails**: Order line items
- **ApplicationUsers**: User accounts (via Identity)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please open a GitHub issue or contact the maintainers.

## Future Enhancements

- Mobile app development
- Advanced analytics dashboard
- Multi-language support
- Integration with more payment gateways
- Real-time notifications</content>
<parameter name="filePath">D:\practice\Projects\Rent2Own\VP Project(Final)\Rent2Own\README.md