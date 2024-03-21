# scripts/data_processing.py

def process_data(data):
    # data processing logic
    processed_data = []
    for item in data:
        # Example: processing each item by squaring it
        processed_item = item ** 2
        processed_data.append(processed_item)
    print("Processing data...")
    return processed_data
