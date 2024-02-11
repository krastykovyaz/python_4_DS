from callLimit import callLimit

@callLimit(3)
def f():
    print("f()")

@callLimit(1)
def g():
    print("g()")

def main():
    try:
        for _ in range(3):
            f()
            g()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



# $> python tester.py
# f()
# g()
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times