import os

SUPPORTED_FILE_TYPES = ['bin', 'hdf', 'hdf5', 'py']


def get_files_in_dir(directory):
    all_files_in_dir = ['{0}{1}'.format(directory, file_path) for file_path in os.listdir(directory) if os.path.isfile(file_path)]
    files_to_rename = [file_path for file_path in all_files_in_dir if supported_file(file_path)]
    return files_to_rename


def supported_file(file_path):
    file_type = file_path.split('.')[1]
    if file_type not in SUPPORTED_FILE_TYPES:
        return False
    else:
        return True


def generate_names(file_list):
    name_dictionary = dict()
    for file_path in file_list:
        name_dictionary[file_path] = generate_name(file_path)
    return name_dictionary


def generate_name(file_path):
    path, filename = os.path.split(file_path)
    if 'XG' in filename:
        return '{0}/{1}'.format(path, generate_rc_name(filename))
    else:
        return file_path


def generate_rc_name(path, filename):
    basename = filename.split('.')[0]
    extension = filename.split('.')[1]

    new_name = reformat_rc_band(basename)
    location = location_from_path(path)
    new_name = '{0}.{1}'.format(reformat_rc_location(new_name, location), extension)
    return new_name


def reformat_rc_band(basename):
    tokens1 = basename.split('(')
    tokens2 = tokens1[1].split(')')
    return '{0}{1}{2}'.format(tokens1[0], tokens2[0], tokens2[1])


def reformat_rc_location(basename, location):
    tokens = basename.split('_')
    return '{0}_{1}_{2}_{3}_{4}'.format(tokens[0], location, tokens[2], tokens[3], tokens[4])


def location_from_path(filepath):
    if 'HP' in filepath or 'harbor_point' in filepath:
        return 'HP'
    else:
        return 'IITSO'


def rename_files(name_dictionary):
    for filename, new_name in name_dictionary.iteritems():
        print '{0} -> {1}'.format(filename, new_name)
