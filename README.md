## Blogging Platform API
This is a RESTful API for a Blogging Platform, developed using Django and Django REST Framework (DRF). The API allows users to create and manage blog posts, categorize them, tag them with multiple tags, and interact with the posts through comments and likes. The platform also includes user authentication and a flexible filtering system.

## Table of Contents
Features
Technologies Used
Setup and Installation
API Endpoints
Data Models
Authentication
Challenges and Key Learnings
Future Enhancements
Features
User Authentication: Register, login, and manage user profiles.
Blog Post Management: CRUD operations for blog posts.
Categories and Tags: Classify posts by categories and assign multiple tags.
Comments: Allow users to comment on blog posts.
Likes: Optional feature to like posts.
Search and Filter: Search for posts by title and filter posts by category, tags, or author.
Pagination and Sorting: Paginate and sort results for efficient browsing.
Technologies Used
Backend Framework: Django
API Framework: Django REST Framework (DRF)
Database: SQLite (for development) or PostgreSQL (for production)
Authentication: Token-based authentication using DRF
Tools:
ERD Tool: Lucidchart / Draw.io
API Testing: Postman
Setup and Installation
1. Clone the repository
bash
Copy code
git clone (https://github.com/mallifs/Blog-Platform-api)
cd Blog-platform-api
2. Set up the virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate    # For MacOS/Linux
venv\Scripts\activate       # For Windows
3. Install the dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up the database
bash
Copy code
python manage.py migrate
5. Create a superuser for admin access
bash
Copy code
python manage.py createsuperuser
6. Run the server
bash
Copy code
python manage.py runserver
7. Access the admin interface
Go to http://127.0.0.1:8000/admin and log in with your superuser credentials to manage users, blog posts, categories, and tags.

## API Endpoints
Here's a summary of the API endpoints:

## Authentication
POST /api/auth/login/: Log in a user.
POST /api/auth/register/: Register a new user.
POST /api/auth/logout/: Log out the current user.
Blog Posts
GET /api/posts/: List all blog posts (supports pagination, sorting, filtering).
POST /api/posts/: Create a new blog post (authenticated users).
GET /api/posts/{id}/: Retrieve details of a single post.
PUT /api/posts/{id}/: Update a blog post (author only).
DELETE /api/posts/{id}/: Delete a blog post (author only).
## Categories and Tags
GET /api/categories/: List all categories.
GET /api/tags/: List all tags.
## Comments
GET /api/posts/{post_id}/comments/: List comments on a post.
POST /api/posts/{post_id}/comments/: Add a comment to a post (authenticated users).
DELETE /api/comments/{id}/: Delete a comment (author or admin).
## Likes (Optional)
POST /api/posts/{post_id}/like/: Like a post (authenticated users).
DELETE /api/posts/{post_id}/unlike/: Unlike a post.
## Data Models
User: Uses Django's built-in user model for authentication.
BlogPost:
Title
Content
Author (ForeignKey to User)
Category (ForeignKey to Category)
Tags (Many-to-Many relation with Tag)
Created date
Published date
Category: Represents a category for classifying blog posts.
Tag: Represents a tag for tagging blog posts.
Comment: Allows users to comment on blog posts.
Like (Optional): Allows users to like blog posts.
Authentication
The API uses token-based authentication provided by Django REST Framework. Users need to log in to access restricted endpoints such as creating posts, commenting, or liking posts.

## Example Login Request:
bash
Copy code
POST /api/auth/login/
Content-Type: application/json
{
    "username": "your_username",
    "password": "your_password"
}
Upon successful login, a token will be provided in the response which should be included in the headers for authenticated requests.

## Challenges and Key Learnings


## Challenges Faced:
Handling complex relationships between BlogPost, Tag, and Category in Django ORM required careful design of models and migrations.
Optimizing search and filtering in large datasets to maintain efficiency and reduce response times.
Implementing custom permissions to ensure that only authors can edit or delete their own posts and comments.
Debugging deployment issues on Heroku or PythonAnywhere, especially with environment variables and database configuration.


## Key Learnings:
Understanding Django ORM and how it simplifies the creation and management of database models.
Implementing token-based authentication using Django REST Framework.
Best practices for designing RESTful APIs, including versioning, proper status codes, and pagination.
Optimizing database queries for better performance and scalability in production environments.


## Future Enhancements

## User Profiles: 
Enhance user profiles with bio, profile pictures, and social links.
Draft Posts: Add support for saving blog posts as drafts.
Post Sharing: Allow users to share blog posts via social media or email.
Notification System: Implement a system for notifying users when someone comments on or likes their post.
Post Analytics: Track views, comments, and likes on blog posts for authors to see post performance.

## License
This project is licensed under the MIT License. See the LICENSE file for details.