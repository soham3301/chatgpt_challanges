
#? Note:- A real loan depends on much more variables. Here it's a small demo

#? Rule 1 :- Loan is allowed maximum 10 times of bank balance
#? Rule 2 :- Loan is alllowed if EMI is below 60% of monthly income

class Loan:
    def __init__(self, cust_id):
        self.attached_customer = cust_id
        self.loan_account_number = None
        self.loan_amount = None
        self.repayment_amount = None
        self.amount_paid_till_now = None
        self.loan_interest = 12
        self.emi_amount = None
        self.total_emi = None
        self.paid_emi = None
        self.pending_emi = None
        self.repayment_tenures_in_month = [12, 24, 36, 48, 60]

    def generate_one_year_repayment_amount(self, req_amount):
        one_year_repayment_amount = ((self.loan_interest / 100) * req_amount) + req_amount
        return one_year_repayment_amount

    def generate_repayment_amount_and_emi(self, requested_amount, months):
        repayment_amount = 0
        emi = 0
        input_amount = requested_amount
        for _ in range(round(months/12)):
            repayment_amount = self.generate_one_year_repayment_amount(input_amount)
            input_amount = repayment_amount
            emi = repayment_amount / months
        return [round(repayment_amount), round(emi)]

    def find_eligible_loans(self, loan_amount, emi, income, bank_bal):
        return loan_amount <= bank_bal * 10 and emi <= round(income * 60/100)

    def check_loan_possibility(self, requested_amount, monthly_income, bank_balance):
        possible_loan_options = {}
        repayment_emi_list = []
        serial_no = 0
        for tenure in self.repayment_tenures_in_month:
            repayment_amount_and_emi_amount_list = self.generate_repayment_amount_and_emi(requested_amount, tenure)
            repayment_amount_and_emi_amount_list.append(tenure)
            repayment_emi_list.append(repayment_amount_and_emi_amount_list)
        for repayment_and_emi in repayment_emi_list:
            if self.find_eligible_loans(repayment_and_emi[0], repayment_and_emi[1], monthly_income, bank_balance):
                serial_no += 1
                possible_loan_options[serial_no] = {
                    "loan_amount": requested_amount,
                    "repayment_amount": repayment_and_emi[0],
                    "tanure_in_months": repayment_and_emi[2],
                    "yearly_interest": self.loan_interest,
                    "monthly_emi": repayment_and_emi[1]
                }
        return possible_loan_options
        




# loan = Loan(123)

# loan.check_loan_possibility(100000, 10000, 50000)