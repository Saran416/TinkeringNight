def remove_waste(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Remove curly braces from the content
    content_without_braces = content.replace('{', '').replace('}', '').replace('"','').replace(":").replace("\"test\"",'')

    with open(output_file, 'w') as file:
        file.write(content_without_braces)  




