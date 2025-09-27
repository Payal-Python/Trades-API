# Trade Management API (Django + DRF)

This is a sample Django REST API for managing trade records. It demonstrates:
- Django REST Framework ViewSet-based CRUD API
- JWT Authentication (SimpleJWT)
- SQLite for demo (swap to PostgreSQL by setting DATABASE env vars)
- Dockerfile for containerised deployment

## Quickstart (local)
1. Create a virtualenv and activate it
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
2. Run migrations and create a superuser
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Run server
   ```bash
   python manage.py runserver
   ```
4. Get token (using POST to /api/auth/token/ with username/password) and call endpoints:
   - `GET /api/trades/` (requires token in Authorization: Bearer <token>)
   - `POST /api/trades/` to create trade

## Notes
- For production, configure SECRET_KEY, DEBUG, ALLOWED_HOSTS, and use PostgreSQL.
- Replace SQLite with PostgreSQL if connecting to real data.
