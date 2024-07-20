from src.fraud_detection import detect_fraud

def test_detect_fraud():
    transaction = {"amount": 1500, "description": "Test transaction"}
    assert detect_fraud(transaction) == True

    transaction = {"amount": 500, "description": "Test transaction"}
    assert detect_fraud(transaction) == False

