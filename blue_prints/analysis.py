from services.analysis import get_attack_analysis
from flask import Blueprint, jsonify

analysis_bp = Blueprint('analysis', __name__)


@analysis_bp.route('/api/attack/<int:year>', methods=['GET'])
def get_attack_city(year):
    result = get_attack_analysis(year)
    if result:
        return jsonify({
            'target_city': result['target_city'],
            'mission_count': result['mission_count']
        }), 200
    else:
        return jsonify({'message': 'No data found for the given year'}), 404
