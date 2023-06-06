# Istruction to Use the API

## Start Project

- To start the project you have to run the command:

```bash
make start
```
 - Here you need to create a super user to access to the admin panel.

 - After this step every time you need to run docker use:

```bash
make up
```

- To shut down the docker use:

```bash
make down
```

 ## Login with github
  
 - Calling this endpoint you can login with github:

```bash
http://127.0.0.1:5050/account/github/login/
```
- After the loging you will automatically redirect to the swagger page.

- After login you can see the user profile in this endpoint:

```bash
http://127.0.0.1:5050/swagger/
```
- Here you have the possibiliti to use all the endpoints to create, update, delete and list the user profile.

# Istruction to Use the API with Postman, Insomnia or other API client (curl)

- Use the (app.spec.yaml)[api.spec.yaml] file to import the swagger page in your API client.

- In Postman you can import the swagger page in this way:

 1. go tu collections
 2. import
 3. paste the the yaml file or copy paste the content of yaml file.

 This authomatically generate a collection with all the endpoints and the base urls and parameters.

 4. after modify the bodies with the datas to test it.

 - To run it the docker shoud be up and running.

 - Here there are all the endpoint to login and make a the CRUD requests for the users.


## Alternative to swagger

- There is a redoc page implemented if you want to use it after login with github:

```bash
http://127.0.0.1:5050/redoc/
```