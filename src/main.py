from fraud_detection import detect_fraud

if __name__ == "__main__":
    transaction = {"amount": 1500, "description": "Test transaction"}
    is_fraud = detect_fraud(transaction)
    print(f"Transaction is {'fraudulent' if is_fraud else 'legitimate'}")
 
