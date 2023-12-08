import re

def find_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Mencari link web menggunakan ekspresi reguler
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    links = re.findall(pattern, text)

    return links

# Contoh penggunaan
file_path = 'text_file.txt'  # Gantilah dengan nama file teks yang sebenarnya
web_links = find_links(file_path)

# Menampilkan hasil
print("Web Links found in the file:")
for link in web_links:
    print(link)
