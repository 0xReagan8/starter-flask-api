from flask import Flask, Response,request
import os
from datetime import datetime
import requests
import json

KEY_NAME = os.getenv("KEY_NAME")

# Your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1214662183452016660/1yOSpSVg3oj0gr6rQWnpKW9ncjt-TKeODdlzXE12hWSLwmNlUNOEUI21L3hmxPYCvK5u"
SERVVER_URL = 'https://drab-gold-chimpanzee-shoe.cyclic.app'
APPROVED_SVG = 'approved.svg'

app = Flask(__name__)

@app.route('/')
def hello_world():

    return 'Hello, world!'



def write_pickle_test(data:dict, event_id:str):
    import io
    import pickle
    import json
    from b2sdk.v1 import InMemoryAccountInfo, B2Api

    pickled_data = pickle.dumps(data)

    # Convert the dictionary to a JSON string
    json_string = json.dumps(test)

    # Encode the JSON string to a byte string using UTF-8 encoding
    byte_string = json_string.encode('utf-8')

    # Initialize the B2 API with your account information
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    application_key_id = os.getenv("KEY_ID")
    application_key = os.getenv("APPLICATION_KEY")
    b2_api.authorize_account("production", application_key_id, application_key)

    # Specify your bucket
    bucket = b2_api.get_bucket_by_name(os.getenv("BUCKET_NAME"))

    file_name = f'{event_id}.pck'  # The name of the file in B2

    # Upload the data
    b2_file_version = bucket.upload_bytes(
        data_bytes=pickled_data,
        file_name=file_name
    )
    print(f"Data uploaded to file {file_name} with version {b2_file_version.id_}")

def read_pickle_test(event_id):
    import pickle
    from b2sdk.v1 import InMemoryAccountInfo, B2Api, DownloadDestBytes

    # Initialize the B2 API with your account information
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    application_key_id = os.getenv("KEY_ID")
    application_key = os.getenv("APPLICATION_KEY")
    b2_api.authorize_account("production", application_key_id, application_key)

    # Specify your bucket
    bucket = b2_api.get_bucket_by_name(os.getenv("BUCKET_NAME"))
    try:
        # File to download
        file_name = f'{event_id}.pck'  # The name of the file in B2

        # Prepare a DownloadDestBytesIO object for the downloaded file
        download_dest = DownloadDestBytes()

        # Download the file into the DownloadDestBytesIO object
        bucket.download_file_by_name(file_name, download_dest)

        # Access the BytesIO object from download_dest
        bytes_io = download_dest.get_bytes_written()

        # decode the pickle
        d = pickle.loads(bytes_io)

        return(d)
    except:
        return(None)

@app.route('/submit', methods=['GET'])
def submit_request():
    now = datetime.now()
    scan_time = now.strftime(" %I:%M:%S %p | %Y-%m-%d")
    event_id = request.args.get('event_id')
    ticket_id = request.args.get('ticket_id')
    

    if not event_id or not ticket_id:
            return Response("{'error': 'Missing event_id or ticket_id'}", status=400, mimetype='application/json')


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

   # You might want to select an SVG file dynamically based on ticket_id and event_id
    svg_file_path = APPROVED_SVG
    
    # Open the SVG file and read its contents
    with open(svg_file_path, 'r') as svg_file:
        svg_data = svg_file.read()

    data = read_pickle_test()
    
    # # Return the SVG data with the appropriate MIME type
    # return Response(svg_data, mimetype='image/svg+xml')
    # return KEY_NAME
    return str(data)
        
    
if __name__ == '__main__':
    app.run(debug=True)


# https://drab-gold-chimpanzee-shoe.cyclic.app//tickets/123/events/test
# https://drab-gold-chimpanzee-shoe.cyclic.app/submit?event_id=test_123&ticket_id=4
# https://secure.backblaze.com/b2_buckets.htm
    



