import datetime
import random
import string
import concurrent.futures
import logging


def fuzz_generator(symbols, word_length: int):
    res = random.choices(symbols, k=word_length)
    return (''.join(res))


def exec_process(symbols, word_length: int, words_amount: int = 10):
    logging.basicConfig(level=logging.INFO)
    start = datetime.datetime.now()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(words_amount):
            futures.append(executor.submit(fuzz_generator, symbols, word_length))
        with open("file.txt", 'w') as file:
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                file.write(f'{res}\n')
    finish = datetime.datetime.now()
    execution_speed = finish - start


if __name__ == "__main__":
    exec_process(string.ascii_lowercase + string.digits, 5, 5)
    logging.basicConfig(level=logging.INFO)
