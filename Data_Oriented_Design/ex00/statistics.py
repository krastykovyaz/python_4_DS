from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate statistics based on the given arguments.

    Args:
        *args (Any): Arbitrary number of arguments.
        **kwargs (Any): Keyword arguments specifying the statistics to calculate.

    Returns:
        None: This function does not return anything. It prints the calculated statistics.

    This function calculates statistics such as mean, median, quartile, variance, and standard deviation
    based on the provided arguments. The statistics to calculate are specified using keyword arguments.
    """
    def find_median(sorted_list):
        indices = []

        list_size = len(sorted_list)
        median = 0
        if list_size % 2 == 0:
            indices.append(int(list_size / 2) - 1)  # -1 because index starts from 0
            indices.append(int(list_size / 2))
            median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
        else:
            indices.append(int(list_size / 2))
            median = sorted_list[indices[0]]
        return median, indices

    for kw in kwargs.values():
        if kw == 'mean' and len(args) > 0:
            print(f"mean : {sum(args) / len(args)}")
        elif kw == 'median' and len(args) > 0:
            args_s = sorted(args)
            med, _ = find_median(args_s)
            print(f"median : {med}")
        elif kw == 'quartile' and len(args) > 0:
            args_s = sorted(args)
            q1_index = len(args_s) // 4
            left = len(args_s) // 4
            right = q1_index * 3
            l,r = [float(args_s[left]), float(args_s[right])]
            print(f"quartile : [{l}, {r}]")
        elif kw == 'var' and len(args) > 0:
            mean_ = sum(args) / len(args)
            f = lambda x: (x - mean_)**2
            print(f"var : {sum([f(val) for val in args]) / len(args) - 1}")
        elif kw == 'std' and len(args) > 0:
            mean_ = sum(args) / len(args)
            f = lambda x: (x - mean_)**2
            print(f"std : {(sum([f(val) for val in args]) / len(args) - 1) ** .5}")
        elif len(args) > 0:
            pass
        else:
            print("ERROR")

