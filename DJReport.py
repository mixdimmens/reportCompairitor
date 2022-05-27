from Orders import Orders

class DJReport(Orders):

    def __init__(self, workbook, sheet_index= 0):
        super().__init__(workbook, sheet_index= 0)

    def get_data(self):
        cols = ['OPO', 'M2 Job Code', 'Item Description', 'Qty.', 'PO Issue Date', 'Wood', 'Wood Finish', 'Metal / Metal Finish', 'COM/COL Required', 'COM/COL Recieved', 'DFA Required', 'DFA Sent', 'DFA Approved', 'SFA/STM Required', 'SFA Sent', 'SFA Approved', 'Status']
        self.data_pull(cols)

    def get_current_orders(self):
        self.get_data()

        self.orders = self.orders[~self.orders['Status'].str.contains('SHIPPED', case=False, na=False)]

    def __repr__(self):
        return self.orders