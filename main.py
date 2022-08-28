# Andrew Shen, 07/03/2022
# python expenseProcesser.py <path to input_file>
# input_file: input expense statement file in .txt form

# Future Steps
# 1. Use JS React or Flask for front-end interface: can query different variables and make different categories
# 2. Scheduled tasks with Airflow every month when expense statements come in
# 3. Use some sort of ML model to make classifications of the payments

# Import statements
import sys
import PyPDF2
from class_files import Transaction

# Take in input files
statement_in = sys.argv[1]


# Functions
def process_inputs(file_in):
    """
    Converts just page number 3 of expense statement input file into string format
    :param file_in: input expense statement in PDF format
    :return: file_in_str: string version of input expense statement
    """
    # Reading in PDF input file in "rb" form, read and binary
    with open(file_in, "rb") as pdf_obj:
        pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
        # Getting page number 3 (with transaction information)
        page_obj = pdf_reader.getPage(2)
        file_in_str = page_obj.extractText()
        pdf_obj.close()
    return file_in_str


def make_transaction_list(input_str):
    """
    Converts info in input expense statement (page 3) to transactions and returns list of transactions
    :param input_str: string version of input expense statement
    :return: transact_list: list of transactions
    """
    transact_list = []
    input_str_lines = input_str.splitlines()
    # Extract just the transaction info
    start = 8
    end = None
    # Find index of last occurrence of transaction
    for i in range(len(input_str_lines)):
        curr_line = input_str_lines[i]
        if "TOTAL PURCHASES AND ADJUSTMENTS FOR THIS PERIOD" in curr_line:
            end = i
            break
    input_str_lines = input_str_lines[start:end]
    # Populate transact_list with transactions
    for i in range(len(input_str_lines)):
        curr_line_split = input_str_lines[i].split("\t")
        print(curr_line_split)
        # TO-DO: need to create Transaction objects from each line of transaction info
        # transact_list.append(Transaction)
    return transact_list


def print_statement(file_to_print):
    """
    Helper function to print out current status of expense statement
    :param file_to_print: file containing expense info in list of lists format
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


# Main function
if __name__ == '__main__':
    statement_processed = process_inputs(statement_in)
    transaction_list = make_transaction_list(statement_processed)
    # print(statement_processed)

    # Test transaction object creation
    test_transact = Transaction(1, 12, "8/23", "8/25", "test transaction")
    # test_transact.print_transaction()
    # print(test_transact.amount)
