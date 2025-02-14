import sys
import logging

def error_message_detail(error):
    # Use sys.exc_info to get the current exception information
    exc_type, exc_value, exc_tb = sys.exc_info()
    # Extract the filename and line number from the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    # Format the detailed error message
    error_message = f"""Error occured in python script, Please see the following for details \n 
    Type: [{exc_type}] \n 
    Value: [{exc_value}]\n 
    Name: [{file_name}]\n 
    Line number: [{line_number}]\n 
    Error message: [{str(error)}]"""
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        # Initialize the base Exception with the error_message
        super().__init__(error_message)
        # Retrieve and store the detailed error message using the current exception
        self.error_message = error_message_detail(error_message)
    
    def __str__(self):
        # Return the custom error message when the exception is printed
        return self.error_message

'''
# Example usage:
try:
    # Simulate an error
    1 / 0
except Exception as e:
    logging.info("Dividing by Zero")
    raise CustomException(str(e)) from e
'''