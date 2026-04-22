import re
from PIL import Image
import pytesseract

def extract_receipt_data(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        date_pattern = r"\b(\d{2}[./-]\d{2}[./-]\d{4})\b" 
        total_pattern = r"Total\s*[:\-]?\s*\$?(\d+\.\d{2})"
        item_pattern = r"([A-Za-z0-9\s]+)\s+\$?(\d+\.\d{2})"

        date_match = re.search(date_pattern, text)
        total_match = re.search(total_pattern, text, re.IGNORECASE)
        items = re.findall(item_pattern, text)

        return {
            "raw_text": text.strip(),
            "date": date_match.group(1) if date_match else None,
            "total": float(total_match.group(1)) if total_match else None,
            "items": [{"name": name.strip(), "price": float(price)} for name, price in items]
        }

    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as e:
        print(f"Error processing receipt: {e}")

if __name__ == "__main__":
    receipt_info = extract_receipt_data("receipt_sample.jpg")
    if receipt_info:
        print("Date:", receipt_info["date"])
        print("Total:", receipt_info["total"])
        print("Items:")
        for item in receipt_info["items"]:
            print(f"  - {item['name']}: ${item['price']}")
