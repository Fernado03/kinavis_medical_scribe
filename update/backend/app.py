import os
from flask import Flask, jsonify, request, Blueprint
import mysql.connector
from .config import config
import whisper  # Import the Whisper library
from dotenv import load_dotenv

load_dotenv()

def create_app(config_name=os.getenv('FLASK_CONFIG') or 'default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Load Whisper model on app startup
    app.whisper_model = whisper.load_model(app.config.get('WHISPER_MODEL', 'base'))

    def get_db_connection():
        conn = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        return conn

    @app.route('/')
    def hello_world():
        return 'Hello, World! AI Medical Scribe Backend is running.'

    # Import and register the API blueprint
    from .api_routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/test-db')
    def test_db_connection():
        messages = []
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            messages.append("Successfully connected to the database.")

            # Execute schema.sql
            try:
                with open('schema.sql', 'r') as f:
                    sql_schema = f.read()
                for statement in sql_schema.split(';'):
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
                conn.commit()
                messages.append("Successfully executed schema.sql.")
            except Exception as e:
                messages.append(f"Error executing schema.sql: {str(e)}")
                conn.rollback()
                return jsonify({"status": "error", "messages": messages}), 500

            # Execute sample_clinicians.sql
            try:
                with open('sample_clinicians.sql', 'r') as f:
                    sql_sample_data = f.read()
                for statement in sql_sample_data.split(';'):
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
                conn.commit()
                messages.append("Successfully executed sample_clinicians.sql.")
            except Exception as e:
                messages.append(f"Error executing sample_clinicians.sql: {str(e)}")
                conn.rollback()
                return jsonify({"status": "error", "messages": messages}), 500

            cursor.close()
            conn.close()
            return jsonify({"status": "success", "messages": messages})

        except mysql.connector.Error as err:
            messages.append(f"Database connection error: {err}")
            return jsonify({"status": "error", "messages": messages}), 500
        except Exception as e:
            messages.append(f"An unexpected error occurred: {str(e)}")
            return jsonify({"status": "error", "messages": messages}), 500

    # Define the /api/transcribe-audio route here or in api_routes.py
    @app.route('/api/transcribe-audio', methods=['POST'])
    def transcribe_audio():
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        audio_file = request.files['audio']
        temp_audio_path = "temp_audio_" + audio_file.filename
        try:
            audio_file.save(temp_audio_path)
            result = app.whisper_model.transcribe(temp_audio_path)
            os.remove(temp_audio_path)
            return jsonify({"transcription": result["text"]})
        except Exception as e:
            os.remove(temp_audio_path)
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config.get('DEBUG', True))
