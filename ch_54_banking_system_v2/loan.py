
#? Note:- A real loan depends on much more variables. Here it's a small demo

#? Rule 1 :- Loan is allowed maximum 10 times of bank balance
#? Rule 2 :- Loan is alllowed if EMI is below 60% of monthly income
#? Note:- Mistakenly used tenure and tanure in several places.

#? Note:- Do I need to write the loan interest and tenures list into json file? I don't know
#? Note:- Repayment amount and loan tanure will decrease after each emi payment.

#? Note:- Here, self.attached_customer holds customer ID, not the customer object. The name might be confusing

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

    def validate_emi_amount(self, paid_amount):
        return paid_amount == self.emi_amount

    def validate_full_repayment_amount(self, paid_amount):
        return paid_amount == self.repayment_amount

    def is_all_emis_paid(self):
        #* Note:- Because of round(repay_amt / loan_tanure), sometimes emi * tanure not always matches exactly the repayment_amount.
        if self.emi_status["paid"] == self.emi_status["total"]:
            self.repayment_amount = 0
            return True
        else:
            return False

    def receive_emi_amount(self, emi):
        self.repayment_amount -= emi
        self.amount_paid_till_now += emi
        self.emi_status["paid"] += 1
        self.emi_status["unpaid"] -= 1
        self.loan_tanure_in_months -= 1

    def receive_full_repayment_amount(self, full_amount):
        #* Note:- In real banks, during pre closure of loan, the repayment amount decreases because the interest doesn't apply fully.
        #* Note:- So the interest is applied from loan opening date to loan closing date. However, for simplicity purpose, I am not calculating new repayment amount based on closing date.
        #* Note:- Anohter point, during real bank loan pre closure, banks keep a record of how much emi was pending during the loan pre closure. But here I am making the unpaid emi 0 and paid emi to total emi just to simplify.
        #* Note:- Here my logic is, if you paid the full pending amount, it means you paid all the emis. However, it's a wrong logic.
        self.repayment_amount -= full_amount
        self.amount_paid_till_now += full_amount
        self.emi_status["paid"] = self.emi_status["total"]
        self.emi_status["unpaid"] = 0
        self.loan_tanure_in_months = 0

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
        
