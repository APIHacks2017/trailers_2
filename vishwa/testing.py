import requests
import json
payload = [
    {'lat': -50.44,
     'long': 70.999,
     'type': 'locats',
     'duration': {
                    'sttime': 1030,
                    'entime': 1130
                }
     },
    {'lat': -50.24,
     'long': 70.11199,
     'type': 'lossss',
     'duration': {
         'sttime': 1230,
         'entime': 2230
     }
     }
]


latitude= -50.7894
longitude = 70.09882329
type_user = 'restaurant'
duration = {
            'sttime': 1110,
            'entime': 1920
        }
payload_json = json.dumps(payload)

r = requests.post('http://127.0.0.1:5000/receivedata', data={'listed':payload_json,
                                                             'lat':latitude,
                                                             'long': longitude,
                                                              'type': type_user
                                                            })

print(r.status_code, r.reason)