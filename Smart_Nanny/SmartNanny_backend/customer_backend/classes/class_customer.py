# declaring class customer and what attributes it takes in
class Customer:
    def __init__(self, name, phone_no, address, subscription_start_date, days_in_a_week, days_of_the_week, nanny_id,
                 discount_id, payment_amount):
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.subscription_start_date = subscription_start_date
        self.days_in_a_week = days_in_a_week
        self.days_of_the_week = days_of_the_week
        self.nanny_id = nanny_id
        self.discount_id = discount_id
        self.payment_amount = payment_amount

