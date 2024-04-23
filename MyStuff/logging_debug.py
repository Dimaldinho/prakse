import logging
#logging.disable(logging.CRITICAL)   =>  disable logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s -  %(message)s') #config
logging.debug('Start of program') #Debug message

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1): #range starts from 0
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')


######
#   Disable messages:
#   logging.disable(logging.CRITICAL) call. 
# 
#
#   Diferent types of messages:
#   logging.debug()
#   logging.info()
#   logging.warning()
#   logging.error()
#   logging.critical()
#
#   Save messages to file:
#   logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')