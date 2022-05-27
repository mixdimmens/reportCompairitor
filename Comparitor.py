# from typing_extensions import Self
from DJReport import DJReport
from M2Report import M2Report
import pandas as pd

m2_book = 'DakotaJacksonProductionReport2022-04-09'
dj_book = 'OrderDBRead'

class Comparator():

    def __init__(self, dj_book, m2_book):
        self.dj_book = dj_book
        self.m2_book = m2_book
        self.dj_workbook = DJReport(self.dj_book)
        self.m2_workbook = M2Report(self.m2_book)
        self.comparison_report = pd.DataFrame()

    def get_reports(self):
        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(['M2 Job Code'])

    def dict_to_list(dictionary):
        keys = [*dictionary.keys()]
        vals = []
        for ii in dictionary.keys():
            keys.append()

    def compare_lines(self, export_csv=False):
        discrepencies = []

        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(self.dj_workbook.orders['OPO']) 

        for index, row in self.dj_workbook.orders.iterrows():

            if self.m2_workbook.m2_current_orders.loc[(self.m2_workbook.m2_current_orders['OPO'] == row['OPO']) & (self.m2_workbook.m2_current_orders['Qty.'] == row['Qty.'])].values.tolist() != []:

                m2_row = self.m2_workbook.m2_current_orders.loc[self.m2_workbook.m2_current_orders['OPO'] == row['OPO']].values.tolist()

                compare_dict = {'OPO': row['OPO'], 'M2 Job Code': row['M2 Job Code'], 'Item Description': row['Item Description'], 'Item Description - M2': m2_row[0][2], 'DJ Qty.': row['Qty.'], 'M2 Qty.': m2_row[0][3], 'DFA Required - DJ': row['DFA Required'], 'DFA Required - M2': m2_row[0][10], 'DFA Approved - DJ': row['DFA Approved'], 'DFA Approved - M2': m2_row[0][12], 'SFA/STM Required - DJ': row['SFA/STM Required'], 'SFA/STM Required - M2': m2_row[0][13], 'SFA Sent': m2_row[0][14], 'SFA Approved - DJ': row['SFA Approved'], 'SFA Approved - M2': m2_row[0][15],'COM/COL Required': row['COM/COL Required'], 'COM/COL Recieved': m2_row[0][9]}

                discrepencies.append(compare_dict.values())
        
        self.compareFrame = pd.DataFrame(discrepencies, columns=compare_dict.keys())

        if export_csv:
            filepath = '/Users/maximdiamond/Code/DJi/scripts/comparedReports.csv'
            self.compareFrame.to_csv(filepath)

        print(self.compareFrame)

    def __repr__(self):
        return str(self.compareFrame)