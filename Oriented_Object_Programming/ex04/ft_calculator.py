class Calculator:
    """
    A class to perform vector calculations.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (List[float]): First vector.
            V2 (List[float]): Second vector.

        Returns:
            float: The dot product of the two vectors.
        """
        try:
            out = 0
            for i in range(len(V1)):
                out += (V1[i] * V2[i])
            return f"Dot product is: {out}"
        except Exception as e:
            print(e)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise.

        Args:
            V1 (List[float]): First vector.
            V2 (List[float]): Second vector.

        Returns:
            List[float]: The resulting vector after addition.
        """
        try:
            out = [0. for _ in range(len(V1))]
            for i in range(len(V1)):
                out[i] += (V1[i] + V2[i])
            return f"Add Vector is : {out}"
        except Exception as e:
            print(e)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise.

        Args:
            V1 (List[float]): First vector.
            V2 (List[float]): Second vector.

        Returns:
            List[float]: The resulting vector after subtraction."""
        try:
            out = [0. for _ in range(len(V1))]
            for i in range(len(V1)):
                out[i] += (V1[i] - V2[i])
            return f"Sous Vector is: {out}"
        except Exception as e:
            print(e)
