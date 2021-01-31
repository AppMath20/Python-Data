from Resource import file_reader as fr
from Resource import directory_reader as dir_read


# The format of the data
# ID	Name	Hour(hour)	Machine	Seq
# 0	Petr Mazeev	16	IDSSA1	GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


def read_researches(dir_path):
    # To record studies that satisfy us
    researches = []
    dir_reader = dir_read.DirReader(dir_path)
    # We get the canonical file name that matches our conditions
    for file_name in dir_reader:
        # With the help of our generator, which will give us the correct lines
        with fr.FileReader(file_name) as record_reader:
            # Getting the correct string
            for record in record_reader:
                # We write the string of this study to our class and it to the list of studies
                researches.append(Research(record))
    return researches


def get_unique_machines(researches):
    return set(research.machine for research in researches)


def get_max_research_hour_for_machine(machines, researches):
    max_research_hour_for_machine = []
    for machine in machines:
        researches_per_hour = {}
        for research in researches:
            if research.machine == machine:
                count_researches = researches_per_hour.get(research.hour, 0)
                researches_per_hour[research.hour] = count_researches + 1
        max_researches_per_hour = max(researches_per_hour, key=lambda k: researches_per_hour[k])
        max_research_hour_for_machine.append((machine, max_researches_per_hour))
        # Clearing the dictionary
        researches_per_hour.clear()
    return max_research_hour_for_machine


def get_unique_scientist_name(researches):
    return set(research.full_name for research in researches)


PATH_TO_RESULT = "D:\REPOSITORY\Python UI\Python_CLASS\CLASS Project\Exam project_1\Result\Result.txt"
LINE_DELIMITER = "\n"
LINE_TAB = "\\"


def write_result(file_name, max_research_hour_for_machine):
    with open(file_name, "w") as file_output:
        for name, hours in max_research_hour_for_machine:
            file_output.write("Name:" + name + " Hours:" + hours + LINE_DELIMITER)


def write_researches_per_scientist(researchers, researches, dir_to_save):
    SCIENTIST_RESULT_EXTENSION = ".txt"
    # For all researchers, we create a file and write all the information about their
    for researcher in researchers:
        with open(dir_to_save + LINE_TAB + researcher + SCIENTIST_RESULT_EXTENSION, "w") as file_output:
            for research in researches:
                if research.full_name == researcher:
                    file_output.write(str(research))


class Research:
    def __init__(self, line):
        _, first_name, second_name, hour, machine, seq = line.split()
        # Collected last name first name in full name
        self.full_name = first_name + " " + second_name
        self.hour = hour
        self.machine = machine
        self.seq = seq

    def __str__(self):
        return self.machine + " " + self.hour + " " + self.seq + LINE_DELIMITER


DIR_TO_SAVE = "D:\REPOSITORY\Python UI\Python_CLASS\CLASS Project\Exam project_1\Data\Researcher_data"


def main():
    dir_path = "D:\REPOSITORY\Python UI\Python_CLASS\CLASS Project\Exam project_1\Data\data"
    researches = read_researches(dir_path)
    unique_machines = get_unique_machines(researches)
    max_research_hour_per_machine = get_max_research_hour_for_machine(unique_machines, researches)
    unique_scientist_name = get_unique_scientist_name(researches)
    write_result(PATH_TO_RESULT, max_research_hour_per_machine)
    write_researches_per_scientist(unique_scientist_name, researches, DIR_TO_SAVE)


main()
