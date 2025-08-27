# roommateproject
This website is about roommate match and appartment listing
# Roommate Project

A Django REST API for managing roommate listings, authentication with JWT, and user interactions.  
This project allows users to register, log in securely, and create or browse available roommate listings.

---

## Features

- **User authentication with JWT** (JSON Web Tokens)  
- **Create, view, update, and delete roommate listings**  
- **Secure endpoints for authenticated users**  
- **Simple, RESTful API structure** for easy integration with frontend or mobile apps  

---

## Tech Stack

- **Backend:** Django, Django REST Framework (DRF)  
- **Authentication:** Simple JWT (access + refresh tokens)  
- **Database:** MySQL  
- **Testing tools:** REST Client / Thunder Client / Postman  

---

## Installation

1. Clone the repository:
  
   git clone https://github.com/<your-username>/roommateproject.git
   cd roommateproject
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Apply migrations:


python manage.py migrate
Create a superuser (optional, for admin access):


python manage.py createsuperuser
Run the server:


python manage.py runserver

API Endpoints
Authentication (JWT)
Obtain Token


POST /api/token/
Content-Type: application/json

{
  "email": "yourusername",
  "password": "yourpassword"
}



Roommate Listings
All listing endpoints require authentication using the access token.
Add header:
Authorization: Bearer <your_access_token>

Get all listings
GET /api/listings/


Create a new listing
POST /api/listings/
Content-Type: application/json

{
  "title": "Modern Flat in Abuja",
  "location": "Wuse 2",
  "price": "1500.00",
  "description": "Spacious rooms, secure area with constant power supply",
  "apartment_type": "2_bed",
  "duration": "12 months",
  "vacant_type": "shared",
  "user": "8bd0e166-9a76-49b9-b861-46b70aec81ab"
}




Get a single listing

GET /api/listings/<id>/
Update a listing


PUT /api/listings/<id>/
Content-Type: application/json

{
  "title": "Updated title",
  "location": "Abuja, Nigeria",
  "rent": 35000,
  "description": "Updated description"
}


Delete a listing
DELETE /api/listings/<id>/

POST http://127.0.0.1:8000/api/token/
Content-Type: application/json


{
  "username": "testuser",
  "password": "secretpassword"
}

### Get all listings (replace <ACCESS_TOKEN>)
GET http://127.0.0.1:8000/api/listings/
Authorization: Bearer <ACCESS_TOKEN>
