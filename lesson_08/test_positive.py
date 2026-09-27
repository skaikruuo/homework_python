import requests

base_url = "https://ru.yougile.com/api-v2/projects"

payload = {
    "login": "",
    "password": "",
    "companyId": ""
}
headers = {"Content-Type": "application/json"}
response = requests.request("POST", base_url + '/auth/keys', json=payload, headers=headers)
print(response.text)

def test_add():
    payload = {
        "title": "Task",
        "users": {
            "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
            "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
        },
        "departments": {"4902b994-b806-4af4-acec-018ea5ea6468": {
                "manager": "admin",
                "member": "worker"
            }},
        "idempotencyKey": "string"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer OWjz-hE8a4Ia5hBeENOzqnCEXmXx6X8KB0KJCd30Cggsk8gblsm4s4P-sS0tk3hc"
}
    response = requests.request("POST", base_url, json=payload, headers=headers)
    print(response.text)

def test_change():
    payload = {
        "deleted": True,
        "title": "Task-007",
        "users": {
            "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
            "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
        },
        "departments": {"4902b994-b806-4af4-acec-018ea5ea6468": {
                "manager": "admin",
                "member": "worker"
            }}
}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer OWjz-hE8a4Ia5hBeENOzqnCEXmXx6X8KB0KJCd30Cggsk8gblsm4s4P-sS0tk3hc"
}
    response = requests.request("PUT", base_url + '/90678b93-7541-4754-9494-8e04bb802514', json=payload, headers=headers)
    print(response.text)

def test_get():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer OWjz-hE8a4Ia5hBeENOzqnCEXmXx6X8KB0KJCd30Cggsk8gblsm4s4P-sS0tk3hc"
}
    response = requests.request("GET", base_url + '/90678b93-7541-4754-9494-8e04bb802514', headers=headers)
    print(response.text)
