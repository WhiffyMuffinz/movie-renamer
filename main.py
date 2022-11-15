import os
import argparse
import re


def main():
    args = get_args()
    input_path = os.path.expanduser(args.input)

    for path, subdirs, files in os.walk(input_path):
        for subdir in subdirs:
            path_to = os.path.join(path, subdir)
            for file in os.listdir(path_to):
                print(
                    "{} --> {}".format(
                        os.path.join(subdir, file),
                        os.path.join(subdir, rename(subdir, file)),
                    )
                )
                os.rename(
                    os.path.join(path_to, file),
                    os.path.join(path_to, rename(subdir, file)),
                )


def get_args():
    parser = argparse.ArgumentParser(
        prog="Movie renamer",
        description="Renames Movies to a standard format",
    )
    parser.add_argument("-i", help="Input folder", required=True, dest="input")
    args = parser.parse_args()

    return args


def rename(parent_directory: str, file: str):
    if file.__contains__(parent_directory):
        return file

    return parent_directory + re.sub("E\d+", "", file)


if __name__ == "__main__":
    main()
