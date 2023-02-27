

class carsharing:

    rental_charge = 0
    insurance_fee = 0
    driving_charge = 0

    def fee(minutes,driving_distance):
        rental_charge = (minutes//10) * 1200
        
        if minutes % 30 == 20: 
            insurance_fee = (minutes // 30 + 1) * 525
        else:
            insurance_fee = (minutes // 30) * 525

        if driving_distance >= 100:
            driving_charge = 100 * 170 + (driving_distance - 100) * 85
        else: 
            driving_charge = driving_distance * 170

        return rental_charge + insurance_fee + driving_charge 
        






print(carsharing.fee(600, 50)) #=> 91000
print(carsharing.fee(600, 110)) #=> 10