from flask import Flask, Response
import os
from datetime import datetime
import requests
import json


# Your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1214662183452016660/1yOSpSVg3oj0gr6rQWnpKW9ncjt-TKeODdlzXE12hWSLwmNlUNOEUI21L3hmxPYCvK5u"
SERVVER_URL = 'https://drab-gold-chimpanzee-shoe.cyclic.app'

app = Flask(__name__)


@app.route('/')
def hello_world():

    # embed = {
    #     "title": "🚀",
    #     "description": "Event ID: <EVENT ID>\nTicket ID: <TICKET ID>\nScan Time: <SCAN TIME>\n\nhttps://sore-cyan-ostrich-fez.cyclic.app",
    #     "color": 1543684, 
    #     "fields": [],
    #     "footer": {
    #         "text": "** use report URL to get a text listing of all activity"
    #     }
    # }

    # # Wrap the embed in a payload as Discord expects
    # payload = {
    #     "embeds": [embed],
    # }

    # # Convert the payload to JSON and make the POST request to the webhook URL
    # response = requests.post(WEBHOOK_URL, json=payload)

    # # Check the response
    # if response.status_code == 204:
    #     print("Embed sent successfully!")
    # else:
    #     print(f"Failed to send embed. Status code: {response.status_code} - Response: {response.text}")

   # You might want to select an SVG file dynamically based on ticket_id and event_id
    svg_file_path = os.path.join(app.root_path, 'approved.svg')
    
    # Open the SVG file and read its contents
    with open(svg_file_path, 'r') as svg_file:
        svg_data = svg_file.read()
    
    # return 'Hello, world!'
        
    # Return the SVG data with the appropriate MIME type
    return Response(svg_data, mimetype='image/svg+xml')

    
# Define the GET endpoint
@app.route('/tickets/<int:ticket_id>/events/<int:event_id>', methods=['GET'])
def get_ticket_info(ticket_id, event_id):

    now = datetime.now()
    scan_time = now.strftime(" %I:%M:%S %p | %Y-%m-%d")

    embed = {
        "title": "🚀",
        "description": f"Event ID: {event_id}\nTicket ID: {ticket_id}\nScan Time: {scan_time}\n\n{SERVVER_URL}",
        "color": 1543684, 
        "fields": [],
        "footer": {
            "text": "** use report URL to get a text listing of all activity"
        }
    }

    # Wrap the embed in a payload as Discord expects
    payload = {
        "embeds": [embed],
    }

    # Convert the payload to JSON and make the POST request to the webhook URL
    response = requests.post(WEBHOOK_URL, json=payload)

    # Check the response
    if response.status_code == 204:
        print("Embed sent successfully!")
    else:
        print(f"Failed to send embed. Status code: {response.status_code} - Response: {response.text}")

    return 'Hello, world!'

    
if __name__ == '__main__':
    app.run(debug=True)