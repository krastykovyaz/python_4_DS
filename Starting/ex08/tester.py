from Loading import ft_tqdm
from time import sleep

# Example usage
if __name__ == "__main__":
    from tqdm import tqdm

    print("Custom ft_tqdm:")
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    print("\nOriginal tqdm:")
    for elem in tqdm(range(333)):
        sleep(0.005)
