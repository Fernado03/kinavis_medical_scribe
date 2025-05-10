import os
from flask import Flask, jsonify, request
import mysql.connector
from .config import config
from .api_routes import api_bp
import whisper
from dotenv import load_dotenv

load_dotenv()

def create_app(config_name=os.getenv('FLASK_CONFIG') or 'default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Load Whisper model on app startup and attach it to the app context
    try:
        app.whisper_model = whisper.load_model(app.config.get('WHISPER_MODEL', 'base'))
        app.logger.info(f"Whisper model '{app.config.get('WHISPER_MODEL', 'base')}' loaded successfully.")
    except Exception as e:
        app.logger.error(f"Error loading Whisper model: {e}")
        app.whisper_model = None

    def get_db_connection():
        conn = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        return conn

    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def hello_world():
        return 'Hello, World! AI Medical Scribe Backend is running.'

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

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config.get('DEBUG', True))
