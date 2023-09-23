# CoRider-Assignment

You need to develop a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The REST API endpoints should be accessible via HTTP requests and tested using Postman.

**REQUIREMENTS :**

* The application must be developed using Flask and MongoDB.
* The application should provide REST API endpoints for CRUD operations on a User resource.
* The User resource should have the following fields:
  * id (a unique identifier for the user)
  * name (the name of the user)
  * email (the email address of the user)
  * password (the password of the user)
* The application should connect to a MongoDB database.
* The application should provide the following REST API endpoints:
  * GET /users - Returns a list of all users.
  * GET /users/<id> - Returns the user with the specified ID.
  * POST /users - Creates a new user with the specified data.
  * PUT /users/<id> - Updates the user with the specified ID with the new data.
  * DELETE /users/<id> - Deletes the user with the specified ID.
* Using Docker is mandatory.

**STEPS :**
```bash
docker-compose -f docker-compose.yaml up
```
