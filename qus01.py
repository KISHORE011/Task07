import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_time = datetime.datetime.now()
    
    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a file with the timestamp as the filename
    file_name = f"{timestamp_str}.txt"
    
    # Write the timestamp to the file
    with open(file_name, 'w') as file:
        file.write(timestamp_str)
    
    print(f"File '{file_name}' created with the timestamp: {timestamp_str}")

# Call the function to create the timestamp file
create_timestamp_file()

