import time

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    for i, elem in enumerate(lst, 1):
        elapsed_time = time.time() - start_time
        progress = i / total
        percentage = int(progress * 100)

        bar_length = 40
        num_hashes = int(progress * bar_length)
        bar = '=' * num_hashes + '>' + ' ' * (bar_length - num_hashes)

        info_str = f'{percentage}%|[{bar}]| {i}/{total}'
        print(info_str, end='\r')
        yield elem

# Example usage
if __name__ == "__main__":
    from time import sleep
    from tqdm import tqdm

    print("Custom ft_tqdm:")
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    # print("\nOriginal tqdm:")
    # for elem in tqdm(range(333)):
    #     sleep(0.005)
