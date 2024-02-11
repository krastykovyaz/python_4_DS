# ft_package

This is a simple Python package named `ft_package` with the following structure:

ft_package/
|-- ft_package/
| |-- init.py
| |-- module.py
|-- setup.py


## Installation

To install the package, you can use the following steps:

1. Install the `build` tool:

    ```bash
    pip install build
    ```

2. Build the package by running the following command inside the `ft_package` directory:

    ```bash
    python -m build
    ```

    This will create distribution files in the `./dist/` directory.

3. Install the package inside the package directory using one of the following commands:

    ```bash
    pip install -e .
    ```

    or

    ```bash
    pip install ./dist/ft_package-0.0.1.tar.gz
    ```

    or

    ```bash
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    ```

4. If you are outside the folder, you can still install the package using:

    ```bash
    pip install -e ft_package
    ```

## Usage

After installation, you can use the `ft_package` module in your Python scripts or interactive sessions.

```python
from ft_package import module
```

# Use functions from the module
result = module.count_in_list(["toto", "tata", "toto"], "toto")
print(result)  # Output: 2
