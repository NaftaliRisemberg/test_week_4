from flask import Blueprint, jsonify, request
from db import db
from services.analysis import get_attack_analys

analysis_bp = Blueprint('analysis', __name__)

from flask import Blueprint, jsonify
from db import db  # ודא שאתה מייבא את ה-db שלך

analysis_bp = Blueprint('analysis', __name__)


@analysis_bp.route('/api/attack/<int:year>', methods=['GET'])
def get_attack_city(year):
    result = get_attack_analys(year)
    if result:
        return jsonify({
            'air_force': result['air_force'],
            'target_city': result['target_city'],
            'mission_count': result['mission_count']
        }), 200
    else:
        return jsonify({'message': 'No data found for the given year'}), 404
