import os
import requests

key = os.environ.get('MSW_API_KEY')

def msw_loc(location):
    if (location.lower()) == 'croyde' :
        id = 7
        return id
    elif (location.lower()) == 'newquay':
        id = 1361
        return id
    else:
        return "Location not available"

def msw_res(key, id):
        response = requests.get(f'http://magicseaweed.com/api/{ key }/forecast/?spot_id={ id }',
                                    params={'q': 'requests+language:python'},
                                )

        json_response = response.json()

        # Pull the swell size out
        dd = json_response[1]['swell']
        min_swell = dd['minBreakingHeight']
        max_swell = dd['maxBreakingHeight']
        res = f"Swell between {min_swell} and {max_swell} ft"
        return res

def swell(location):
    l1 = msw_loc(location)
    if l1 != "Location not available":
        swell = msw_res(key, l1)
        return swell
    else:
        return "ERROR: invalid input"
