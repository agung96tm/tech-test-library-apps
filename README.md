Library Apps
==========================================
[![Test & Deploy](https://github.com/agung96tm/tech-test-library-apps/actions/workflows/main.yml/badge.svg)](https://github.com/agung96tm/tech-test-library-apps/actions/workflows/main.ymll)

Technical Test for Backend Engineer using the Django framework.

How to Run
-----------------
#### Run Application
```commandline
docker-compose -f deploy/local/docker-compose.yml up -d -build

cd src/project

python manage.py migrate
python manage.py runserver
```

#### Run Test
```commandline
cd src/project

python manage.py test
```

#### Run Formatter
```commandline
black .
isort .
```

#### Run Worker & Scheduler
```commandline
cd src/project

celery -A configs beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A configs worker -l info
```


Docs
--------------------------------
* [BetterToPractice: Initialize Django Rest](https://github.com/BetterToPractice/django-rest-setup)
* [Postman: Library Collection](https://www.postman.com/speeding-comet-3687/workspace/tech-tests-be/collection/2399435-0f8df135-02ea-4a89-bf6f-0c6f6bc5616e)