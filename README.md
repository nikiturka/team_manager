# Test Task - Python Developer at MB Digital

## Installation
clone:
```shell
git clone https://github.com/nikiturka/team_manager
```
switch to the project folder:
```shell
cd team_manager
```
Building the docker image:
```
docker-compose build
```

Raising docker-compose:
```
docker-compose up
```

## Project Overview
* **CRUD Operations**: Implemented using ModelViewSet, which provides complete functionality for creating, reading, updating,
and deleting resources.


* **Team Membership Management**: Adding and removing persons from teams is handled by TeamMembershipViewSet. This choice
was made because PersonViewSet requires a single serializer for all operations, which can be inconvenient when only a limited
set of fields is needed for certain actions. Additionally, using separate methods helps avoid potential overload in a
single method as logic expands in the future, ensuring clearer structure and maintainability.


* The <kbd>.env</kbd> file is included in <kbd>.gitignore</kbd>, but for demonstration purposes, I've provided an
<kbd>.env.example</kbd> file to ensure everything works correctly.


* A dedicated test database has been set up for running tests, located in <kbd>team_manager/test_settings.py</kbd>.
This allows for isolated testing without affecting the production database.