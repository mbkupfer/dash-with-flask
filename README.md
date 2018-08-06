# dash-with-flask
Simple example of integrating [Dash](https://plot.ly/products/dash/) into the flask framework.

This is a demonstration on how to get [Dash](https://plot.ly/products/dash/) working inside of a flask framework. Dash is a fantastic library for those that want to create dashboard interfaces while still staying within the python domain language.

I created this because I myself had trouble figuring out this setup given the documentation out there. From the plotly forums to the documentation for werkzeug, flask and dash, none had a complete living example that tied it all together. *Although, some were quite helpful in helping me get there*

## Instructions:

`git clone https://github.com/mbkupfer/dash-with-flask.git`

`cd dash-with-flask.git`

`python3 -m venv venv`

On Windows:

`py -3 -m venv venv`

**Activate the environment**

`. venv/bin/activate`

On Windows:

`venv\Scripts\activate`

You know your virtual environment is active when you see the `(venv)` at the beginning of the CLI line.

`(venv) C:\Users\user\path_to\dash-with-flask>`

**Install requirements**

`pip install -r requirements.txt`

**Run code**

`python main.py`

This should launch the application on your localhost as such:

```
* Restarting with stat
* Running on http://localhost:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [06/Aug/2018 13:40:23] "GET / HTTP/1.1" 200 -
```

Navigating to http://localhost:5000/my-app will launch the dash application.

## Future:
This is part of a larger project in which I'm trying to learn about web app development. I'm planning on refining this repository with new branches to showcase other web app architectures that incorporate dash. 
