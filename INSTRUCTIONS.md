# Istruction to Use the API

## Start Project

- In order to start the project you need to register the app in github you need to add to dev.env the Client ID and the Secret Key.

- To start the project you have to run the command:

```bash
make start
```
 - Here you need to create a super user to access to the admin panel.

 ## Register another app in github (optional)

- To register the app in github you need to add to dev.env the Client ID and the Secret Key of your new app and change the name.
- After this you can run the command to register the app in github:

```bash
make socialapp
```


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
- Here you have the possibility to use all the endpoints to create, update, delete and list the user profile.


## Alternative to swagger

- There is a redoc page implemented if you want to use it after login with github:

```bash
http://127.0.0.1:5050/redoc/
```

## YAML file

- The api.spec.yaml provide all the instruction about the api.
- You can use it to import the api in postman or other software.

## Every thing is made to avoid to use directly the admin pannel, if you need it you have to access with a superuser to be able to see all the models inside.

link to the admin pannel:

```bash
127.0.0.1:5050/admin/
```

# I hope you enjoy it!