# Задание 2:
# Дано: список, содержащий URL страниц
# Требуется: Написать функцию, которая получает из Сети код страниц из списка и сохраняет его (код) на диск.
import requests
import os


def save_web_pages_code(urls: list[str], directory='pages') -> None:
    """Сохранить код страниц"""

    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()

            filename = url.split('//')[-1].replace('/', '_') + '.html'
            file_path = os.path.join(directory, filename)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f'Сохранена страница: {file_path}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при получении {url}: {e}')


if __name__ == '__main__':
    urls = input('Введите адреса станиц разделённые пробелом \n')
    urls = urls.strip().split()
    save_web_pages_code(urls)
