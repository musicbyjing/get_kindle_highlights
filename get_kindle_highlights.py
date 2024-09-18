'''
Arguments: 
    clipping file
    "title of book, as specific as possible"
    output file
'''

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Name of clippings file")
    parser.add_argument("title", help="title of book to retrieve clippings from")
    parser.add_argument("output_file", help="output file name")
    args = parser.parse_args()

    filename = args.filename
    title = args.title
    output = args.output_file

    with open(filename, 'r') as f:
        with open(output, 'a') as g:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if title in line:
                    print(lines[i+3])
                    g.write(lines[i+3])

if __name__ == '__main__':
    main()