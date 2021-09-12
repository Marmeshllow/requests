from datetime import datetime, date, time
import requests
import json


def last_questions(tag='python', delay=2):
    to_date = int(datetime.combine(date.today(), time(0, 0, 0)).timestamp())
    from_date = to_date - delay * 86400
    url = f'https://api.stackexchange.com/2.3/questions'
    params = {"fromdate": from_date, "todate": to_date, 'order': 'desc',
              'sort': 'activity', 'tagged': tag, 'site': 'stackoverflow'}
    response = requests.get(url, params=params)
    file_name = str(date.today())+'.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4)
