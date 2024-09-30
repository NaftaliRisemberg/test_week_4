from sqlalchemy import text
from db import db


def get_attack_analysis(year):
    query = text("""
        SELECT 
            l.loc_city,
            COUNT(*) AS mission_count
        FROM 
            mission m 
        INNER JOIN 
            location l ON m.location_id = l.location_id 
        WHERE 
            EXTRACT(YEAR FROM m.mission_date) = :year
        GROUP BY 
            l.loc_city
        ORDER BY 
            mission_count DESC
        LIMIT 1;
    """)

    result = db.session.execute(query, {'year': year})
    data = result.fetchone()

    if data:
        return {
            'target_city': data[0],
            'mission_count': data[1]
        }
    else:
        return None

