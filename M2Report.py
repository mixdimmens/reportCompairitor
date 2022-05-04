from Orders import Orders

class M2Report(Orders):

    def __init__(self, workbook, sheet_index= 0):
        super().__init__(workbook, sheet_index= 0)

    def get_data(self):
        cols = ['OPO', 'M2 Job Code', 'Item Description', 'Qty.', 'PO Issue Date', 'Wood', 'Wood Finish', 'Metal / Metal Finish', 'COM / COL', 'COM/COL Recieved', 'DFA Required', 'DFA Sent', 'DFA Approved', 'SFA/STM Required', 'SFA Sent', 'SFA Approved']
        self.data_pull(cols)

    def get_current_m2_orders(self, current_order_list_to_compare):
        self.get_data()
        self.m2_current_orders =  self.orders.loc[self.orders['M2 Job Code'].isin(current_order_list_to_compare)]      

    def __repr__(self):
        return self.orders

    