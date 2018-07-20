# A Completely Useless Application
GooseOrNot allows the user to upload a photo and decides whether that photo contains a picture of a goose ... or not!

It features a loosely coupled front-end and back-end and communicates solely through REST endpoints.

## Deployment
### Heroku
Not a particular fan of heroku but it does save me the work of manually configuring my AWS instance for this project.

A proper setup would use nginx to serve static files for our front end.

## Database
### Postgresql
Setup is relatively straightforwards so I will not include a guide here.

The Arch Linux wiki has a great walkthrough which is basically universal for most -nix platforms.

One thing to watch out for is that you may need to create your own postgres user since the default data base url generated by heroku is user dependent.

## Backend
Server side deployment is all in python.

I whole-heartedly recommend the direnv tool to manage environment settings.

You will need to set
```bash
DATABASE_URL=blah_blah_blah
APP_SETTINGS=config._SOMETHING_Config
```

### Flask
- Application Factory Pattern
### SQLAlchemy
Flask is integrated with SQLAlchemy so not much setup is required.

run the following for server migrations
```bash
python manage.py db migrate
python manage.py db upgrade
python manage.py db downgrade
```

The only thing to beware of is that adding a new model definition but not using it in any route or not importing it anywhere means SQLALchemy's introspection will not detect it.

A proper setup of Flask would NOT require the Application Factory Pattern but it may solve circular imports which you can fall into to escape the above issue.

**Note**

Always manually inspect migration files generated by alembic since no tool is perfect!

I wrote a simple script you can run interactively with ipython to verify the changes you made to the database.

run
```bash
ipython -i -m server.scripts.interactive
```


### TensorFlow
This project was partially inspired by Professor Andrew Ng's Deep Learning Specialization on Coursera. Definitely shoutout to him for the excellent material.

### Redis Task Queue
The redis task queue is used to process client requests to run our neural network.

you will need to install redis or redis-server depending on your platform and run it (as a daemon)

the development redis worker is a simple script but is run as a daemon on our staging and development servers

### SocketIO
SocketIO is used to keep the client up to date with the progress of the request to process a photo

## Client
### React-Socket-IO
the client for our websocket to process requests

### Web
#### React-Typescript
I simply modified the setup for the cookie cutter starter for typescript react.

Note that if you use vim as your editor and vim-syntastic, you may need to install typescript typescript-dev tslint globally.

**Note**

If you use vim as your main editor, I strongly advise installation of Quramy/tusquyomi client for the TSServer

##### Webpack
### Mobile
This would technically be my first mobile project. If there's anything you notice and wish to fix, let me know!

#### React-Native-Typescript
I did not use the cookie cutter for mobile since the expo platform is still a bit too raw for my taste.

##### Android
I am using openjdk8, jdk9 is not working for me but you are more than welcome to try :).

On Archlinux. You may need to enable the multilib repository for certain dependencies.

The development platforms does NOT use android-studio but feel free to install the IDE if you are more comfortble with that.

Install android-sdk, android-sdk-build-tools, android-sdk-platform-tools. We will need platforms;android-26.

**Note**

The react-native targeted gradle download is completely behind, I am currently using 4.9

the adb tool (android device bridge) comes with the android=sdk-platform-tools. Please do NOT install the android-tool or the adb versions may not match and result in terrible things.

To accept licenses for a platform run either
```bash
sdkmanager "platforms;android-26"
sdkmanager --licenses
```
to resolve the issue.

We may need to install the android-ndk package due to gradle issues.

You must also export certain paths for the android packages installed, this is trivially resolved by a google search so will not be provided here.

##### iOS
I did not test anything on the iOs platform but in theory (aka never), the react-native library should run correctly.

Please lookup up the react-native IOs guide if you wish to extend this project for the iOs platform.

