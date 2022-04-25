# Flask sample API

A simplest REST API created using Python + Flask with RESTful framework. 

This API is about stores and items available on the stores.

## Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Project Structure](#structure)


## <a name="features"></a>Features

- Register / Authenticate users
- Manage stores (create, read, delete)
- Manage items available on stores (create, read, update, delete)


## <a name="structure"></a> Project Structure

```
root
├── models (entities on database)
│   ├── __init__.py          
│   ├── item.py          
│   ├── store.py
│   └── user.py  
├── resources (entities on API)
│   ├── __init__.py          
│   ├── item.py          
│   ├── store.py
│   └── user.py  
├── .gitignore
├── Procfile (required to deploy project on Heroku)
├── README.md
├── app.py (contain Flask app and Flask-RESTful Api)
├── db.py
├── run.py (run the app)
├── requirements.txt (required to install on environment)
├── runtime.txt
├── security.py
└── uwsgi.ini (wsgi config)
```

## <a name="quick-start"></a>Quick Start 

### Creates a Virtual Environment:

#### 1. Install virtualenv

```bash
pip install virtualenv

cd your_project_folder

virtualenv environment_name --python=3.9
```

#### 2. Activate the environment

Windows:
```bash
.\environment_name\Scripts\activate
```

Linux / Mac:
```bash
source environment_name/bin/activate
```

Result:
```bash
(environment_name) your_project_folder>
```

#### Deactivate the environment:
```bash
(environment_name) your_project_folder> deactivate
```

### Install the requirements on your environment:
```bash
pip install -r requirements.txt
```

### Requirements:
- Python 3.9
- Flask
- Flask-RESTful
- Flask-JWT
- Flask-SQLAlchemy
- uwsgi
- psycopg2

Also available in file `requirements.txt`
<br>

### Run the app in your PC:

1. In the file `app.py`:

- Change DEBUG config to True
```python
app.config['DEBUG'] = True
```

- Comment the `uri` variable lines :
```python
# uri = os.getenv("DATABASE_URL")
# 
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
```

2. Activate your virtual environment.
<br>

3. Execute the following command on prompt or shell:

```bash
python app.py
```