from flask import Flask
from app.routes.user import user_bp
from app.db import get_connection
from sqlalchemy import text

def create_app():
    app = Flask(__name__)

    # Blueprint 등록
    app.register_blueprint(user_bp)

    # health
    @app.route("/health")
    def health():
        return {"status": "ok"}

    # db-test
    @app.route("/db-test")
    def db_test():
        conn = None
        try:
            conn = get_connection()
            result = conn.execute(text("SELECT 1"))
            data = [row[0] for row in result]

            return {"status": "ok", "result": data}

        except Exception as e:
            return {"status": "error", "message": str(e)}

        finally:
            if conn:
                conn.close()

    return app

