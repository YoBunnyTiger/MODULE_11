import requests
from PIL import Image

"""Библиотека requests"""


def download_image(image__url):
    """Скачивает изображение по указанной ссылке и возвращает его содержимое."""
    try:
        response = requests.get(image__url)
        response.raise_for_status()  # Проверяет, что запрос успешен
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def save_web_image(image_data, output_path):
    """Сохраняет скачанное изображение по указанному пути."""
    if image_data:
        with open(output_path, 'wb') as f:
            f.write(image_data)
        print(f"Изображение сохранено как '{output_path}'.")
    else:
        print("Нет данных изображения для сохранения.")


def main(image__url, output_path):
    """Основная логика загрузки и сохранения изображения."""
    image_data = download_image(image__url)
    save_web_image(image_data, output_path)


"""Библиотека Pillow"""


def load_image(image_path):
    """Загружает изображение из указанного пути."""
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(f"Ошибка: файл '{image_path}' не найден.")
        return None


def resize_image(image, new__size):
    """Изменяет размер переданного изображения на новый размер."""
    if image is not None:
        resized__image = image.resize(new__size)
        return resized__image
    else:
        print("Ошибка: изображение не загружено.")
        return None


def save_image(image, output_path):
    """Сохраняет изображение по указанному пути."""
    if image is not None:
        image.save(output_path)
        print(f"Изображение сохранено как '{output_path}'.")
    else:
        print("Ошибка: нечего сохранять.")


if __name__ == "__main__":
    image_url = ('https://avatars.mds.yandex.net'
                 '/i?id=febe8a6b72e3211de8e881bde569ad81_l'
                 '-5255469-images-thumbs&n=13')  # Ссылка на изображение
    save_image_path = 'downloaded_image.png'  # Путь для сохранения

    main(image_url, save_image_path)

    input_image_path = 'logo.png'  # Путь к изображению
    output_image_path = 'logo(new).png'  # Путь для сохранения измененного изображения
    new_size = (980, 550)  # Новый размер (ширина, высота)

    original_image = load_image(input_image_path)
    resized_image = resize_image(original_image, new_size)
    save_image(resized_image, output_image_path)
