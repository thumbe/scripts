import requests
import json
import os
import time

location_id="5446"
api_url=f"https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={location_id}&minimum=1"

while True: 
	response = requests.get(api_url)
	jsonResponse = response.json()
	if len(jsonResponse) > 0:
		print(jsonResponse[0]['startTimestamp'])
		date = jsonResponse[0]['startTimestamp']
		title = "Appointment Available"
		cmd = """osascript -e \'Tell application \"System Events\" to display dialog \"Date Available: {0} \" with title \" Appointment Available \" \' """.format(date)
		os.system(cmd)
	else:
		print("Not available")
	time.sleep(90)
 

