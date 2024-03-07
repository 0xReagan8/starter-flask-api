import os, sys
import requests
import json
from dotenv import load_dotenv

os.chdir(os.path.join(str(os.getcwd())))

# Load environment variables
load_dotenv(".env")


def write_pickle_test(data:dict, event_id:str):
    import io
    import pickle
    import json
    from b2sdk.v1 import InMemoryAccountInfo, B2Api


    # dump to a bstrt
    pickled_data = pickle.dumps(data)

    # Initialize the B2 API with your account information
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    application_key_id = os.getenv("KEY_ID")
    application_key = os.getenv("APPLICATION_KEY")
    b2_api.authorize_account("production", application_key_id, application_key)

    # Specify your bucket
    bucket = b2_api.get_bucket_by_name(os.getenv("BUCKET_NAME"))

    file_name = f"{event_id}.pck"  # The name of the file in B2

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

    # File to download
    file_name = f'{event_id}.pck'  # The name of the file in B2

    try:
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

if __name__ =="__main__":

    # test = {
    #     "one": [1,2,3],
    #     "two": {'A':1, "B":2,"C":3 }
    #     }

    # write_pickle_test(test, 'test_123')
    data = read_pickle_test('test_123')
    print(data)

# def read_test():
#     from b2sdk.v1 import InMemoryAccountInfo, B2Api, DownloadDestBytes

#     # Initialize the B2 API with your account information
#     info = InMemoryAccountInfo()
#     b2_api = B2Api(info)
#     application_key_id = os.getenv("KEY_ID")
#     application_key = os.getenv("APPLICATION_KEY")
#     b2_api.authorize_account("production", application_key_id, application_key)

#     # Specify your bucket
#     bucket = b2_api.get_bucket_by_name(os.getenv("BUCKET_NAME"))

#     # File to download
#     file_name = 'example.txt'  # The name of the file in B2

#     # Prepare a DownloadDestBytesIO object for the downloaded file
#     download_dest = DownloadDestBytes()

#     # Download the file into the DownloadDestBytesIO object
#     bucket.download_file_by_name(file_name, download_dest)

#     # Access the BytesIO object from download_dest
#     bytes_io = download_dest.get_bytes_written()

#     # Now you can use file_bytes as needed, for example:
#     print(bytes_io.decode('utf-8'))  # Assuming the file content is text

# def write_test():
#     from b2sdk.v1 import InMemoryAccountInfo, B2Api
#     import io

#     from b2sdk.v1 import InMemoryAccountInfo, B2Api

#     # Initialize the B2 API with your account information
#     info = InMemoryAccountInfo()
#     b2_api = B2Api(info)
#     application_key_id = os.getenv("KEY_ID")
#     application_key = os.getenv("APPLICATION_KEY")
#     b2_api.authorize_account("production", application_key_id, application_key)

#     # Specify your bucket
#     bucket_name = 'your_bucket_name'  # Replace with your bucket name
#     bucket = b2_api.get_bucket_by_name(os.getenv("BUCKET_NAME"))

#     # Data to upload (as bytes)
#     data_bytes = b"""
#     Hello, world!
#     In this example, b'Hello, world!' is a bytes literal, which is written to the BytesIO object. The seek(0) method is used to move the cursor to the start of the BytesIO object so that we can read from the beginning. The read() method reads the bytes, and decode('utf-8') converts the bytes to a string assuming the bytes are encoded in UTF-8.
#     """  # Example data to upload
#     file_name = 'example.txt'  # The name of the file in B2

#     # Upload the data
#     b2_file_version = bucket.upload_bytes(
#         data_bytes=data_bytes,
#         file_name=file_name
#     )
#     print(f"Data uploaded to file {file_name} with version {b2_file_version.id_}")
