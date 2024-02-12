import time
from typing import Generator


def ft_tqdm(lst: range) -> Generator:
    """
    A custom tqdm implementation to display progress bars.

    Args:
        lst (range): The range over which to iterate.

    Yields:
        Any: The elements from the input range.
    """
    total = len(lst)
    start_time = time.time()
    for i, elem in enumerate(lst, 1):
        elapsed_time = time.time() - start_time
        progress = i / total
        percentage = int(progress * 100)
        speed = i / elapsed_time if elapsed_time > 0 else 0

        bar_length = 40
        num_hashes = int(progress * bar_length)
        bar = '=' * num_hashes + '>' + ' ' * (bar_length - num_hashes)

        info_str = f'{percentage}%|[{bar}]| {i}/{total} [{speed: .2f}it/s]'
        print(info_str, end='\r')
        yield elem
