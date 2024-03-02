import os

def generate_documentation(directory):
    documentation_content = "Documentation:\n"
    documentation_content += "Directory: {}\n".format(directory)
    
    for root, dirs, files in os.walk(directory):
        documentation_content += "\n"
        documentation_content += "Folder: {}\n".format(root)
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            documentation_content += "  - File: {}, Size: {} bytes\n".format(file, size)

    with open("documentation.txt", "w") as file:
        file.write(documentation_content)
    print("Documentation generated successfully.")

# Call the function to generate documentation for a specific directory
directory_path = "/path/to/your/directory"  # Replace this with your directory path
generate_documentation(directory_path)
