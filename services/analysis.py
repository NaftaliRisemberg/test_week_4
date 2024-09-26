from db import db

def get_attack_analys(year):
    query = """
        SELECT 
            air_force,
            target_city,
            COUNT(*) AS mission_count
        FROM mission
        WHERE EXTRACT(YEAR FROM mission_date) = :year
        GROUP BY air_force, target_city
        ORDER BY mission_count DESC
        LIMIT 1;
    """
    result = db.session.execute(query, {'year': year})
    data = result.fetchone()
    return data