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

    def compare_items(self, aa, bb):
        match_index = 0
        item_a = str(aa).lower().strip().split()
        item_b = str(bb).lower().strip().split()

        for word in item_a:
            if word in item_b:
                match_index += 1

        return match_index

        

    def compare_lines(self, export_csv=False):
        discrepencies = []
        no_match = []

        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(self.dj_workbook.orders['OPO']) 

        for index, row in self.dj_workbook.orders.iterrows():

            if self.m2_workbook.m2_current_orders.loc[(self.m2_workbook.m2_current_orders['OPO'] == row['OPO']) & (self.m2_workbook.m2_current_orders['Qty.'] == row['Qty.'])].values.tolist() != []:

                m2_row = self.m2_workbook.m2_current_orders.loc[self.m2_workbook.m2_current_orders['OPO'] == row['OPO']].values.tolist()

                compare_dict = {'OPO': row['OPO'], 'M2 Job Code': row['M2 Job Code'], 'Item Description': row['Item Description'], 'Item Description - M2': m2_row[0][2], 'DJ Qty.': row['Qty.'], 'M2 Qty.': m2_row[0][3], 'DFA Required - DJ': row['DFA Required'], 'DFA Required - M2': m2_row[0][10], 'DFA Approved - DJ': row['DFA Approved'], 'DFA Approved - M2': m2_row[0][12], 'SFA/STM Required - DJ': row['SFA/STM Required'], 'SFA/STM Required - M2': m2_row[0][13], 'SFA Sent': m2_row[0][14], 'SFA Approved - DJ': row['SFA Approved'], 'SFA Approved - M2': m2_row[0][15],'COM/COL Required': row['COM/COL Required'], 'COM/COL Recieved': m2_row[0][9], 'match index': self.compare_items(row['Item Description'], m2_row[0][2])}

                if compare_dict['match index'] > 0:
                    discrepencies.append(compare_dict.values())
                else: 
                    no_match.append(compare_dict.values())
        
        self.compareFrame = pd.DataFrame(discrepencies, columns=compare_dict.keys())
        self.compareFrame.sort_values(by=['OPO', 'match index'], ascending=False)
        self.noMatchFrame = pd.DataFrame(no_match, columns=compare_dict.keys())

        if export_csv:
            filepath_compare = '/Users/maximdiamond/Code/DJi/scripts/comparedReports.csv'
            filepath_noMatch = '/Users/maximdiamond/Code/DJi/scripts/noMatchReports.csv'
            self.compareFrame.to_csv(filepath_compare)
            self.noMatchFrame.to_csv(filepath_noMatch)

        print(self.compareFrame)

    def __repr__(self):
        return str(self.compareFrame)