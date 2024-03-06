from flask import Flask, Response,request
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

    return 'Hello, world!'


@app.route('/submit', methods=['GET'])
def submit_request():
    event_id = request.args.get('event_id')
    ticket_id = request.args.get('ticket_id')

    if not event_id or not ticket_id:
        return Response("{'error': 'Missing event_id or ticket_id'}", status=400, mimetype='application/json')

    # # Construct the URL with the event_id and ticket_id
    # target_url = f"{SERVER_URL}/some-endpoint?event_id={event_id}&ticket_id={ticket_id}"

    # # Make a GET request to the server
    # response = requests.get(target_url)

    # if response.status_code == 200:
    #     # You can process the response here if needed
    #     return Response(response.content, status=200, mimetype='application/json')
    # else:
    #     return Response("{'error': 'Failed to get data from server'}", status=response.status_code, mimetype='application/json')

    return f'done! {ticket_id}'



    
if __name__ == '__main__':
    app.run(debug=True)


# https://drab-gold-chimpanzee-shoe.cyclic.app//tickets/123/events/test
# https://drab-gold-chimpanzee-shoe.cyclic.app/submit?event_id=123&ticket_id=456



# # Define the GET endpoint
# @app.route('/tickets/<int:ticket_id>/events/<int:event_id>', methods=['GET'])
# def get_ticket_info(ticket_id, event_id):

#     # now = datetime.now()
#     # scan_time = now.strftime(" %I:%M:%S %p | %Y-%m-%d")

#     # embed = {
#     #     "title": "🚀",
#     #     "description": f"Event ID: {event_id}\nTicket ID: {ticket_id}\nScan Time: {scan_time}\n\n{SERVVER_URL}",
#     #     "color": 1543684, 
#     #     "fields": [],
#     #     "footer": {
#     #         "text": "** use report URL to get a text listing of all activity"
#     #     }
#     # }

#     # # Wrap the embed in a payload as Discord expects
#     # payload = {
#     #     "embeds": [embed],
#     # }

#     # # Convert the payload to JSON and make the POST request to the webhook URL
#     # response = requests.post(WEBHOOK_URL, json=payload)

#     # # Check the response
#     # if response.status_code == 204:
#     #     print("Embed sent successfully!")
#     # else:
#     #     print(f"Failed to send embed. Status code: {response.status_code} - Response: {response.text}")

#     return 'Hello, world!2'





# @app.route('/')
# def hello_world():

#     # embed = {
#     #     "title": "🚀",
#     #     "description": "Event ID: <EVENT ID>\nTicket ID: <TICKET ID>\nScan Time: <SCAN TIME>\n\nhttps://sore-cyan-ostrich-fez.cyclic.app",
#     #     "color": 1543684, 
#     #     "fields": [],
#     #     "footer": {
#     #         "text": "** use report URL to get a text listing of all activity"
#     #     }
#     # }

#     # # Wrap the embed in a payload as Discord expects
#     # payload = {
#     #     "embeds": [embed],
#     # }

#     # # Convert the payload to JSON and make the POST request to the webhook URL
#     # response = requests.post(WEBHOOK_URL, json=payload)

#     # # Check the response
#     # if response.status_code == 204:
#     #     print("Embed sent successfully!")
#     # else:
#     #     print(f"Failed to send embed. Status code: {response.status_code} - Response: {response.text}")

#     svg_data ="""
#     <?xml version="1.0" encoding="UTF-8" standalone="no"?>
#     <!-- Created with Inkscape (http://www.inkscape.org/) -->

#     <svg
#     width="210mm"
#     height="297mm"
#     viewBox="0 0 210 297"
#     version="1.1"
#     id="svg1"
#     xmlns="http://www.w3.org/2000/svg"
#     xmlns:svg="http://www.w3.org/2000/svg">
#     <defs
#         id="defs1" />
#     <g
#         id="layer1">
#         <path
#         style="font-size:60px;font-family:'Roboto Slab';-inkscape-font-specification:'Roboto Slab';letter-spacing:-0.148168;white-space:pre;fill:#ff4242;stroke:#f8ff4e;stroke-width:0"
#         d="m 107.2168,469.04233 3.16406,-0.43946 14.91211,-38.52539 h 4.95117 l 14.64844,38.52539 3.13476,0.43946 v 3.6914 h -12.24609 v -3.6914 l 3.22266,-0.55664 -2.8125,-7.85157 h -17.08008 l -2.90039,7.85157 3.22265,0.55664 v 3.6914 H 107.2168 Z m 13.68164,-13.24219 h 13.53515 l -6.62109,-18.31055 h -0.17578 z m 30.40847,25.40039 4.77539,-0.82031 v -34.80469 l -4.77539,-0.82031 v -3.72071 h 9.72656 l 0.52735,3.86719 q 1.58203,-2.16797 3.83789,-3.31055 2.28515,-1.14257 5.27344,-1.14257 5.88867,0 9.14062,4.6875 3.28125,4.6582 3.28125,12.33398 v 0.61524 q 0,6.85546 -3.28125,11.07421 -3.28125,4.18946 -9.05273,4.18946 -2.92969,0 -5.15625,-0.9668 -2.19727,-0.99609 -3.75,-2.92969 v 10.92774 l 4.77539,0.82031 v 3.7207 h -15.32227 z m 25.98633,-23.73047 q 0,-5.41992 -2.10938,-8.87695 -2.10937,-3.45703 -6.26953,-3.45703 -2.46093,0 -4.21875,1.11328 -1.75781,1.11328 -2.84179,3.04687 v 15.43946 q 1.08398,1.96289 2.8125,3.04687 1.75781,1.05469 4.30664,1.05469 4.10156,0 6.21093,-2.98828 2.10938,-2.98828 2.10938,-7.76367 z m 10.19363,23.73047 4.77539,-0.82031 v -34.80469 l -4.77539,-0.82031 v -3.72071 h 9.72656 l 0.52735,3.86719 q 1.58203,-2.16797 3.83789,-3.31055 2.28515,-1.14257 5.27343,-1.14257 5.88868,0 9.14063,4.6875 3.28125,4.6582 3.28125,12.33398 v 0.61524 q 0,6.85546 -3.28125,11.07421 -3.28125,4.18946 -9.05274,4.18946 -2.92968,0 -5.15625,-0.9668 -2.19726,-0.99609 -3.75,-2.92969 v 10.92774 l 4.7754,0.82031 v 3.7207 h -15.32227 z m 25.98633,-23.73047 q 0,-5.41992 -2.10938,-8.87695 -2.10937,-3.45703 -6.26953,-3.45703 -2.46094,0 -4.21875,1.11328 -1.75781,1.11328 -2.8418,3.04687 v 15.43946 q 1.08399,1.96289 2.8125,3.04687 1.75782,1.05469 4.30665,1.05469 4.10156,0 6.21093,-2.98828 2.10938,-2.98828 2.10938,-7.76367 z m 10.89675,-12.71484 v -3.72071 h 9.93164 l 0.55664,4.59961 q 1.34766,-2.43164 3.31055,-3.80859 1.99218,-1.37695 4.54101,-1.37695 0.67383,0 1.37696,0.11718 0.73242,0.0879 1.11328,0.20508 l -0.76172,5.36133 -3.28125,-0.17578 q -2.28516,0 -3.83789,1.08398 -1.55274,1.05469 -2.40235,2.98828 v 18.19336 l 4.77539,0.82032 v 3.6914 h -15.32226 v -3.6914 l 4.77539,-0.82032 v -22.64648 z m 24.10965,11.83593 q 0,-7.03125 3.80859,-11.57226 3.8086,-4.57031 10.3418,-4.57031 6.5625,0 10.37109,4.54101 3.83789,4.54102 3.83789,11.60156 v 0.64454 q 0,7.08984 -3.80859,11.60156 -3.80859,4.51172 -10.3418,4.51172 -6.59179,0 -10.40039,-4.51172 -3.80859,-4.54102 -3.80859,-11.60156 z m 5.77148,0.64454 q 0,5.03906 2.10938,8.32031 2.13867,3.28125 6.32812,3.28125 4.10157,0 6.24024,-3.28125 2.13867,-3.28125 2.13867,-8.32031 v -0.64454 q 0,-4.98046 -2.13867,-8.29101 -2.13867,-3.31055 -6.29883,-3.31055 -4.16016,0 -6.26953,3.31055 -2.10938,3.31055 -2.10938,8.29101 z m 38.14284,-12.48047 -3.80859,0.58593 6.5332,18.04688 0.52734,2.28516 h 0.17579 l 0.55664,-2.28516 6.32812,-18.04688 -3.83789,-0.58593 v -3.72071 h 12.24609 v 3.72071 l -2.60742,0.43945 -10.63476,27.53906 h -4.36524 l -10.75195,-27.53906 -2.60742,-0.43945 v -3.72071 h 12.24609 z m 36.56082,28.59375 q -6.62109,0 -10.54687,-4.39453 -3.89649,-4.42383 -3.89649,-11.45508 v -1.28906 q 0,-6.76758 4.01367,-11.25 4.04297,-4.51172 9.55079,-4.51172 6.38671,0 9.66796,3.86718 3.31055,3.86719 3.31055,10.3125 v 3.60352 h -20.5664 l -0.0879,0.14648 q 0.0879,4.57032 2.31446,7.5293 2.22656,2.92969 6.24023,2.92969 2.92969,0 5.12696,-0.82031 2.22656,-0.84961 3.83789,-2.31446 l 2.25586,3.75 q -1.69922,1.64063 -4.51172,2.78321 -2.78321,1.11328 -6.70899,1.11328 z m -0.8789,-28.35938 q -2.90039,0 -4.95118,2.46094 -2.05078,2.43164 -2.51953,6.12305 l 0.0586,0.14648 h 14.61914 v -0.76172 q 0,-3.39844 -1.81641,-5.68359 -1.81641,-2.28516 -5.39062,-2.28516 z m 39.87136,23.96485 q -1.55273,2.16796 -3.80859,3.28125 -2.22656,1.11328 -5.18555,1.11328 -5.80078,0 -9.08203,-4.18946 -3.25195,-4.21875 -3.25195,-11.07421 v -0.61524 q 0,-7.64648 3.25195,-12.33398 3.28125,-4.6875 9.14063,-4.6875 2.8125,0 4.95117,1.05468 2.16797,1.02539 3.69141,2.98829 v -12.91993 l -4.77539,-0.82031 v -3.7207 h 4.77539 5.77148 v 41.1914 l 4.77539,0.82032 v 3.6914 h -9.78516 z M 352.39056,458.0853 q 0,4.77539 1.96289,7.67578 1.9629,2.90039 6.06446,2.90039 2.57812,0 4.33594,-1.17188 1.75781,-1.17187 2.90039,-3.31054 v -14.70704 q -1.11329,-1.99218 -2.90039,-3.16406 -1.78711,-1.17187 -4.27735,-1.17187 -4.13086,0 -6.12305,3.42773 -1.96289,3.42774 -1.96289,8.90625 z"
#         id="text2"
#         transform="scale(0.26458333)"
#         aria-label="Approved" />
#     </g>
#     </svg>
#     """
# #    # You might want to select an SVG file dynamically based on ticket_id and event_id
# #     svg_file_path = './approved.svg'
    
# #     # Open the SVG file and read its contents
# #     with open(svg_file_path, 'r') as svg_file:
# #         svg_data = svg_file.read()
    
#     # return 'Hello, world!'
        
#     # Return the SVG data with the appropriate MIME type
#     return Response(svg_data, mimetype='image/svg+xml')
