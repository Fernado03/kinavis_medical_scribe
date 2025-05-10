# AI Medical Scribe - Backend

This directory contains the Flask backend for the AI Medical Scribe application.

## Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    ```
2.  **Activate the virtual environment:**
    *   Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
    *   Windows (Git Bash/CMD): `.\.venv\Scripts\activate`
    *   macOS/Linux: `source .venv/bin/activate`
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    Create a `.env` file in this `backend` directory with the following (adjust as necessary, especially for production):
    ```
    FLASK_APP=app.py
    FLASK_ENV=development # or production
    SECRET_KEY=your_very_secret_random_key_here 
    MYSQL_HOST=localhost
    MYSQL_USER=your_db_user
    MYSQL_PASSWORD=your_db_password
    MYSQL_DB=ai_medical_scribe 
    ```
    *Note: Ensure the `MYSQL_DB` matches the database created by `schema.sql` and that the user has appropriate permissions.*

## Running the Application

Once the setup is complete and the virtual environment is activated:

```bash
flask run
```

The application will typically be available at `http://127.0.0.1:5000/`.

## API Endpoints

-   `GET /api/clinicians`: Returns a list of all clinicians.
-   `GET /api/patients`: Returns a list of all patients. Supports `?search=<name>` query parameter.
-   `POST /api/patients`: Creates a new patient. Expects JSON body with `first_name`, `last_name`, `date_of_birth`, `gender`, and optional `contact_phone`, `contact_email`.
-   `POST /api/encounters`: (Stub) Accepts `clinician_id` and `patient_id` for future encounter creation.
