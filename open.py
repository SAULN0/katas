def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError as err:
        print("got a problem trying to read the file:", err)

if __name__ == '__main__':
    main()