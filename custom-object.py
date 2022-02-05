#Module 3 - Chapter 4: custom-object

class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
        
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100
    
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100 + tipPercent/100)
    
#Create Purchase Object given an amount

purchase = Purchase(100.0)

#Set the tax and tip percentages

taxPercent = 7.5
tipPercent = 20

#Use the object to calculate the tax and tip

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Display the transaction information

print('Tax ', tax)
print('Tip ', tip)
print('Total ', purchase.calculateTotal(taxPercent, tipPercent))

