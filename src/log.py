from datetime import datetime

def log_progress(message, log_file): 
    # Define the timestamp format
    timestamp_format = '%Y-%m-%d %H:%M:%S' 
    now = datetime.now()
    timestamp = now.strftime(timestamp_format) 
    
    # Append the log message with a timestamp to the log file
    with open(log_file, "a") as f: 
        f.write(f"{timestamp}, {message}\n")