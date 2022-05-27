# from typing_extensions import Self
from DJReport import DJReport
from M2Report import M2Report
import pandas as pd

m2_book = 'DakotaJacksonProductionReport2022-04-09'
dj_book = 'OrderDBRead'

class Compairitor():

    def __init__(self, dj_book, m2_book):
        self.dj_book = dj_book
        self.m2_book = m2_book
        self.dj_workbook = DJReport(self.dj_book)
        self.m2_workbook = M2Report(self.m2_book)
        self.comparison_report = pd.DataFrame()

    def get_reports(self):
        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(['M2 Job Code'])

    def compare_lines(self):
        discrepencies = []
        col_names = ['OPO', 'M2 Job Code', 'Item Description', 'DJ Qty.', 'M2 Qty.', 'DFA Required - DJ', 'DFA Required - M2', 'SFA Sent', 'SFA Approved', 'COM/COL Required', 'COM/COL Recieved']

        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(self.dj_workbook.orders['OPO']) 

        for index, row in self.dj_workbook.orders.iterrows():

            if self.m2_workbook.m2_current_orders.loc[(self.m2_workbook.m2_current_orders['OPO'] == row['OPO'])].values.tolist() != []:

                m2_row = self.m2_workbook.m2_current_orders.loc[self.m2_workbook.m2_current_orders['OPO'] == row['OPO']].values.tolist()

                compare_row = [row['OPO'], row['M2 Job Code'], row['Item Description'], row['Qty.'], m2_row[0][3], row['DFA Required'], m2_row[0][10], m2_row[0][14], m2_row[0][15], row['COM/COL Required'], m2_row[0][9]]

                discrepencies.append(compare_row)
        
        compareFrame = pd.DataFrame(discrepencies, columns=col_names)
        print(compareFrame)

