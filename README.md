# Practice

## Task

### Main

You have one docker image named `flask`. Your task is to run 2 applications: `main` as the main form for users and `support` for tech support. Both of them use a database in directory `/db`. Keep in mind, support should not change data.

### Additional

Keep both apps open for external connections is not really secure. And 5000 port is not obvious. Let's keep both apps inside an internal network. Since the main app should be accessible from other networks, let's also configure `Nginx` proxy server in order to handle incoming connections on 80 port and proxy it to the `main` app.

## How to work with image

There are 2 main directories within the container:

* `/src` - directory with the source code of an application. The app to be run should be named `main.py`.
* `/db` - database storage directory

## Tips

#### Request to the application from CLI

`curl` should do the stuff:

```
curl localhost:80
```