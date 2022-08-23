# Andrew Shen, 07/03/2001
# python expenseProcesser.py <path to input_file>
# input_file: input expense statement file in .txt form

# Future Implementations
# 1. Scheduled tasks with Airflow every month when expense statements come in
# 2. Use JS React or Flask for front-end interface
# 3. Use some sort of ML model to make classifications of the payments

# Import statements
import sys
import PyPDF2

# Take in input files
statement_in = sys.argv[1]


def process_inputs(file_in):
    """
    Converts input files into string format
    :param file_in: input expense statement in PDF format
    :return: file_in_processed
    """
    file_in_str = ""
    # Reading in PDF input file in "rb" form, read and binary
    with open(file_in, "rb") as pdf_obj:
        pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
        # Getting page number 3 (with transaction information"
        page_obj = pdf_reader.getPage(2)
        file_in_str = page_obj.extractText()
        pdf_obj.close()
    return file_in_str


def print_statement(file_to_print):
    """
    Helper function to print out current status of expense statement
    :param file_to_print: variable containing expense statement info
    :return: None
    """
    for i in range(len(file_to_print)):
        curr_line = file_to_print[i]
        formatted_line = ""
        for j in range(len(curr_line)):
            if j != len(curr_line) + 1:
                formatted_line += curr_line[j] + "\t"
            else:
                formatted_line += curr_line[j]
        print(curr_line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    statement_processed = process_inputs(statement_in)
    print(statement_processed)

