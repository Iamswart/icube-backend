# Todo API

The TODO API is a Django Rest Framework application that enables users to manage their to-do lists. It integrates Google for social authentication, allowing users to sign in easily. The application provides endpoints for user registration via Google, as well as for creating, retrieving, updating, and deleting to-do items.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Iamswart/icube-backend
   cd expense-tracker

2. **Create and activate a virtual environment windows (optional)**
    ```bash
    virtualenv myenv
    myenv\Scripts\activate

3. **Create and activate a virtual environment Unix or MacOS (optional)**
    ```bash
    virtualenv myenv
    source myenv/bin/activate

4. **Install requirements**
    ```bash
    pip install -r requirements.txt

5. **Set up environment variables**

    Create a .env file in the root directory of the project and add the following variables:

    ```bash
    DEBUG=True
    DJANGO_SECRET_KEY='your_secret_key'
    DATABASE_NAME='your_db_name'
    DATABASE_USER='your_db_user'
    DATABASE_PASSWORD='your_db_password'
    DATABASE_HOST='your_db_host'
    DATABASE_PORT='your_db_port'

    Replace the placeholders with your actual database configuration and Django secret key.

6. **Run database migrations**
    ```bash
    python manage.py migrate

7. **Start the development server**
    ```bash
    python manage.py runserver

    The API will be available at http://localhost:8000/.
