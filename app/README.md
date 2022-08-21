# Flask Application with Gunicorn and Nginx

A very common production stack is to create a [Flask](
https://flask.palletsprojects.com/en/2.1.x/) application with a [Gunicorn](
https://gunicorn.org/) server and [NGINX](https://www.nginx.com/) front-end [reverse
proxy](https://en.wikipedia.org/wiki/Reverse_proxy#:~:text=In%20computer%20networks%2C%20a%20reverse,%2C%20performance%2C%20resilience%20and%20security.). Flask provides its own server, however this is not designed for anything beyond development and testing purposes.

This toy example allows you to launch a gunicorn server hosting the application locally
but does not go to the full extent of configuring a system daemon, setting up a reverse
proxy and connecting to an external domain name. To go through this complete process
follow [this tutorial](
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04).

I would also recommend the following presentation for tips from someone far more
experienced in this domain:
- [Miguel Grinberg - Flask at Scale - PyCon 2016](https://www.youtube.com/watch?v=tdIIJuPh3SI)
- [github Flack](https://github.com/miguelgrinberg/flack)

## Running the application

To run the application, first install the app dependencies:

```bash
pip install .[app]
```

### Server

You can then use the `gunicorn.sh` script to start, stop and check the status of the
app. For a lighter-weight server for testing run `python app.py`.

### API

To make a direct API request, use the `predict.sh` script.

### Frontend

To use the frontend, go to [localhost:5000](http://localhost:5000) and upload an image.