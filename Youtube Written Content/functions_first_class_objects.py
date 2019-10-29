def small():
    return 30

def large(var):
    return 2*var

def sample():
    return small() + large(small())

def main():
    # Assigned to Variables

    tiny = small

    # Pass as an Argument

    big = large(tiny())

    # print(big)

    # Return a Function
    print(sample())


if __name__ == '__main__':
    main()