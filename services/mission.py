from models import Mission

def get_all_missions():
    missions = Mission.query.all()
    if missions:
        return [mission.to_dict() for mission in missions]
    else:
        return None

def get_mission_by_id(mission_id):
    mission = Mission.query.get(mission_id)
    if mission:
        return mission.to_dict()
    else:
        return None

