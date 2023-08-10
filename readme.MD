# Gecko🐸

Welcome to Gecko, a powerful and versatile Django application designed to streamline your development process and provide a robust foundation for building feature-rich web applications. Whether you're a seasoned developer or just starting your journey, Gecko's comprehensive feature set will empower you to create efficient and secure web applications with ease.

![Gecko Logo](assets/gecko.gif)



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Basic Authentication](#basic-authentication)
  - [JWT-based REST API Authentication](#jwt-based-rest-api-auth)
  - [Social Authentication](#social-authentication)
  - [AWS S3 Storage](#aws-s3-storage)
  - [PostgreSQL Database](#postgresql-database)
  - [Redis Cache](#redis-cache)
  - [Background Tasks with Celery and Redis](#background-tasks-with-celery-and-redis)
  - [Notifications](#notifications)
  - [OTP-based Authentication](#otp-based-authentication)
  - [Sidebar and Basic Dashboard](#sidebar-and-basic-dashboard)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Gecko is a Free and Open Source Software (FOSS) Django application that simplifies and accelerates the development of web applications. It provides a set of pre-built features that are essential for modern web applications, allowing developers to focus on their application's unique logic rather than reinventing the wheel.

## Features

1. **Basic Authentication**: Secure user authentication system out of the box.

2. **JWT-based REST API Authentication**: Create secure REST APIs using JSON Web Tokens for enhanced authentication and authorization.

3. **Social Authentication**: Seamlessly integrate social authentication into your Django-based full stack applications.

4. **AWS S3 Storage**: Effortlessly store and manage your application's static and media files using Amazon S3.

5. **PostgreSQL Database**: Utilize the power and reliability of PostgreSQL for managing your application's data.

6. **Redis Cache**: Improve application performance with Redis-based caching mechanism.

7. **Background Tasks with Celery and Redis**: Execute background tasks and asynchronous processes using Celery and Redis integration.

8. **Notifications**: Implement a notification system to keep users informed and engaged.

9. **OTP-based Authentication**: Enhance security with OTP-based two-factor authentication.

10. **Sidebar and Basic Dashboard**: Get started quickly with a basic dashboard layout and sidebar navigation.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- Python (version x.x)
- Pip (package installer)
- Virtualenv (optional but recommended)

### Installation

1. Clone the Gecko repository:

   ```bash
   git clone https://github.com/yourusername/gecko.git
   cd gecko
   ```

2. Create and activate a virtual environment:

   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Copy the example configuration file and set the necessary environment variables:

   ```bash
   cp .env.example .env
   ```

   Update `.env` with your configuration values for AWS, PostgreSQL, Redis, and other settings.

2. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

### Basic Authentication

Gecko comes with a built-in basic authentication system for user registration, login, and password management. You can extend and customize it as needed.

### JWT-based REST API Authentication

Secure your RESTful APIs using JSON Web Tokens for authentication and authorization. Refer to the documentation for integrating JWT authentication in your API views.

### Social Authentication

Integrate social authentication providers (e.g., Facebook, Google) into your Django-based full stack applications using Gecko's pre-built social authentication system.

### AWS S3 Storage

Configure your application to store static and media files on Amazon S3 for efficient and scalable file management.

### PostgreSQL Database

Utilize the PostgreSQL database backend for efficient data storage and management. Update your settings to connect to your PostgreSQL instance.

### Redis Cache

Improve your application's performance by utilizing Redis as a caching mechanism. Configure your cache settings to use Redis.

### Background Tasks with Celery and Redis

Execute asynchronous and background tasks using Celery and Redis integration. Refer to the documentation for implementing and managing background tasks.

### Notifications

Implement a notification system in your application to keep users informed about important events and updates.

### OTP-based Authentication

Enhance user security with OTP-based two-factor authentication. Follow the documentation to integrate OTP authentication into your application.

### Sidebar and Basic Dashboard

Gecko provides a basic dashboard layout and sidebar navigation components to help you kickstart your application's frontend development.

## Contributing

We welcome contributions from the open-source community! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for details on how to get involved.

## License

Gecko is released under the [MIT License](LICENSE).

---

Happy coding with Gecko! If you encounter any issues or have questions, feel free to open an issue on the repository. We're here to help.