# Achool API

## What is it?

A REST API implementing CRUD operations for a school entity with students.

## The Latest Version
This API is currently at Version 1.0 (the first version).

## Installation
Clone the repo
```
https://github.com/alexkiura/school_api.git
```

Navigate to the root folder
```
cd school_api
```
Install the necessary packages
```

pip install -r requirements.txt
```



## Perform migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Testing
To run the tests for the API
```
python manage.py test
```

## REST API
School API has a RESTful Application Program Interface (API)

### School API's resources
The API resources are accessible at [localhost:8000/api/v1/](http://127.0.0.1:8000/api/v1.0/). They include:

| Resource URL | Methods | Description |
| -------- | ------------- | --------- |
| `/api/v1/` | GET  | The index |
| `/api/v1/schools/` | GET, POST | Schools |
| `/api/v/schools/<id>/` | GET, PUT, DELETE | A single school |
| `/api/v1/students/` | GET, POST | Students |
| `/api/v1/students/<id>/` | GET, PUT, DELETE| A single student |


| Method | Description |
|------- | ----------- |
| GET | Retrieves a resource(s) |
| POST | Creates a new resource |
| PUT | Updates an existing resource |
| DELETE | Deletes an existing resource |


## Built with
[Django](https://www.djangoproject.com/) |
[Django REST](http://www.django-rest-framework.org/) |


## Author
[![Alex Kiura](http://0.gravatar.com/avatar/ea50741579447e4a8dcd743e10c25fd7?s=144)](https://github.com/andela-akiura)


## License

### The MIT License (MIT)

Copyright (c) 2017 Alex Kiura <alex.kiura@andela.com>

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
