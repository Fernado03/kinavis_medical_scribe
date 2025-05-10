from flask import Blueprint, jsonify, request, current_app
import mysql.connector

api_bp = Blueprint('api', __name__)

def get_db_connection_from_app_context():
    # Helper to get connection from app context if needed by blueprint
    # This assumes get_db_connection is attached to current_app or accessible
    # For simplicity, directly using app config here, but in larger apps
    # you might pass the db connection or a session to routes.
    conn = mysql.connector.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['MYSQL_USER'],
        password=current_app.config['MYSQL_PASSWORD'],
        database=current_app.config['MYSQL_DB'],
        # cursorclass=current_app.config.get('MYSQL_CURSORCLASS') # This will fail if not set
    )
    # Ensure cursorclass is used if defined, otherwise default behavior
    if current_app.config.get('MYSQL_CURSORCLASS') == 'DictCursor':
        # mysql.connector uses dictionary=True for DictCursor behavior
        conn.config(dictionary=True)
    return conn

@api_bp.route('/clinicians', methods=['GET'])
def get_clinicians():
    try:
        conn = get_db_connection_from_app_context()
        cursor = conn.cursor(dictionary=True) # Ensure dictionary cursor for this route
        cursor.execute("SELECT clinician_id, first_name, last_name, specialty, contact_phone, contact_email FROM Clinicians")
        clinicians = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(clinicians), 200
    except mysql.connector.Error as err:
        # Log error: current_app.logger.error(f"Database error: {err}")
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
        # Log error: current_app.logger.error(f"An unexpected error occurred: {e}")
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
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
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
        # current_app.logger.error(f"Database error during patient creation: {err}")
        return jsonify({"error": "Database error", "details": str(err)}), 500
    except Exception as e:
        # current_app.logger.error(f"Unexpected error during patient creation: {e}")
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