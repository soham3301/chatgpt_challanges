
import json

class Recorder:
    def __init__(self):
        self.name = "Recorder"

    def write_account_data(self, saved_accounts):
        formatted_data = {}
        for account_number, account_object in saved_accounts.items():
            formatted_data[account_number] = {
                "number": account_object.number,
                "balance": account_object.balance,
                "is_locked": account_object.is_locked,
                "attached_customer_id": account_object.attached_customer_id,
            }
            for tran_id, tran_object in account_object.transaction_history.items():
                formatted_data[account_number]["transaction_history"] = {
                    tran_id: {
                        "tran_id": tran_object.tran_id,
                        "amount": tran_object.amount,
                        "from_account_no": tran_object.from_account_no,
                        "to_account_no": tran_object.to_account_no,
                        "transaction_type": tran_object.transaction_type
                    }
                }
        with open("./data/accounts.json", mode="w") as account_file:
            json.dump(formatted_data, account_file, indent=4)

    def write_customer_data(self, saved_customers):
        formatted_data = {}
        for customer_id, customer_object in saved_customers.items():
            formatted_data[customer_id] = {
                "name": customer_object.name,
                "age": customer_object.age,
                "email": customer_object.email,
                "mobile": customer_object.mobile,
                "account_number": customer_object.account_number,
                "cust_id": customer_object.cust_id,
                "password": customer_object.password
            }
        with open("./data/customers.json", mode="w") as customer_file:
            json.dump(formatted_data, customer_file, indent=4)

    def write_email_mobile_set(self, the_set):
        with open("./data/unique_set.txt", mode="w") as unique_file:
            for item in the_set:
                unique_file.write(f"{str(item)}\n")

    def load_account_data(self):
        pass

    def load_customer_data(self):
        try:
            loaded_data = {}
            with open("./data/customers.json") as customer_loaded_file:
                data = json.load(customer_loaded_file)
                for customer_id, customer_details in data.items():
                    loaded_data[customer_id] = {
                        "name": customer_details["name"],
                        "age": customer_details["age"],
                        "email": customer_details["email"],
                        "mobile": customer_details["mobile"],
                        "account_number": customer_details["account_number"],
                        "cust_id": customer_details["cust_id"],
                        "password": customer_details["password"]
                    }
        except json.JSONDecodeError:
            loaded_data = {}
        return loaded_data

    def load_email_mobile_set(self):
        pass