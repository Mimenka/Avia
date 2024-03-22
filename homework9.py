avia_raises = [
{'code':100, 'destination': 'Bishkek-Osh', 'start_time': '13:00', 'price':4500},
{'code':101, 'destination': 'Bishkek-Moscow', 'start_time': '13:00', 'price':12500},
{'code':102, 'destination': 'Bishkek-Paris', 'start_time': '13:00', 'price':23500},
{'code':103, 'destination': 'Bishkek-Stambul', 'start_time': '13:00', 'price':11500},
{'code':104, 'destination': 'Bishkek-Turkey', 'start_time': '13:00', 'price':8500},
{'code':105, 'destination': 'Bishkek-Dubai', 'start_time': '13:00', 'price':30500},
]

for avia in avia_raises:
    print('=================================================')
    print(f'Code: {avia["code"]}')
    print(f'Route: {avia["destination"]}')
    print(f'Time departure: {avia["start_time"]}')
    print(f'Cost: {avia["price"]}')
    print('=================================================')

def choice_destination_by_code():
    while True:
        try:
            code = int(input('Enter code air flight: '))
        except Exception:
            print('incorrect format for code')
            continue
        while True:
            code = int(input('Enter code air flight: '))
            result = None   
            for avia in avia_raises:
                if code == avia["code"]:result = avia
            if result == None:
                print('With that code air flight not exist,try again!')
                continue
            break
        return result

avia = choice_destination_by_code()
print(avia)