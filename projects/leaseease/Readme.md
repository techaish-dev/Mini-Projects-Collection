# 🏠 LeaseEase - Rent-to-Own E-commerce Platform

[![.NET](https://img.shields.io/badge/.NET-6.0-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![C#](https://img.shields.io/badge/C%23-10.0-239120?style=for-the-badge&logo=csharp&logoColor=white)](https://docs.microsoft.com/en-us/dotnet/csharp/)
[![ASP.NET Core](https://img.shields.io/badge/ASP.NET_Core-6.0-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/apps/aspnet)
[![Blazor](https://img.shields.io/badge/Blazor-WebAssembly-512BD4?style=for-the-badge&logo=blazor&logoColor=white)](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor)
[![Entity Framework](https://img.shields.io/badge/Entity_Framework-6.0-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)](https://docs.microsoft.com/en-us/ef/)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

---

## 📋 Overview

**LeaseEase** is a full-stack rent-to-own e-commerce platform built with .NET 6.0 and ASP.NET Core, following a clean layered architecture. It enables users to rent products with the option to own them through flexible payment plans.

### 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🏪 **Product Catalog** | Browse products with categories and pricing tiers |
| 👤 **User Authentication** | Secure JWT-based authentication with ASP.NET Identity |
| 💳 **Payment Processing** | Stripe integration for secure payments (test mode) |
| 📦 **Order Management** | Track rentals, purchases, and payment schedules |
| 📧 **Email Notifications** | Automated email alerts via MailKit |
| 🎨 **Modern UI** | Blazor WebAssembly frontend with Bootstrap |
| 📊 **Admin Dashboard** | Radzen & Syncfusion components for management |
| 🔐 **Role-Based Access** | Separate client and admin interfaces |

---

## 🏗️ Architecture

The solution follows a **clean layered architecture** with 6 interconnected projects:
LeaseEase.sln


├── 📁 LeaseEase_API # ASP.NET Core Web API (Backend Entry)


├── 📁 LeaseEase_Server # ASP.NET Core App (Admin Interface)


├── 📁 LeaseEase_Client # Blazor WebAssembly (Frontend)


├── 📁 LeaseEase_Business # Business Logic Layer


├── 📁 LeaseEase_DataAccess # Data Access Layer (EF Core)


├── 📁 LeaseEase_Models # Data Models


└── 📁 LeaseEase_Common # Shared Utilities


### Layer Responsibilities

| Project | Responsibility | Tech Stack |
|---------|---------------|------------|
| **API** | RESTful endpoints, auth, email, payments | ASP.NET Core Web API, JWT, MailKit, Stripe |
| **Server** | Admin dashboard, management interface | ASP.NET Core, Radzen, Syncfusion |
| **Client** | User-facing web interface | Blazor WebAssembly, Bootstrap, jQuery |
| **Business** | Core business logic, payment processing | C# .NET 6.0 |
| **DataAccess** | Database operations, migrations | Entity Framework Core, SQL Server |
| **Models** | Data entities, Identity models | C# POCOs |
| **Common** | Shared utilities, helpers | C# .NET 6.0 |

---

## 🚀 Quick Start Guide

### Prerequisites

| Requirement | Version |
|-------------|---------|
| .NET SDK | 6.0 or higher |
| SQL Server | Express or Developer Edition |
| Visual Studio | 2022 (recommended) |
| Stripe Account | Test mode (free) |

### Installation Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/techaish-dev/Mini-Projects-Collection.git
cd Mini-Projects-Collection/projects/leaseease
```

#### 2️⃣ Set Up Database
```bash
-- Create database
CREATE DATABASE LeaseEase;
GO

-- Update connection string in appsettings.json
-- "ConnectionStrings": {
--   "DefaultConnection": "Server=YOUR_SERVER;Database=LeaseEase;Trusted_Connection=True;"
-- }
```
#### 3️⃣ Run Database Migrations
```bash

# From the solution root
cd LeaseEase

# Add initial migration
dotnet ef migrations add Init --project LeaseEase_DataAccess --context DBHelper

# Update database
dotnet ef database update --project LeaseEase_DataAccess --context DBHelper
```

#### 4️⃣ Seed Initial Data
Run the provided SQL scripts in order:

```bash

-- Execute these scripts (in order)
1. Category.sql      -- Create categories
2. Products.sql      -- Create products
3. ProductPrice.sql  -- Set pricing tiers
```

#### 5️⃣ Configure Stripe (Test Mode)
Update appsettings.json:
```bash
{
  "Stripe": {
    "SecretKey": "sk_test_YOUR_TEST_KEY",
    "PublishableKey": "pk_test_YOUR_TEST_KEY"
  }
}

```
#### 6️⃣ Build and Run

```bash
# Build solution
dotnet build

# Run API (Backend)
dotnet run --project LeaseEase_API
# Swagger UI: https://localhost:44307/swagger

# Run Server (Admin Interface)
dotnet run --project LeaseEase_Server
# Admin URL: https://localhost:5001

# Run Client (User Interface)
dotnet run --project LeaseEase_Client
# Client URL: https://localhost:5000
```

#### Visual Studio Setup (Alternative)
Open LeaseEase.sln in Visual Studio 2022
Set multiple startup projects:

-LeaseEase_API

-LeaseEase_Server

-LeaseEase_Client

Press F5 to run
