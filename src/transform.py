def transform(data):
    # Round the price column to 2 decimal places
    data['price'] = round(data['price'], 2)
    
    return data