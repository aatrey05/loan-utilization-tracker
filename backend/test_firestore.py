from firebase_config import db

# Add a test beneficiary
try:
    db.collection('beneficiaries').document('1234567890').set({
        'name': 'Test User',
        'phone': '1234567890',
        'loan_amount': 10000
    })
    print("Test beneficiary added successfully!")

    # Retrieve all beneficiaries
    beneficiaries = db.collection('beneficiaries').stream()
    for doc in beneficiaries:
        print(doc.id, doc.to_dict())

except Exception as e:
    print("Error connecting to Firestore:", e)
