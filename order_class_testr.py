from Orders import Orders
from M2Report import M2Report
from DJReport import DJReport

m2_book = 'DakotaJacksonProductionReport2022-04-09'
dj_book = 'OrderDBRead'

# dj_report = DJReport(dj_book)
# dj_report.get_data()
# # print((dj_report.orders))
# # print(list(dj_report.sheet.columns))
# dj_report.get_order_by_job_code('nhhh')
# print(dj_report.order)

m2_report = M2Report(m2_book)
m2_report.get_data()
# print(m2_report.orders)
m2_report.get_order_by_job_code('Nhqh')
print(m2_report.order)