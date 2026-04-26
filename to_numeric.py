X['TotalCharges'] = pd.to_numeric(X['TotalCharges'], errors='coerce')

#👉 Problem:
#TotalCharges is stored as text, not number

#What it does:
#Converts text → number
#If conversion fails → puts NaN (missing value)

#(errors='coerce' = “force convert, else make it empty”)
