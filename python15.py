# задача №1
import logging

# Настройка логгера для сообщений уровня DEBUG и INFO
debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG)

# Создание файла для логов уровня DEBUG и INFO
debug_handler = logging.FileHandler('debug_info.log')
debug_handler.setLevel(logging.DEBUG)

# Форматирование сообщений
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
debug_logger.addHandler(debug_handler)

# Настройка логгера для сообщений уровня WARNING и выше
warning_logger = logging.getLogger('warning_logger')
warning_logger.setLevel(logging.WARNING)

# Создание файла для логов уровня WARNING и выше
warning_handler = logging.FileHandler('warnings_errors.log')
warning_handler.setLevel(logging.WARNING)

# Форматирование сообщений
warning_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
warning_logger.addHandler(warning_handler)

# Примеры логирования
debug_logger.debug("Это сообщение уровня DEBUG.")
info_logger = logging.getLogger('debug_logger')  # Логгер уже настроен для INFO
info_logger.info("Это сообщение уровня INFO.")
warning_logger.warning("Это сообщение уровня WARNING.")
error_logger = logging.getLogger('warning_logger')  # Логгер уже настроен для ERROR
error_logger.error("Это сообщение уровня ERROR.")
critical_logger = logging.getLogger('warning_logger')  # Логгер уже настроен для CRITICAL
critical_logger.critical("Это сообщение уровня CRITICAL.")

# задача №2
 from datetime import datetime

# Получение текущего времени и даты
now = datetime.now()

# Форматирование даты и времени в нужный формат
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Получение полного названия дня недели
day_of_week = now.strftime("%A")

# Получение номера недели в году
week_number = now.isocalendar()[1]

# Вывод результатов
print(f"Текущая дата и время: {formatted_date_time}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")

# задача №3
from datetime import datetime, timedelta

def get_future_date(days_ahead):
    # Получаем текущую дату и время
    current_date = datetime.now()
    
    # Создаем объект timedelta для добавления указанного количества дней
    future_date = current_date + timedelta(days=days_ahead)
    
    # Форматируем будущую дату в нужном формате
    formatted_date = future_date.strftime("%Y-%m-%d")
    
    return formatted_date

# Пример использования функции
future_date = get_future_date(30)
print(f"Дата через 30 дней: {future_date}")

# задача №4
import argparse

# Подсказка № 2: Создаем объект парсера
parser = argparse.ArgumentParser(description="Скрипт для работы с числом и строкой")

# Подсказка № 3: Добавляем обязательные аргументы
parser.add_argument("number", type=int, help="Число для обработки")
parser.add_argument("text", type=str, help="Строка для обработки")

# Подсказка № 4: Добавляем опции
parser.add_argument("--verbose", "-v", action="store_true", help="Активировать дополнительный вывод")
parser.add_argument("--repeat", "-r", type=int, default=1, help="Количество повторений строки")

# Парсим аргументы
args = parser.parse_args()

# Основная логика скрипта
if args.verbose:
    print(f"Принятые аргументы: Число={args.number}, Строка='{args.text}', Повторения={args.repeat}")

for _ in range(args.repeat):
    print(args.text)

# Дополнительный вывод, если включен режим verbose
if args.verbose:
    print(f"Выполнено {args.repeat} повторений строки '{args.text}'.")

# задача №5
import os
import pathlib
from collections import namedtuple
import logging

# Определение структуры данных
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])

# Настройка логирования
logging.basicConfig(
    filename='directory_content.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def gather_directory_info(directory_path):
    try:
        directory = pathlib.Path(directory_path)
        parent = directory.parent.name
        for entry in directory.iterdir():
            name = entry.stem
            extension = entry.suffix.lstrip('.')
            is_dir = entry.is_dir()
            info = FileInfo(name=name, extension=extension, is_dir=is_dir, parent=parent)
            log_message(info)
    except Exception as e:
        logging.exception(f"Ошибка при сборе информации о директории: {e}")

def log_message(file_info):
    message = f"{file_info.name}, {file_info.extension}, {'Directory' if file_info.is_dir else 'File'}, {file_info.parent}"
    logging.info(message)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Использование: python script.py <путь_к_директории>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    gather_directory_info(directory_path)
