import qrcode
import os

EVENT_ID="Some Event Title"
# format the event id so we can send in the URL
EVENT_ID= EVENT_ID.replace(' ', '_' )


# Ensure the directory for QR codes exists
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)

EVENT_ID = "test_123"
BASE_URL = "https://drab-gold-chimpanzee-shoe.cyclic.app/submit"  # Replace with your actual server address
# https://drab-gold-chimpanzee-shoe.cyclic.app/submit?event_id=test_123&ticket_id=5

for i in range(1, 31):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    url = f"{BASE_URL}?event_id={EVENT_ID}&ticket_id={i}"  # Added event_id to the URL

    print(url)

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    img.save(f"{output_dir}/QR_Code_{i}.png")

print("QR codes generated successfully.")

