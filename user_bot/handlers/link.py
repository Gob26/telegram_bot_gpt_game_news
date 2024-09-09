import re

text =
# Используем регулярное выражение для поиска ссылки
url_pattern = r'https?://[^\s]+'
matches = re.findall(url_pattern, text)

if matches:
    # Получаем первое совпадение, если оно есть
    url = matches[0]
    print("Ссылка:", url)
else:
    print("Ссылка не найдена.")