import requests

base_url = "https://ru.yougile.com/api-v2/projects"


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
    response = requests.request("POST", base_url, json=payload, headers=head)
    assert response.status_code == 400

def test_change():
    payload = {
        "title": "",
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
    response = requests.request("PUT", url, json=payload, headers=headers)
    assert response.status_code == 400

def test_get():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer OWjz-hE8a4Ia5hBeENOzqnCEXmXx6X8KB0KJCd30Cggsk8gblsm4s4P-sS0tk3hc"
}
    response = requests.request("DELETE", base_url + '/90678b93-7541-4754-9494-8e04bb802514', headers=headers)
    assert response.status_code == 400