from classes import Helper


def main():
    with Helper() as helper:
        helper.running()


if __name__ == '__main__':
    main()
