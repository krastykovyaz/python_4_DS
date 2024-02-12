from datetime import datetime


def main():
    """
    Print the current timestamp in scientific notation and the formatted date.
    """
    try:
        # Get the current timestamp
        timestamp = datetime.timestamp(datetime.now())

        # Format the timestamp in scientific notation
        scientific_notation = "{:,.4f}".format(timestamp)

        # Format the current date
        formatted_date = datetime.now().strftime("%b %d %Y")

        # Print the formatted output
        print(f"Seconds since January 1, 1970: {scientific_notation} \
or {timestamp:.2e} in scientific notation")
        print(formatted_date)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
