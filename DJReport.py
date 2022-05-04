from Orders import Orders

class DJReport(Orders):

    def __init__(self, workbook, sheet_index= 0):
        super().__init__(workbook, sheet_index= 0)

    def get_data(self):
        cols = ['OPO', 'M2 Job Code', 'Item Description', 'Qty.', 'PO Issue Date', 'Wood', 'Wood Finish', 'Metal / Metal Finish', 'COM/COL Required', 'COM/COL Recieved', 'DFA Required', 'DFA Sent', 'DFA Approved', 'SFA/STM Required', 'SFA Sent', 'SFA Approved']
        self.data_pull(cols)

    # def get_order_by_job_code(self, job_code):
    #     self.order = self.orders[self.orders['M2 Job Code'].str.contains(job_code, case= False, na= False)]

    # def get_order_by_oso(self, oso):
    #     self.order = self.orders[self.orders['OSO'].str.contains(oso, case= False, na= False)]

    # def get_order_by_opo(self, opo):
    #     self.order = self.orders[self.orders['OPO'].str.contains(opo, case= False, na= False)]



    def __repr__(self):
        return self.orders