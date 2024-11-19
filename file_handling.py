import csv


def read_file_contents(filename: str) -> str:

    """

    Read file contents into string.


    :param filename: File to read.

    :return: File contents as string.

    """

    with open(filename, mode="r", encoding="utf-8") as file:

        contents = file.read()

    return contents



def read_file_contents_to_list(filename: str) -> list:

    """

    Read file contents into list of lines.


    :param filename: File to read.

    :return: List of lines.

    """

    with open(filename, mode="r", encoding="utf-8") as file:

        lines = [line.strip() for line in file]

    return lines



def read_csv_file(filename: str) -> list:

    """

    Read CSV file into list of rows.


    :param filename: File to read.

    :return: List of lists.

    """

    with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:

        reader = csv.reader(csv_file)

        return [row for row in reader]



def write_contents_to_file(filename: str, contents: str) -> None:

    """

    Write contents to file.


    :param filename: File to write to.

    :param contents: Content to write to.

    :return: None

    """

    with open(filename, mode="w", encoding="utf-8") as file:

        file.write(contents)



def write_lines_to_file(filename: str, lines: list) -> None:

    """

    Write lines to file.


    :param filename: File to write to.

    :param lines: List of string to write to the file.

    :return: None

    """

    if not lines:

        return

    with open(filename, mode="w", encoding="utf-8") as file:

        for line in lines[:-1]:

            file.write(line + "\n")

        file.write(lines[-1])



def write_csv_file(filename: str, data: list) -> None:

    """

    Write data into CSV file.


    :param filename: Name of the file.

    :param data: List of lists to write to the file.

    :return: None

    """

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerows(data)



def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:

    """

    Merge information from two files into one CSV file.


    :param dates_filename: Input file with names and dates.

    :param towns_filename: Input file with names and towns.

    :param csv_output_filename: Output CSV-file with names, towns and dates.

    :return: None

    """

    dates_dict = {}

    with open(dates_filename, mode="r", encoding="utf-8") as dates_file:

        for line in dates_file:

            name, date = line.strip().split(":")

            dates_dict[name] = date


    towns_dict = {}

    with open(towns_filename, mode="r", encoding="utf-8") as towns_file:

        for line in towns_file:

            name, town = line.strip().split(":")

            towns_dict[name] = town


    output_data = []

    for name in dates_dict:

        town = towns_dict.get(name, "-")

        date = dates_dict[name]

        output_data.append([name, town, date])


    for name in towns_dict:

        if name not in dates_dict:

            town = towns_dict[name]

            output_data.append([name, town, "-"])


    with open(csv_output_filename, mode="w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(["name", "town", "date"])

        writer.writerows(output_data)