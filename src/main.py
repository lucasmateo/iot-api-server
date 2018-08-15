from flask import Flask, request
import os
import database.database as database

import blueprints.deviceBlueprint as deviceBp
import blueprints.testBlueprint as testBp
import blueprints.webBlueprint as webBp

app = Flask(__name__, static_url_path='')
port = int(os.getenv('PORT', 8001))

database.Database.getDatabase().connect();

app.register_blueprint(deviceBp.deviceBp)
app.register_blueprint(testBp.testBp)
app.register_blueprint(webBp.webBp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
