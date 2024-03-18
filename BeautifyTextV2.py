def format_text(file_path):
    color = input("Enter your preferred title color (e.g., red, green, blue): ")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write('<html><body>\n')
        for line in lines:
            title = line.strip()
            if title.endswith('.'):
                file.write('<p>\n')
                file.write(title)
                file.write('</p>\n')
            elif title.startswith('*') and title.endswith('*'):
                file.write(f'<h1 style="color:{color};">\n')
                file.write(title[1:-1])  # remove the asterisks
                file.write('</h1>\n')
            else:
                file.write('<p>\n')
                file.write(title)
                file.write('</p>\n')
        file.write('</body></html>\n')

format_text('doc.txt')

