"""https://www.codewars.com/kata/57a429e253ba3381850000fb"""
"""Write function bmi that calculates body mass index (bmi = weight / height2)."""

def bmi (weight, height): 
    bmi= weight/ height**2
    if bmi <= 18.5:
      return("underwright")
    elif bmi <=  25.0:
      return("normal")
    elif bmi <= 30.0:
      return("overweight")
    elif bmi > 30:
      return("obese")
print(bmi(50,2))