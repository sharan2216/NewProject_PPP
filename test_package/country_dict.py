
points_table = {
    'India':8,
    'Pakistan':6,
    'South Africa':5,
    'Bangladesh':4,
    'netherland':2,
    'Bermuda':2
    }
while True:
    try:
        name = input("Enter the country name:")
        points=points_table[name]
        print(f"{name}has got {points} points")
    except:
        print("No such country")
    else:
        break
