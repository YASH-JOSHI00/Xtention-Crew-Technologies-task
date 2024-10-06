def process_log_file(filename, keyword="ERROR"):
    try:
        with open(filename, 'r') as file:
            # Initialize count variable
            count = 0
            
            # Loop through each line in the file
            for line in file:
                # Check if the keyword exists in the current line
                if keyword in line:
                    count += 1

        # Print the total count of lines containing the keyword
        print(f"Number of lines containing '{keyword}': {count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    log_file = "server_log.txt"
    process_log_file(log_file, "ERROR")
