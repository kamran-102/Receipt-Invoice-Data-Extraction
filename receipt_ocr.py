import pandas as pd
import requests
import json
import re

imageFile = "receipt_4.jpg" # Target Image Path
receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt' # Receipt OCR API endpoint
r = requests.post(receiptOcrEndpoint, data = { \
  'client_id': 'TEST',      
  'recognizer': 'auto',       
  'ref_no': 'ocr_python_123', 
  }, \
  files = {"file": open(imageFile, "rb")})

data_string = r.text 

# Converting ocr resutls into Json format
data = json.loads(data_string)

# Fetching only specific details 
receipt = data['receipts'][0]
receipt_no = receipt['receipt_no']
items = receipt['items']
for i in items:
    match = re.search(r'\$(\d+(\.\d{1,2})?)', i['description'])
    if match:
        price = float(match.group(1))
        # Updating the amount with the extracted price
        i['price'] = price
        # Remove the dollar amount from the description
        i['description'] = re.sub(r'\$\d+(\.\d{1,2})?', '', i['description']).strip()
# Filtering the items to retain only specific fields
filtered_items = [
    {key: item[key] for key in item if key in ['amount', 'category', 'description', 'qty', 'price']}
    for item in items
]
currency = receipt['currency']
total = receipt['total']
subtotal = receipt['subtotal']
tax = receipt['tax']

extracted_data = {
    'receipt_no': receipt_no,
    'items': filtered_items,
    'currency': currency,
    'total': total,
    'subtotal': subtotal,
    'tax': tax,    
}

# Save JSON data to a file
file_path = imageFile.split(".")[0]
with open(f"{file_path}.json", 'w') as json_file:
    json.dump(extracted_data, json_file, indent=4)
    