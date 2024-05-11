# OpenHumanize Complete API Reference

This detailed reference includes every component of the OpenHumanize project, covering Python scripts, configuration files, dependencies, batch files, and web resources.

## Table of Contents
- [Configuration Files](#configuration-files)
  - [.env.temp](#envtemp)
  - [requirements.txt](#requirementstxt)
- [Python Scripts](#python-scripts)
  - [app.py](#apppy)
  - [routes.py](#routespy)
  - [utils.py](#utilspy)
  - [kill_flask.py](#kill_flaskpy)
- [Batch Files](#batch-files)
  - [setup.bat](#setupbat)
  - [start.bat](#startbat)
- [Web Resources](#web-resources)
  - [Static Content](#static-content)
  - [HTML Templates](#html-templates)

## Configuration Files

### .env.temp
Defines environment variables to configure the application behavior dynamically.
- **SPACY_MODEL=en_core_web_sm**: Specifies the default spaCy NLP model used for text processing tasks like tokenization and named entity recognition. This model is lightweight and ideal for basic NLP tasks.

### requirements.txt
Lists the Python packages that need to be installed to run the application. Each package is vital for certain functionalities:
- **Flask==3.0.3**: Flask is a micro web framework for building web applications in Python. It is used to handle HTTP requests, route URLs, and render templates.
- **spacy==3.7.4**: Provides robust tools for advanced natural language processing. Used for processing and analyzing text.
- **python-dotenv==1.0.1**: Loads environment variables from a `.env` file, allowing configuration settings to be separated from code.
- **psutil==5.9.8**: Used in the kill_flask.py script to manage and terminate processes based on certain criteria, particularly for controlling Flask server instances.

## Python Scripts

### app.py
Initializes the Flask application and integrates various components.
- **Functions:**
  - **create_app()**: Sets up the Flask application.
    - **Arguments:** None
    - **Returns:** A configured Flask app instance.
    - **Details:** Initializes the Flask app with static path configurations and registers routes by calling `configure_routes()` from `routes.py` with the loaded NLP model.

### routes.py
Manages URL routing for the Flask application.
- **Functions:**
  - **configure_routes(app, nlp_model)**: Attaches URL routes to the Flask app.
    - **Arguments:**
      - `app`: Instance of Flask. Acts as the central object for configuring routes and handling requests.
      - `nlp_model`: The loaded spaCy NLP model used for processing text.
    - **Returns:** None
    - **Endpoints:**
      - **GET /**: Home page. Uses Flask's `render_template()` to serve the `index.html` page.
      - **POST /process**: Processes input text, tokenizes it using the spaCy model, and returns the results both as JSON and within a rendered HTML template.

### utils.py
Provides utility functions related to the spaCy NLP model.
- **Functions:**
  - **load_spacy_model()**: Loads the NLP model specified in the environment.
    - **Arguments:** None
    - **Returns:** A loaded spaCy model object.
    - **Details:** Checks for the model specified in the environment variable `SPACY_MODEL`. Loads it using spaCy's `load()` function, handling any exceptions related to model loading.

### kill_flask.py
Contains functions to terminate Flask server processes.
- **Functions:**
  - **find_and_kill_flask(identifier, port)**: Searches for and terminates Flask processes.
    - **Arguments:**
      - `identifier`: A string identifier to locate the correct Flask process.
      - `port`: The port number on which the Flask server is running.
    - **Returns:** Boolean. True if a process was found and killed, False otherwise.
    - **Details:** Iterates over all system processes, matching by command line arguments to the identifier and port. Uses `psutil` to safely terminate the process.

## Batch Files

### setup.bat
Automates the setup of the Python development environment.
- **Details:** Checks for Python installation, sets up a virtual environment using Python's `venv` module, activates the environment, and installs dependencies listed in `requirements.txt`.

### start.bat
Handles starting the application in a prepared environment.
- **Details:** Activates the Python virtual environment, installs any missing dependencies from `requirements.txt`, and starts the Flask application by running `app.py`. Includes error checks at each step to ensure smooth operation.

## Web Resources

### Static Content
#### styles.css
Located in the `static` directory, provides CSS for styling the web interface.

### HTML Templates
#### index.html
Main user interface for the OpenHumanize web application, located in the `templates` directory. Includes HTML forms for user input and areas to display processed results.