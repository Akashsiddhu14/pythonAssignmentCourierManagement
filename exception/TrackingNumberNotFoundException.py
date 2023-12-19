class TrackingNumberNotFoundException(Exception):
    def __init__(self,message="Tracking number not found"):
        self.message=message
        super().__init__(self.message)
class BankAccount:
    def __init__(self,account_number,balance):
        self.AccountNumber=account_number
        self.Balance=balance

    def withdraw(self,amount,tracking_number):
        if tracking_number not in [1, 2, 3]:
            raise TrackingNumberNotFoundException()

    def transfer(self,amount,tracking_number,recipient_account):
        if tracking_number not in [1, 2, 3]:
            raise TrackingNumberNotFoundException()
class BankException:
    def raise_exception(self):
        try:
            account=BankAccount(123456, 1000.0)
            withdrawal_tracking_number=int(input("Enter withdrawal tracking number: "))
            account.withdraw(100.0,withdrawal_tracking_number)
            print("Withdrawal successful.")
        except TrackingNumberNotFoundException:
            print("Tracking number not found. Withdrawal failed.")
        try:
            transfer_tracking_number=int(input("Enter transfer tracking number: "))
            recipient_account=BankAccount(654321,500.0)
            account.transfer(200.0,transfer_tracking_number,recipient_account)
            print("Transfer successful.")
        except TrackingNumberNotFoundException:
            print("Tracking number not found. Transfer failed.")

obj8=BankException()
obj8.raise_exception()