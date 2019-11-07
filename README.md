## :high_brightness: OnlyYou
### : Automatic face replacement web service in pictures for portrait right protection using cycleGAN


> &#9989; &#10102; We generate faked faces to replace with other's faces in your pictures  :open_mouth::camera:

> &#9989; &#10103;  We take care of your original pictures and generated pictures  &#128140;

<!-- blank line -->
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.gpl-license.org)


## What you can see

**Result for Web Development**
- <img src="/img/web_result_1.png" width="450px" height="300px" title="web_result_1_pic" alt="Web Result Picture 1"></img>
- <img src="/img/web_result_2.png" width="450px" height="300px" title="web_result_2_pic" alt="Web Result Picture 2"></img>
- <img src="/img/web_result_5.png" width="450px" height="300px" title="web_result_3_pic" alt="Web Result Picture 3"></img>
- <img src="/img/web_result_3.png" width="450px" height="400px" title="web_result_4_pic" alt="Web Result Picture 4"></img>
- <img src="/img/web_result_4.png" width="450px" height="400px" title="web_result_5_pic" alt="Web Result Picture 5"></img>

**Result for Modeling**
- <img src="/img/modeling_result_1.png" width="450px" height="300px" title="modeling_result_1_pic" alt="Modeling Result Picture 1"></img><br>

## Installation

**Requirements**

Python : 3.7.0 or later (3.6 may compatible)

Opencv-Python : 4.0.0 or later

### Clone

- Clone this repo to your local machine using `https://github.com/sjly3k/Django.git`

### Dockerizing

- Later on

### Setup

To install the current release for Ubuntu server.
```bash
sudo apt update
sudo apt install git python3-venv libsm6 libxext6 libxrender1 ffmpeg

git clone https://github.com/sjly3k/Django.git
cd Server

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
#### *Try to run OnlyYou*
Add your public IP or DNS to allow hosts.

```bash
$ vim Server/settings
```

```python
ALLOWED_HOSTS = [
    'ADD YOUR PUBLIC IP or DNS',
    'localhost',
    '127.0.0.1',
]
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8080
```

## Features

> :thumbsup: 
>> `something`

> :astonished:

## Documentations

- Check out https://github.com/onlyyou-teamb/Documentations

## How to contribute

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/sjly3k/Django.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request 

---

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © sjly3k || OnlyYou-Team
