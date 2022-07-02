# MusicAPI-Scraping-Redis-restframework
This API for Iranian music is made with Django Restframework, Web Scraping and redis.
You can use this API in your programs



![Untitled](https://user-images.githubusercontent.com/74909796/177000496-61cc4087-a516-409f-b47a-0278685e249b.png)

# Installation

First of all, you have to clone this repository to your local machine:
```bash
git clone https://github.com/Cmatrix1/MusicAPI-Scraping-Redis-restframework
```

install the project dependencies 
```bash
pip install -r requirement.txt
```

# Usage
- For use this API you should Run redis on port 6379
- Run Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Technologies used
- Django Restframework
- Redis
- Web Scraping (Bs4, requests)

# Testing
You can test the APIs with this command
```
python manage.py test
```
