from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializar o SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Configuração da chave secreta para JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_secret_key_here')

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
                                                      'postgresql://username:password@localhost/flowcommerce_auth_db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializando o JWT Manager e SQLAlchemy
    jwt = JWTManager(app)
    db.init_app(app)

    # Registrando Blueprints (módulos de rotas)
    from auth.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    # Tratamento Global de Erros
    @app.errorhandler(Exception)
    def handle_exception(e):
        response = {
            "message": "An unexpected error occurred.",
            "details": str(e)
        }
        return jsonify(response), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
