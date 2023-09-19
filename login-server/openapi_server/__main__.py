#!/usr/bin/env python3

import connexion
from openapi_server.config import Config
from openapi_server import encoder
from openapi_server.models.db import db
from openapi_server.models.db_models import User
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from prometheus_flask_exporter import ConnexionPrometheusMetrics
def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.config.from_object(Config)
    metrics = ConnexionPrometheusMetrics(app)
    jwt = JWTManager()
    jwt.init_app(app.app)
    db.init_app(app.app)
    with app.app.app_context():
        db.create_all()
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Login API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
