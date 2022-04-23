from Orders import Orders

class M2Report(Orders):

    def __init__(self, workbook, sheet_index= 0):
        super().__init__(workbook, sheet_index= 0)

    def get_data(self):
        self.get_sheet()
        # self.orders = self.sheet[['OPO', 'M2 Job Code', 'Item Description', 'Qty.', 'PO Issue Date', 'Wood', 'Wood Finish', 'Metal / Metal Finish', 'COM / COL', 'COM/COL Recieved', 'DFA Required', 'DFA Sent', 'DFA Approved', 'SFA/STM Required', 'SFA Sent', 'SFA Approved']]
        cols = ['OPO', 'M2 Job Code', 'Item Description', 'Qty.', 'PO Issue Date', 'Wood', 'Wood Finish', 'Metal / Metal Finish', 'COM / COL', 'COM/COL Recieved', 'DFA Required', 'DFA Sent', 'DFA Approved', 'SFA/STM Required', 'SFA Sent', 'SFA Approved']
        self.data_pull(cols)

    def __repr__(self):
        return self.orders

    