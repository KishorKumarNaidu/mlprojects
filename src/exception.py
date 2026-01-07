import sys

def error_messgae_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".formate()"
