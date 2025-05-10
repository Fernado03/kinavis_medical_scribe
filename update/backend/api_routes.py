from flask import Blueprint, jsonify, request, current_app
import mysql.connector
import os
import whisper

api_bp = Blueprint('api', __name__)

def get_db_connection_from_app_context():
    """Helper to get database connection from the Flask application context."""
    conn = mysql.connector.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['MYSQL_USER'],
        password=current_app.config['MYSQL_PASSWORD'],
        database=current_app.config['MYSQL_DB'],
    )
    if current_app.config.get('MYSQL_CURSORCLASS') == 'DictCursor':
        conn.config(dictionary=True)
    return conn

@api_bp.route('/clinicians', methods=['GET'])
def get_clinicians():
    try:
        conn = get_db_connection_from_app_context()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT clinician_id, first_name, last_name, specialty, contact_phone, contact_email FROM Clinicians")
        clinicians = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(clinicians), 200
    except mysql.connector.Error as err:
        current_app.logger.error(f"Database error: {err}")
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
        current_app.logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@api_bp.route('/patients', methods=['GET'])
def get_patients():
    search_term = request.args.get('search')
    try:
        conn = get_db_connection_from_app_context()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT patient_id, first_name, last_name, date_of_birth, gender, contact_phone, contact_email FROM Patients"
        params = []
        if search_term:
            query += " WHERE first_name LIKE %s OR last_name LIKE %s"
            params.extend([f"%{search_term}%", f"%{search_term}%"])

        cursor.execute(query, tuple(params))
        patients = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(patients), 200
    except mysql.connector.Error as err:
        current_app.logger.error(f"Database error: {err}")
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
        current_app.logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@api_bp.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data"}), 400

    required_fields = ['first_name', 'last_name', 'date_of_birth', 'gender']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": "Missing required fields", "missing": missing_fields}), 400

    try:
        conn = get_db_connection_from_app_context()
        cursor = conn.cursor(dictionary=True)

        query = """
            INSERT INTO Patients (first_name, last_name, date_of_birth, gender, contact_phone, contact_email)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            data['first_name'],
            data['last_name'],
            data['date_of_birth'],
            data['gender'],
            data.get('contact_phone'), # Optional
            data.get('contact_email')  # Optional
        )

        cursor.execute(query, params)
        new_patient_id = cursor.lastrowid
        conn.commit()

        cursor.execute("SELECT patient_id, first_name, last_name, date_of_birth, gender, contact_phone, contact_email FROM Patients WHERE patient_id = %s", (new_patient_id,))
        new_patient = cursor.fetchone()

        cursor.close()
        conn.close()

        if new_patient:
            return jsonify(new_patient), 201
        else:
            return jsonify({"error": "Failed to retrieve created patient"}), 500

    except mysql.connector.Error as err:
        current_app.logger.error(f"Database error during patient creation: {err}")
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
        current_app.logger.error(f"Unexpected error during patient creation: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@api_bp.route('/encounters', methods=['POST'])
def create_encounter_stub():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data"}), 400

    clinician_id = data.get('clinician_id')
    patient_id = data.get('patient_id')

    if not clinician_id or not patient_id:
        return jsonify({"error": "Missing clinician_id or patient_id"}), 400

    # This is a stub. In a real implementation, you would create an encounter record.
    # For now, just return the received IDs to confirm they can be passed.
    return jsonify({
        "message": "Encounter creation stub successful",
        "clinician_id": clinician_id,
        "patient_id": patient_id
    }), 201

@api_bp.route('/transcribe-audio', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    temp_audio_path = f"temp_audio_{audio_file.filename}"
    try:
        audio_file.save(temp_audio_path)
        whisper_model = current_app.whisper_model # Access the loaded Whisper model from the app context
        result = whisper_model.transcribe(temp_audio_path)
        os.remove(temp_audio_path)
        return jsonify({"transcription": result["text"]})
    except Exception as e:
        os.remove(temp_audio_path)
        current_app.logger.error(f"Error during audio transcription: {e}")
        return jsonify({"error": "Error during audio transcription", "details": str(e)}), 500
