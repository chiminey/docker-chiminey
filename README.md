Dockerized Chiminey
===================

This is a dockerized build of the docker branch of the Chiminey system: http://chiminey.net

Usage
-----

1. Install docker (>= 1.12.0) and docker-compose (>=1.7.0)

http://docs.docker.com/compose)

2. Clone the dockerized chiminey repository
 ```
    $ git clone https://github.com/chiminey/docker-chiminey.git
 ```

3. Change your working directory
 ```
    $ cd docker-chiminey
    $ git checkout prism
 ```

4. Copy the prototype environment file to your personalised version and change passwords as needed:

```
    $ cp env .env
```

5. Setup a self-signed certificate. You will be prompted to enter country code, state, city, and etc.
```
    $ sh makecert
```

6. Deploy the Chiminey platform
```
    $ docker-compose up -d
```

   After about a minute, the location http://127.0.0.1 will point at the Chiminey portal.
   To watch the celery workers go to: http://127.0.0.1:8080

7. Configure the Chiminey deployment by creating the superuser, initialising the database, and signing up regular users.

```
    $ ./createsuper
    $ ./init
    $ ./createuser
```

8. List existing smart connectors
```
    $ ./listscs
```

9. Activate smart connectors from the tutorials at http://chiminey.readthedocs.org. The syntax to add any of the smart connectors that are included with the platform is ```$ ./activatesc smart-connector-name```. Agree to activate the smart connector when prompted.

```
    $ /activatesc prism
```

This project is working reasonably well as a demo, but IS NOT FOR PRODUCTION USE
