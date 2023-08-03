# :sunrise: ***TouristApp API***
_______________________

<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.10-brightgreen?style=plastic&logo=python&logoColor=green">  <img alt="Static Badge" src="https://img.shields.io/badge/rest_framework-3.14-brightgreen?style=plastic&logo=django&logoColor=green&cacheSeconds=3600"> <img alt="Static Badge" src="https://img.shields.io/badge/postgreSQL-14-brightblue?style=plastic&logo=postgresql&logoColor=blue&labelColor=grey&color=blue&cacheSeconds=3600"> <img alt="Static Badge" src="https://img.shields.io/badge/coverage-green?style=plastic">

## :mount_fuji: ___API for posting information about passes___

# Usage

__Tourist through a mobile application, in JSON format, enters the necessary information about the pass.
Example:__


```Json
{
    "id": 3,
    "user": {
        "id": 4,
        "first_name": "Hanna",
        "surname": "Dmitrievna",
        "last_name": "Ivanova",
        "email": "ivanova@googl.com",
        "phone": "877777777777"
    },
    "level": {
        "id": 3,
        "autumn": "",
        "spring": "",
        "summer": "1A",
        "winter": ""
    },
    "coords": {
        "id": 3,
        "latitude": 777.01,
        "longitude": 458.256,
        "height": 456
    },
    "images": [
        {
            "id": 3,
            "images": "https://ru...com/pe_6199184.htm",
            "title": "https://ru...background-old-brown.htm"
        }
    ],
    "beautyTitle": "pass",
    "title": "Phiy",
    "other_titles": "Triev",
    "connect": " ! ",
    "add_time": "2023-07-26T16:55:34.433081Z",
    "status": "New"
}
```
## ___Method Result:___

### ___JSON___

```Json
{"status": 500, "message": "Error connecting to database", "id": None}

{"status": 400, "message": "Bad request", "id": None}

{"status": 200, "message": "The record was successfully added to the database", "id": 2}
```

__The record can be edited, except for the user's melons 
(Last name, first name, surname, email and phone number).
You can get a list of data about all objects that the user with mail <email> sent to the server. 
You can also get one record about the pass by its 'id'.__   
 ___
___
#### :link: _URL swagger:  <http://kosheldmitriy.pythonanywhere.com/swagger/>

#### :link: _URL to 3-Panel Responsive Layout: <http://kosheldmitriy.pythonanywhere.com/redoc/>_
>#### The left panel contains the search bar and the navigation menu.
>>#### The central panel contains documentation.
>>> #### The right panel contains sample requests and responses.  
---
___
## :rocket:To run on the local machine, compile the project:
###### commands for OC Linux
   ```zsh
     $ git clone https://github.com/Dmitr-iy/touristApps.git
   ```

### Create and activate a virtual environment:
   ```zsh
     $ python3 -m venv env
   ```

   ```zsh
     $ source /env/bin/activate
   ```

### Update pip if necessary:
   ```zsh
     $ pip install --upgrade pip
   ```

### Install dependencies:
   ```zsh
     $ pip install -r requirements.txt
   ```

### Edit the settings.py file:
```python
SECRET_KEY = ''

DATABASES = ''
```

### Do migrations:
  ```zsh
    $ python manage.py makemigrations
  ```

  ```zsh
    $ python manage.py migrate
  ```  

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="icon" sizes="32x32" href="favicon_32.png">
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body class="indexfile">
<header>
    <div class="content">
        <h1>Coverage report:
            <span class="pc_cov">96%</span>
        </h1>
        <aside id="help_panel_wrapper">
            <label for="help_panel_state">
            </label>
            <div id="help_panel">
                <p class="legend"></p>
                <div class="keyhelp">
                </div> 
</header>
<main id="index">
    <table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="manage_py.html">manage.py</a></td>
                <td>12</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="10 12">83%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821___init___py.html">pereval/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821_admin_py.html">pereval/admin.py</a></td>
                <td>7</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="7 7">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821_apps_py.html">pereval/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_fa052a3afecd0863_0001_initial_py.html">pereval/migrations/0001_initial.py</a></td>
                <td>6</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="6 6">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_fa052a3afecd0863___init___py.html">pereval/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821_models_py.html">pereval/models.py</a></td>
                <td>33</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="33 33">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821_serializers_py.html">pereval/serializers.py</a></td>
                <td>73</td>
                <td>6</td>
                <td>0</td>
                <td class="right" data-ratio="67 73">92%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02845a9cb66c5629___init___py.html">pereval/tests/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02845a9cb66c5629_testApi_py.html">pereval/tests/testApi.py</a></td>
                <td>111</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="111 111">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821_urls_py.html">pereval/urls.py</a></td>
                <td>6</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="6 6">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_263dc8d62a331821_views_py.html">pereval/views.py</a></td>
                <td>26</td>
                <td>3</td>
                <td>0</td>
                <td class="right" data-ratio="23 26">88%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_cd1396f5687bc750___init___py.html">tourist/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_cd1396f5687bc750_settings_py.html">tourist/settings.py</a></td>
                <td>23</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="23 23">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_cd1396f5687bc750_urls_py.html">tourist/urls.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>305</td>
                <td>11</td>
                <td>0</td>
                <td class="right" data-ratio="294 305">96%</td>
            </tr>
        </tfoot>
    </table>
</main>
<footer>
    <div class="content">
        <p>
            <a class="nav" href="https://coverage.readthedocs.io/en/7.2.7">coverage.py v7.2.7</a>,
        </p>
    </div>
    <aside class="hidden">
        <a id="prevFileLink" class="nav" href="d_cd1396f5687bc750_urls_py.html"/>
        <a id="nextFileLink" class="nav" href="manage_py.html"/>
        <button type="button" class="button_prev_file" data-shortcut="["/>
        <button type="button" class="button_next_file" data-shortcut="]"/>
        <button type="button" class="button_show_hide_help" data-shortcut="?"/>
    </aside>
</footer>
</body>
</html>

_____


