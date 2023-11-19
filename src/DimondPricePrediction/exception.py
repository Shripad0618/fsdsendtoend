
# to know in which script i am getting the error
#In which line i am getting the error
#What is the error message
# error_details comes from the sys module. it can be int, float . it's like goving pre data type
# exc_tb execution traceback: whatever execution is happening it will give complete details 
# exc_tb.tb_lineno will give line no
#exc_tb.tb_frame.f_code.co_filename will give filename
#sys is a system module in python that gives system related information


import sys
from src.DimondPricePrediction.logger import logging

def error_msg_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Ocurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message