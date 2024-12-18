import requests
import os

def fetch_muscles(type='list'):
    try:
        url = f"https://wger.de/api/v2/muscle.json/"
        response = requests.get(url)
        results = response.json()["results"]
        results = {m["name_en"].lower() if m["name_en"] else m["name"].lower(): m["id"] for m in results}
        if type == 'list':
            return list(results.keys())
        return results
    except:
        return None

def fetch_exercises_by_muscle(muscle_id, language=2,max_tokens=5000):
    try:
        url = f"https://wger.de/api/v2/exercise.json"
        params = {"muscles": muscle_id, "language": language}
        response = requests.get(url,params=params)
        return response.json()["results"][:max_tokens]
    except:
        return None

def exercises_for_muscle(muscle_name):
    muscles = fetch_muscles('dict')
    muscle_id = muscles.get(muscle_name.lower())
    if not muscle_id:
        return f"Muscle '{muscle_name}' not found. the available muscles are {[muscle_name.lower() for muscle_name in muscles.keys()]}"
    exercises = fetch_exercises_by_muscle(muscle_id)
    if exercises:
        result = "\n".join([e['name'] for e in exercises])
        return result
    else:
        return f"No exercises found for muscle '{muscle_name}'."

#?-------------------------------------------------------------

def motivational_quotes():
    url = "https://motivation-quotes4.p.rapidapi.com/api"
    headers = {
    	"x-rapidapi-key": '6a04e8c324mshbd69bc094663974p19f2adjsn6eead4e5eca6',
    	"x-rapidapi-host": "motivation-quotes4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.json()['quote']
