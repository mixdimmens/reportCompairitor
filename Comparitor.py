from DJReport import DJReport
from M2Report import M2Report
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


m2_book = 'DakotaJacksonProductionReport2022-04-09'
dj_book = 'OrderDBRead'

class Comparator():

    def __init__(self, dj_book, m2_book, report_book='M2-DJ_report_compairison'):
        self.dj_book = dj_book
        self.m2_book = m2_book
        self.dj_workbook = DJReport(self.dj_book)
        self.m2_workbook = M2Report(self.m2_book)
        self.report_book = report_book
        self.comparison_report = pd.DataFrame()

    def get_reports(self):
        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(['M2 Job Code'])

    def compare_items(self, aa, bb):
        match_index = 0
        item_a = str(aa).lower().replace("\\", "").strip("()/ -").split()
        item_b = str(bb).lower().replace("\\", "").strip("()/ -").split()

        for word in item_a:
            if word in item_b:
                match_index += 1

        return match_index

    def yes_no_to_bool(self, in_string):
        yesses = ['yes', 'standard', 'YES', 'Yes', 'TRUE']
        nos = ['no', 'No', 'FALSE']

        if type(in_string) != str:
            try:
                in_string = str(in_string)
            except Exception as ee:
                print('yes_no_to_bool\'s string conversion raised an error')
                print(ee)

        # if len(in_string)

        in_string = in_string.lower().strip().replace('\\', '') 
                
        if in_string in yesses:
            return True
        elif in_string in nos:
            return False
        else:
            print('yes_no_to_bool input uncaught')
            return in_string

        
    def strBool_to_bool(self, in_str):
        bool_str_true = ['TRUE', 'True', 'true']
        bool_str_false = ['FALSE', 'False', 'false']


        if in_str in bool_str_true:
            return True
        elif in_str in bool_str_false:
            return False
        else:
            print('yes_no_to_bool boolean uncaught')
            return in_str


        

    def compare_lines(self, export_csv=False):
        matched_lines = []
        no_match = []

        self.dj_workbook.get_current_orders()
        self.m2_workbook.get_current_m2_orders(self.dj_workbook.orders['OPO']) 

        for index, row in self.dj_workbook.orders.iterrows():

            if self.m2_workbook.m2_current_orders.loc[(self.m2_workbook.m2_current_orders['OPO'] == row['OPO']) & (self.m2_workbook.m2_current_orders['Qty.'] == row['Qty.'])].values.tolist() != []:

                m2_row = self.m2_workbook.m2_current_orders.loc[self.m2_workbook.m2_current_orders['OPO'] == row['OPO']].values.tolist()

                compare_dict = {'OPO': row['OPO'], 'M2 Job Code': row['M2 Job Code'], 'Item Description': row['Item Description'], 'Item Description - M2': m2_row[0][2], 'DJ Qty.': row['Qty.'], 'M2 Qty.': m2_row[0][3], 'DFA Required - DJ': self.strBool_to_bool(row['DFA Required']), 'DFA Required - M2': self.yes_no_to_bool(m2_row[0][10]), 'DFA Approved - DJ': row['DFA Approved'], 'DFA Approved - M2': m2_row[0][12], 'SFA/STM Required - DJ': self.strBool_to_bool(row['SFA/STM Required']), 'SFA/STM Required - M2': self.yes_no_to_bool(m2_row[0][13]), 'SFA Sent': m2_row[0][14], 'SFA Approved - DJ': row['SFA Approved'], 'SFA Approved - M2': m2_row[0][15],'COM/COL Required': self.strBool_to_bool(row['COM/COL Required']), 'COM/COL Recieved': m2_row[0][9], 'match index': self.compare_items(row['Item Description'].title(), m2_row[0][2].title())}

                if compare_dict['match index'] > 1:
                    matched_lines.append(compare_dict.values())
                else: 
                    no_match.append(compare_dict.values())
        
        self.compareFrame = pd.DataFrame(matched_lines, columns=compare_dict.keys())
        self.compareFrame.sort_values(by=['OPO', 'match index'], ascending=False)
        self.noMatchFrame = pd.DataFrame(no_match, columns=compare_dict.keys())

        if export_csv:
            filepath_compare = '/Users/maximdiamond/Code/DJi/scripts/comparedReports.csv'
            filepath_noMatch = '/Users/maximdiamond/Code/DJi/scripts/noMatchReports.csv'
            self.compareFrame.to_csv(filepath_compare)
            self.noMatchFrame.to_csv(filepath_noMatch)

    # method to upload reports to report_book
    def upload_reports(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        # add credentials to the account - json file must be located via at least a relative path
        creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/maximdiamond/Code/DJi/scripts/pdfScripts/production-report-api-739f8c22e6b8.json', scope)

        # authorize the clientsheet 
        client = gspread.authorize(creds)

        self.report_book = client.open(self.report_book)
        try:
            self.compared_report = self.report_book.get_worksheet(0)
            self.no_match_report = self.report_book.get_worksheet(1)
            self.compared_report.clear()
            self.no_match_report.clear()
        except Exception as eee:
            print('no workey :\(')
            print(eee)

        try:
            self.compared_report.update([self.compareFrame.columns.tolist()] + self.compareFrame.values.tolist())
            self.no_match_report.update([self.noMatchFrame.columns.tolist()] + self.noMatchFrame.values.tolist())
        except Exception as ee:
            print(self.report_book)
            print('no workey :\(')
            print(ee)

    def __repr__(self):
        return str(self.compareFrame)