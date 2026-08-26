
#? Note:- A real loan depends on much more variables. Here it's a small demo

#? Rule 1 :- Loan is allowed maximum 10 times of bank balance
#? Rule 2 :- Loan is alllowed if EMI is below 60% of monthly income
#? Note:- Mistakenly used tenure and tanure in several places.

#? Note:- Do I need to write the loan interest and tenures list into json file? I don't know

class Loan:
    def __init__(self, cust_id):
        self.attached_customer = cust_id
        self.loan_account_number = None
        self.loan_amount = 0
        self.repayment_amount = 0
        self.amount_paid_till_now = 0
        self.loan_interest = 12
        self.loan_tanure_in_months = 0
        self.emi_amount = 0
        self.emi_status = {
            "total": 0,
            "paid": 0,
            "unpaid": 0,
        }
        self.repayment_tenures_in_month = [12, 24, 36, 48, 60]

    def generate_loan_ac_number(self, ac_no, name, age, tanure, emi):
        first_l = name[0]
        second_l = str(ac_no)[0]
        self.loan_account_number = first_l + second_l + str(age) + str(tanure) + str(emi)[0]

    def populate_loan_details(self, loan_amt, repay_amt, emi, tanure):
        self.loan_amount = loan_amt
        self.repayment_amount = repay_amt
        self.emi_amount = emi
        self.loan_tanure_in_months = tanure
        self.emi_status["total"] = tanure
        self.emi_status["unpaid"] = tanure

    def load_previous_data(self, loan_dict):
        self.loan_account_number = loan_dict["loan_account_number"]
        self.loan_amount = loan_dict["loan_amount"]
        self.repayment_amount = loan_dict["repayment_amount"]
        self.amount_paid_till_now = loan_dict["amount_paid_till_now"]
        self.loan_interest = loan_dict["loan_interest"]
        self.loan_tanure_in_months = loan_dict["loan_tanure_in_months"]
        self.emi_amount = loan_dict["emi_amount"]
        self.emi_status = loan_dict["emi_status"]
        self.repayment_tenures_in_month = loan_dict["repayment_tenures_in_month"]

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

    def find_eligible_loans(self, repay_amount, emi, income, bank_bal):
        return repay_amount <= bank_bal * 10 and emi <= round(income * 60/100)

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
                    "monthly_emi": repayment_and_emi[1],
                    "monthly_income": monthly_income
                }
        return possible_loan_options
        
