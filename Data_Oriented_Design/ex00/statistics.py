from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate statistics based on the given arguments.

    Args:
        *args (Any): Arbitrary number of arguments.
        **kwargs (Any):
        Keyword arguments specifying the statistics to calculate.

    Returns:
        None: This function does not return anything.
        It prints the calculated statistics.

    This function calculates statistics such as
    mean, median, quartile, variance, and standard deviation
    based on the provided arguments.
    The statistics to calculate are specified using keyword arguments.
    """
    try:
        def find_median(sorted_list):
            indices = []

            list_size = len(sorted_list)
            median = 0
            if list_size % 2 == 0:
                indices.append(int(list_size / 2) - 1)
                indices.append(int(list_size / 2))
                median = (
                    sorted_list[indices[0]] + sorted_list[indices[1]]
                    ) / 2
            else:
                indices.append(int(list_size / 2))
                median = sorted_list[indices[0]]
            return median, indices

        def get_diff(val, _mean):
            return (val - _mean) ** 2

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
                l, r = [float(args_s[left]), float(args_s[right])]
                print(f"quartile : [{l}, {r}]")
            elif kw == 'var' and len(args) > 0:
                mean_ = sum(args) / len(args)
                var = sum([get_diff(val, mean_) for val in args]) / len(args)
                print(f"var : {var}")
            elif kw == 'std' and len(args) > 0:
                mean_ = sum(args) / len(args)
                desc = sum([get_diff(val, mean_) for val in args]) / len(args)
                std_ = desc ** .5
                print(f"std : {std_}")
            elif len(args) > 0:
                pass
            else:
                print("ERROR")
    except Exception as e:
        print(e)
