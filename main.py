from stats import Stats
import sys

def main():
    num_of_args = len(sys.argv)
    if num_of_args < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    filepath = sys.argv[1]
    frankenstein = Stats(filepath)
    frankenstein.output()







if __name__ == '__main__':
    main()