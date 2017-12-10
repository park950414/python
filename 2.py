def ml_std_weight(height):
      standard_weight = (height - 100)*0.9
      return standard_weight
 
def fml_std_weight(height):
      standard_weight = (height - 100)*0.9 - 2.5
      return standard_weight
        
def debug_bmi(height, weight, gender):
      if gender != 'male' and gender !='female':
            print("input error")
      elif gender == 'male':
            standard_weight = ml_std_weight(height)
      else:
            standard_weight = fml_std_weight(height)        
      if weight <= (standard_weight*0.9):
            print ("You BMI is -1")
      elif  weight <(standard_weight*1.1):
            print ("You BMI is 0")
      elif  weight <(standard_weight*1.2):
            print ("You BMI is 1")
      elif  weight <(standard_weight*1.3):
            print ("You BMI is 2")
      elif  weight <(standard_weight*1.5):
            print ("You BMI is 3")
      else:
            print ("You BMI is 4")
 
if __name__ == "__main__": 
      debug_bmi(160,60,'male')
