from flask import Blueprint, jsonify
from services.mission import get_all_missions, get_mission_by_id

mission_bp = Blueprint('mission', __name__)

@mission_bp.route('/api/mission', methods=['GET'])
def get_missions():
    missions = get_all_missions()
    if missions:
        return jsonify(missions), 200
    else:
        return jsonify(f'not found any mission in the database')

@mission_bp.route('/api/mission/<int:id>', methods=['GET'])
def get_mission(id):
    mission = get_mission_by_id(id)
    if mission:
        return jsonify(mission), 200
    else:
        return jsonify({'error': 'Mission not found'}), 404



