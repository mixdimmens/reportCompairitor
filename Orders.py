import pandas as pd
import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials

class Orders(object):

    def __init__(self, workbook, sheet_index= 0):
        self.workbook = workbook
        self.sheet_index = sheet_index
    
    def get_sheet(self):
        # define the scope
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        # add credentials to the account - json file must be located via at least a relative path
        creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/maximdiamond/Code/DJi/scripts/pdfScripts/production-report-api-739f8c22e6b8.json', scope)

        # authorize the clientsheet 
        client = gspread.authorize(creds)

        self.workbook = client.open(self.workbook)
        self.sheet = pd.DataFrame(self.workbook.get_worksheet(self.sheet_index).get_all_records())
        self.sheet = self.sheet[self.sheet['M2 Job Code'].str.len() >= 1]
        self.columns = list(self.sheet.columns)

        for col in self.sheet:
            self.sheet[col] = self.sheet[col].apply(str)
        
        for col in self.sheet:
            self.sheet[col] = self.sheet[col].apply(lambda xx : re.escape(xx))

    def data_pull(self, cols):
        self.get_sheet()
        self.orders = self.sheet[self.sheet[cols]]

    def get_order_by_job_code(self, job_code):
        self.order = self.orders.loc[self.orders['M2 Job Code'].str.contains(job_code, case= False, na=False)]

    def get_order_by_oso(self, oso):
        self.order = self.orders.loc[self.orders['OSO'].str.contains(oso, case= False, na= False)]

    def get_order_by_opo(self, opo):
        self.order = self.orders.loc[self.orders['OPO'].str.contains(opo, case= False, na= False)]

    def get_job_code_list(self):
        self.job_code_list = self.orders[['M2 Job Code']]

    def get_opo_list(self):
        self.opo_list = self.orders[['OPO']]

    def get_oso_list(self):
        self.oso_list = self.orders[['OSO']]

    # order method not yet working
    def order(self, oso, dict= True):
        self.get_sheet()
        if not dict:
            self.order = self.sheet.loc[self.sheet['OSO'] == oso]
        else:
            self.order = self.sheet.loc[self.sheet['OSO'] == oso].to_dict('list')

    def __repr__(self):
        return str(self.sheet)