import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    """Base class for all exceptions in the Network Security module."""
    def __init__(self, error_message , error_details:sys):
        self.error_message = error_message
        _,_,exc_tb  = error_details.exc_info()
        
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    
    def __str__(self):
        return f"Error occureed in script name [{0}] at line number [{1}] with error message [{2}]".format(
        self.file_name  , self.line_number ,str(self.error_message))
        
        
        
if __name__ == "__main__":
    try:
        logger.logging.info("Enter try block")
        a =1/0
        print("This will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
        
        
        
      