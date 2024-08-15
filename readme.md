# Receipt | Invoice Data Extraction

### Overview

This project provides a Python script to extract specific information from the input image of receipt or invoice using Optical Character Recognition (OCR). The extracted data is then processed and saved into a JSON file.

## Features

- **OCR Integration**: Uses the Asprise OCR API to extract data from a receipt image.
- **Data Extraction**: Extracts key details such as receipt number, items, prices, currency, subtotal, tax, and total.
- **JSON Output**: Saves the processed data into a JSON file for further use.

## How It Works

1. **OCR Request**: The script sends a POST request to the Asprise OCR API with the receipt image.
2. **Data Parsing**: The OCR results are parsed to extract specific information.
3. **Data Processing**: Prices are extracted from item descriptions, and the descriptions are cleaned up.
4. **Filtering**: The script filters out unnecessary fields, retaining only essential information like amount, category, description, quantity, and price.
5. **JSON Storage**: The processed data is stored in a JSON file named after the original image file.


### Dependencies

- **Python 3.x**
- **requests**
- **pandas**
- **json**
- **re**


### Installation

1. **Install Python 3.x:** Ensure that Python 3.x is installed on your system.
2. **Install Required Libraries:** Run the following command to install the necessary Python libraries:
    ```bash
    pip install requests, pandas, json, re
    ```
3. **Clone the Repository:** Download or clone this repository to your local machine.

## Usage

1. **Set Imagepath**:
   - Modify the `imageFile` variable to match the name of your image file.

2. **Run the Script**:
    ```bash
    python receipt_ocr.py
    ```

3. **Output**:
   - The extracted data will be saved in a JSON file with the same name as the image (e.g., `receipt_4.json`).

## Notes

- The performance of the OCR and the quality of the extracted data may vary based on the clarity of the receipt image.

### Disclaimer

"This script is provided for educational purposes only and the author cannot be held responsible for any misuse, potential damages, or legal implications that may result from its use. It is advised to ensure that you have the appropriate permissions and that your use of this script is in full compliance with relevant laws and regulations."
