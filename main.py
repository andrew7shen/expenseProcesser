# Andrew Shen, 07/03/2022
# python expenseProcesser <path to input_file>
# input_file: path to directory containing PDF expense reports

# Future Steps
# 1. Use JS React or Flask for front-end interface: can query different variables and make different categories
# 2. Scheduled tasks with Airflow every month when expense statements come in
# 3. Use some sort of ML model to make classifications of the payments
# 4. Store transaction data in some datastore (AWS, Azure?)

# Import statements
import sys
import os
import PyPDF2
from class_files import Transaction

# Take in input files
dir_in = sys.argv[1]


# Functions
def convert_all(dir_path):
    """
    Takes in directory path containing multiple PDF bank statements and outputs a list of all transactions
    :param dir_path: Path to directory containing bank statements
    :return: concatenated string with all the transaction information for all bank statements
    """
    all_transact_list = []
    pdf_paths = []
    # Keeps only files in "dir_path" with .pdf extension
    for p in os.listdir(dir_path):
        name, ext = os.path.splitext(p)
        if ext == ".pdf":
            pdf_paths.append("%s/%s" % (dir_path, p))
    # Runs full process_inputs --> make_transaction_list pipeline on all input files
    for path in pdf_paths:
        curr_str = process_inputs(path)
        curr_list = make_transaction_list(curr_str)
        # Adds list of transactions to "all_transact_list"
        all_transact_list.extend(curr_list)
    return all_transact_list


def process_inputs(file_in):
    """
    Converts just page number 3 of PDF expense statement input file into string format
    :param file_in: path to input expense statement in PDF format
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
    # Find index of first and last occurrence of transaction
    for i in range(len(input_str_lines)):
        curr_line = input_str_lines[i]
        if "Purchases and Adjustments" in curr_line:
            start = i+1
        if "TOTAL PURCHASES AND ADJUSTMENTS FOR THIS PERIOD" in curr_line:
            end = i
            break
    input_str_lines = input_str_lines[start:end]
    # Populate transact_list with transactions
    for i in range(len(input_str_lines)):
        curr_line = input_str_lines[i]
        transact_list.append(make_transaction_object(curr_line))
    return transact_list


def make_transaction_object(expense_str):
    """
    Helper function to convert transaction string from input file into transaction object
    :param expense_str: string containing contents of one transaction row from
    :return: Transaction object from the transaction string
    """
    temp = expense_str.split()
    transact_date = temp[0]
    post_date = temp[1]
    info = " ".join(temp[2:-3])
    ref_num = temp[-3]
    amount = temp[-1]
    return Transaction(transact_date, post_date, info, ref_num, amount)


# Outdated
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
    all_transactions = convert_all(dir_in)
    for t in all_transactions:
        t.print_transaction_short()
