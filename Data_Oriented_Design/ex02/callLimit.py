from typing import Any

def callLimit(limit: int):
    """
    Decorator function to limit the number of calls to another function.

    Args:
        limit (int): The maximum number of calls allowed.

    Returns:
        function: Decorator function to limit calls.
    """
    count = 0
    def callLimiter(function):
        """
        Wrapper function to limit the number of calls to a given function.

        Args:
            function: The function to be limited in calls.

        Returns:
            function: Wrapper function to limit calls.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Check if the number of calls exceeds the limit before calling the function.

            Args:
                *args: Variable length argument list.
                **kwds: Arbitrary keyword arguments.

            Returns:
                Any: Result of calling the function if limit not exceeded, None otherwise.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter


    
    


