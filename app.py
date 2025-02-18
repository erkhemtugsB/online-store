from flask import Flask
from config import Config
from models.product import db  # ✅ Import only db, not Product

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models.product import Product  # ✅ Import inside app context to avoid circular import
        db.create_all()  # Ensure tables are created

    # Register Blueprints
    from routes.auth import auth_bp
    from routes.products import products_bp
    from routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
