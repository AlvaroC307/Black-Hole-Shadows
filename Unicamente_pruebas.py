# Importar Librerias utiles

import time
import csv
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

def worker(task):
    result = []
    with tqdm(total=len(task)) as pbar:  # initialize progress bar
        for item in task:
            # do some work on the item
            result.append(item ** 2)
            # update progress bar
            pbar.update(1)
    return result

if __name__ == '__main__':
    tasks = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(worker, tasks))
    print(results)


