from DJReport import DJReport
from M2Report import M2Report

m2_book = 'DakotaJacksonProductionReport2022-04-09'
dj_book = 'OrderDBRead'

class Compairitor():

    # def __init__(super):

    def get_m2_current():
        dj_report = DJReport(dj_book)
        dj_report.get_current_orders
        print(dj_report.orders)

        # m2_report = M2Report(m2_book)
        # m2_report.get_current_m2_orders()

def get_m2_current():
    # get DJ orders & current order list by job code 
    dj_report = DJReport(dj_book)
    dj_report.get_current_orders()
    dj_report.get_job_code_list()

    # get current  m2 orders 
    m2_report = M2Report(m2_book)
    m2_report.get_current_m2_orders(dj_report.job_code_list)
    # print(m2_report.orders)


# next up - filter through the orders to compare create list of orders with discrepencies...

# def compare_orders():


get_m2_current()