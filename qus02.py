def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{file_name}': {str(e)}")

file_name = "2023-10-11 13:45:00.txt" 
read_text_file(file_name)
