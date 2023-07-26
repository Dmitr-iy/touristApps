# :mountain_cableway: ***TouristApp API***
__

<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.10-brightgreen?style=plastic&logo=python&logoColor=green">
<img alt="Static Badge" src="https://img.shields.io/badge/rest_framework-3.14-brightgreen?style=plastic&logo=django&logoColor=green&cacheSeconds=3600">
<img alt="Static Badge" src="https://img.shields.io/badge/postgreSQL-14-brightblue?style=plastic&logo=postgresql&logoColor=blue&labelColor=grey&color=blue&cacheSeconds=3600">

:mount_fuji: ___API for posting information about passes___

# Usage

___A tourist through a mobile application enters the necessary information about the pass.
The request will call the submitData method of this REST API.
The submitData method accepts JSON in the request body, an example of this JSON:___


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