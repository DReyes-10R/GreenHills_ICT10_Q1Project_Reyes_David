#Variables
from pyscript import display, document

restaurant_name = "Café de Reyes" #string
owner_name = "David Miguel A. Reyes" #string
established_year = 1995 #integer
business_hours = "9:00 AM - 11:00 PM" #string
menu_price = {
    "Steak frites": 90.00,
    "Croissant": 150.00,
    "Pasta": 120.00,
    "French Fries": 85.00,
    "Iced Tea/Black Coffee": 75.00,
}

#display basic info
document.getElementById("restaurant").innerText = restaurant_name
document.getElementById("owner").innerText = f"Owner: {owner_name}"
document.getElementById("year").innerText = f"Established: {established_year}"
document.getElementById("hours").innerText = f"Business Hours: {business_hours}"


def process_order(e):
    document.getElementById('orderSummary').innerHTML=""
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    item4 = document.getElementById('menu4')
    item5 = document.getElementById('menu5')

    total = (float(item1.value)*item1.checked +
             float(item2.value)*item2.checked +
             float(item3.value)*item3.checked +
             float(item4.value)*item4.checked +
             float(item5.value)*item5.checked)

    name = document.getElementById('custName').value
    address = document.getElementById('custAddress').value
    contact = document.getElementById('custContact').value

    display(f'Order for: {name}', target='orderSummary')
    display(f'Address: {address}', target='orderSummary')
    display(f'Contact Number: {contact}', target='orderSummary')
    display(f'Total: ₱{total}', target='orderSummary')