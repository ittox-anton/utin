def generate_payments(payment_date, payment_amount, payment_method):
    payments = []
    for i in range(12):
        payment = {
            'date': payment_date + timedelta(days=i),
            'amount': payment_amount,
            'method': payment_method
        }
        payments.append(payment)
    return payments
