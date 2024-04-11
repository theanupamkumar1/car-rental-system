# car.py
class Car:
    def __init__(self, model, price, color, availability_status=True):
        self.details = {
            'model': model,
            'price': price,
            'color': color,
            'availability_status': availability_status
        }