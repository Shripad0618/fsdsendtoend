import sys
class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message  = error_message
        _,_,exc_tb = error_details.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

# to know in which script i am getting the error
#In which line i am getting the error
#What is the error message
# error_details comes from the sys module. it can be int, float . it's like goving pre data type
# exc_tb execution traceback: whatever execution is happening it will give complete details 
# exc_tb.tb_lineno will give line no
#exc_tb.tb_frame.f_code.co_filename will give filename
#sys is a system module in python that gives system related information


    def __str__(self):
        return "Error Ocurred in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.line_no,self.error_message )
    

if __name__ == "__main__" :
    try :
        a = 1/0

    except Exception as e:
        raise customexception(e,sys)