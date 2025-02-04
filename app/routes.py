import os
from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

SCRIPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "scripts"))

@routes.route('/scripts', methods=['GET'])
def list_scripts():
    """Devuelve la lista de scripts disponibles en la carpeta 'scripts/'"""
    try:
        scripts = [f for f in os.listdir(SCRIPTS_DIR) if f.endswith('.sh')]
        return jsonify({"scripts": scripts})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
