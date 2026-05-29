# Urban Grocers — API Automated Test Suite

Python + requests test suite for backend validation of the Urban Grocers 
kit creation API. 9 tests cover boundary values, special input types, 
and error handling for the `name` field — validating that the API enforces 
business rules at every input boundary.

---

## What's Being Tested

**Endpoint:** `POST /api/v1/kits`
**Field under test:** `name` (kit name, string)
**Valid range:** 1–511 characters

| Test | Input | Expected Status |
|---|---|---|
| Minimum valid length | 1 character | 201 Created |
| Maximum valid length | 511 characters | 201 Created |
| Over maximum | 512 characters | 400 Bad Request |
| Special characters | `!@#$%` | 201 Created |
| Spaces | `" "` | 201 Created |
| Numbers as string | `"123"` | 201 Created |
| Empty string | `""` | 400 Bad Request |
| Missing `name` field | — | 400 Bad Request |
| Wrong type (integer) | `123` | 400 Bad Request |

---

## Architecture
qa-project-Urban-Grocers-app-es/
├── test.py            # Test cases
├── utilities.py       # HTTP call handlers (GET/POST)
├── data.py            # Test data and request headers
├── configuration.py   # Server URL and endpoint paths
├── README.md
└── .gitignore

**Shared assertion helpers** reduce duplication across tests:

```python
def positive_assert(name):
    """Validates a 201 response and confirms name persistence."""
    auth_token = get_new_user_token()
    response = utilities.post_new_client_kit(set_card_name(name), auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == name

def negative_assert_symbol(name):
    """Validates a 400 response for invalid name inputs."""
    auth_token = get_new_user_token()
    response = utilities.post_new_client_kit(set_card_name(name), auth_token)
    assert response.status_code == 400
```

Each test calls one of these two functions — keeping test cases 
focused on input data, not assertion logic.

---

## Key Technical Decisions

**Boundary value focus**
The test suite targets the 1/511/512 character boundaries — the 
values most likely to expose missing validation logic. This mirrors 
the boundary value analysis technique used in manual API testing.

**Auth token per test**
Each test generates a fresh auth token via `get_new_user_token()`, 
ensuring test independence and preventing state pollution between runs.

**Centralized endpoint configuration**
All URLs and paths live in `configuration.py`. Environment changes 
require no modifications to test logic.

---

## Setup

**Prerequisites**
- Python 3.14+
- Git

**Install dependencies**
```bash
pip install requests pytest
```

**Configure server URL**

Open `configuration.py` and update:
```python
URL_SERVICE = "https://your-server-url"
```

**Run all tests**
```bash
pytest test.py -v
```

**Run a specific test**
```bash
pytest test.py::test_create_kit_1_letter_in_name_get_success_response -v
```

---

## Tech Stack

| Tool | Version |
|---|---|
| Python | 3.14+ |
| requests | Latest |
| pytest | Latest |
| API | REST / JSON |
