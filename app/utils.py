import uuid
from datetime import datetime

def generate_uuid():
    """Генерирует уникальный идентификатор."""
    return str(uuid.uuid4())

def calculate_average_time(order_times):
    """Вычисляет среднее время выполнения заказа."""
    if not order_times:
        return None
    total_time = sum(order_times, datetime.min)
    return total_time / len(order_times)

def calculate_average_orders_per_day(order_counts):
    """Вычисляет среднее количество заказов в день."""
    if not order_counts:
        return None
    return sum(order_counts) / len(order_counts)
