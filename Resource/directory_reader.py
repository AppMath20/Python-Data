import os
import functools

format_position_in_split = -1
format_req = 'txt'


def print_iter(reader):  # a function decorator
    @functools.wraps(reader)
    def dir_reader_decorator(*args, **kwargs):  # The class that will contain the wrapped class
        inner_reader = reader(*args, **kwargs)
        for result in inner_reader:
            print(result)
            yield result
    return dir_reader_decorator


def check_file_name(file_name):
    return file_name.split('.')[format_position_in_split] == format_req


@print_iter
class DirReader:  # To read files in a directory
    def __init__(self, dir):
        self.walk = os.walk(dir)

    def work(self):
        for root, dirs, file_names in self.walk:
            for file_name in file_names:
                # If the file matches the format we need
                if check_file_name(file_name):
                    yield root + "\\" + file_name  # giving the canonical path

    def __iter__(self):
        return self.work()
