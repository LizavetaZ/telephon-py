import datetime
import view

def log_cash_import(res_search):
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{res_search}. Время запроса {str(datetime.datetime.now())}\n')

def log_cash_export(result:tuple):
    with open ('log.txt', 'a', encoding='utf-8') as file:
        tmp= [item for item in result]
        tmp.pop(0)
        file.write(f'{tmp}.  Время запроса {str(datetime.datetime.now())}\n')


