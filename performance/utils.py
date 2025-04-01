import time
import concurrent.futures
from django.db import connection


def query_database(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def parallel_database_queries():
    queries = [
        "SELECT * FROM product_product WHERE price > 100",
        "SELECT * FROM order_order WHERE status = 'pending'",
        "SELECT * FROM product_review WHERE rating >= 4"
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(query_database, queries))

    return results


def run_experiment(num_threads, query_batch_size):
    queries = ["SELECT * FROM product_product"] * query_batch_size
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(query_database, queries))

    execution_time = time.time() - start_time
    return execution_time
