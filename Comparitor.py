from typing_extensions import Self
from DJReport import DJReport
from M2Report import M2Report

m2_book = 'DakotaJacksonProductionReport2022-04-09'
dj_book = 'OrderDBRead'

class Compairitor():

    def __init__(self, dj_book, m2_book):
        self.dj_book = dj_book
        self.m2_book = m2_book
        self.dj_workbook = DJReport(self.dj_book)
        self.m2_workbook = M2Report(self.m2_book)

    def get_reports(self):
        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(['M2 Job Code'])

    # def 
