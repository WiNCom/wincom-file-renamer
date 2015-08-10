import os
import argparse

from filename_fns import *


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', default=os.getcwd(), help='The directory to rename files in')
    return parser.parse_args()


def normalize_directory(dir):
    dir = '/'.join(dir.split('\\'))
    if not dir.endswith('/'):
        dir = '{0}/'.format(dir)
    return dir


def valid_directory(directory):
    if not os.path.isdir(directory):
        return False
    else:
        return True


def execute(directory):
    file_list = get_files_in_dir(directory)
    name_dictionary = generate_names(file_list)
    rename_files(name_dictionary)


if __name__ == '__main__':
    arguments = init()
    directory = normalize_directory(arguments.dir)
    if not valid_directory(directory):
        print "[-] Directory '{0}' invalid! Exiting...".format(directory)
    else:
        execute(directory)
