from Orders import Orders
from M2Report import M2Report
from DJReport import DJReport
from Comparitor import Comparator
# import pkg_resources
# pkg_resources.require("pandas==1.4.2")
# import pandas as pd

m2_book = 'DakotaJacksonProductionReport2022-05-21'
dj_book = 'OrderDBRead'



### Orders Class Tests ###

# orders = Orders(dj_book)
# orders.get_sheet()
# print(orders.sheet[['OPO']])

# orders = Orders(m2_book)
# orders.get_sheet()
# print(orders.sheet)



### DJReport tests ###

# dj_report = DJReport(dj_book)

# dj_report.get_sheet()
# print(dj_report.sheet)
# print(list(dj_report.sheet.columns))

# dj_report.get_data()
# # dj_report.data_pull(['OPO', 'OSO', 'M2 Job Code'])
# # print((dj_report.orders))

# dj_report.get_order_by_job_code('nhhh')
# print(dj_report.order)

# dj_report.get_current_orders()
# print(dj_report.orders.columns)

# dj_report.get_job_code_list()
# print(dj_report.job_code_list)




#### M2Report Tests ####

# m2_report = M2Report(m2_book)
# m2_report.get_sheet()
# print(m2_report.sheet.columns)


# m2_report.data_pull(['OPO', 'DF quote ', 'M2 Job Code', 'Item Description', 'Qty.','DFA Required', 'DFA Sent', 'DFA Approved', 'Status', 'PO Issue Date', 'FWO #', 'FWO issue Date', 'Wood', 'Wood Finish', 'Metal / Metal Finish', 'SFA/STM Required', 'SFA Sent', 'SFA Approved','COM / COL', 'COM/COL Recieved','Inspection photo sent for approval (DATE)', 'Ex-Factory Date','ship to (East coast, West coast)', 'Notes', ''])
# print(m2_report.orders)

# m2_report.get_data()
# print(m2_report.orders)

# m2_report.get_order_by_job_code('Nhqh')
# print(m2_report.order)

# m2_report.get_current_m2_orders(dj_report.orders['M2 Job Code'])
# dj_report.get_job_code_list()
# print(dj_report.noShippedOrders)
# print(dj_report.job_code_list)
# m2_report.get_current_m2_orders(dj_report.job_code_list)

# print(m2_report.m2_current_orders)



#### blah ####

# print(dj_report.orders)
# print(m2_report.m2_current_orders.columns)
# compareTable = dj_report.orders.compare(m2_report.m2_current_orders)
# print(compareTable)
# # print(dj_report.orders.compare(m2_report.m2_current_orders))

# print(pd.__version__)



#### Comparitor tests ####

comparator = Comparator(dj_book, m2_book)
comparator.compare_lines()
comparator.upload_reports()
# print(comparator)