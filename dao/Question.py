#1. Write a program that checks whether a given order is delivered or not based on its status (e.g.,
#"Processing," "Delivered," "Cancelled"). Use if-else statements for this.
order_status = input("Enter the order status: ")

if order_status == "Delivered":
  print("The order has been delivered.")
elif order_status == "Processing":
  print("The order is still being processed.")
elif order_status == "Cancelled":
  print("The order has been cancelled.")
else:
  print("Invalid order status.")

#2.Implement a switch-case statement to categorize parcels based on their weight into "Light,"
#"Medium," or "Heavy."
weight = float(input("Enter the weight of the parcel (kg): "))

if weight <= 0.5:
    category = "Light"
elif weight <= 2:
    category = "Medium"
else:
    category = "Heavy"

print(f"The parcel is categorized as {category}.")


#3.Implement User Authentication 1. Create a login system for employees and customers using Java
#control flow statements.
user_credentials = {
    'employee1': 'employee_password1',
    'customer1': 'customer_password1'
}

def login():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in user_credentials and user_credentials[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1

    if attempts == max_attempts:
        print("Too many login attempts. Please try again later.")

login()


#4.Implement Courier Assignment Logic 1. Develop a mechanism to assign couriers to shipments based
#on predefined criteria (e.g., proximity, load capacity) using loops.

couriers = [
    {"name": "Emma Davis", "capacity": 5.0},
    {"name": "William Brown", "capacity": 4.0}]


shipments = [
    {"sender": "John Doe", "receiver": "Jane Smith", "weight": 2.5},
    {"sender": "Alice Johnson", "receiver": "Bob Anderson", "weight": 1.8}]

for shipment in shipments:
    assigned = False
    for courier in couriers:
        if courier["capacity"] >= shipment["weight"]:
            print(f"Courier '{courier['name']}' assigned to deliver from {shipment['sender']} to {shipment['receiver']}")
            courier["capacity"] -= shipment["weight"]
            assigned = True
            break

    if not assigned:
        print(f"No available courier for the shipment from {shipment['sender']} to {shipment['receiver']}")


#5.rite a Python program that uses a for loop to display all the orders for a specific customer.
orders = [
    {"order_id": 1, "customer_name": "John Doe", "product": "Product A"},
    {"order_id": 2, "customer_name": "Jane Smith", "product": "Product B"},
    {"order_id": 3, "customer_name": "John Doe", "product": "Product C"},
    {"order_id": 4, "customer_name": "Alice Johnson", "product": "Product D"},
    {"order_id": 5, "customer_name": "John Doe", "product": "Product E"}]

customer_to_display = "John Doe"
print(f"Orders for customer '{customer_to_display}':")
for order in orders:
    if order["customer_name"] == customer_to_display:
        print(f"Order ID: {order['order_id']}, Product: {order['product']}")


#6.Implement a while loop to track the real-time location of a courier until it reaches its destination.
import time
courier_location = "Main Office"
destination = "Branch Office"
while courier_location != destination:
    print(f"Courier is currently at: {courier_location}")
    courier_location = destination
print(f"The courier has reached the destination: {destination}")


#7.Create an array to store the tracking history of a parcel, where each entry represents a location update.
tracking_history = [
    {
        'TrackingNumber': 'TRK123',
        'Status': 'In Transit',
        'Location': 'Main Office',
        'UpdateDate': '2023-12-15'
    },
    {
        'TrackingNumber': 'TRK123',
        'Status': 'In Transit',
        'Location': 'Branch Office',
        'UpdateDate': '2023-12-16'
    },
    {
        'TrackingNumber': 'TRK123',
        'Status': 'Delivered',
        'Location': 'Local Store',
        'UpdateDate': '2023-12-17'
    }]
def add_tracking_update(tracking_number, status, location, update_date):
    tracking_history.append({
        'TrackingNumber': tracking_number,
        'Status': status,
        'Location': location,
        'UpdateDate': update_date
    })
add_tracking_update('TRK654', 'In Transit', 'Warehouse', '2023-12-10')
print("Tracking History:")
for update in tracking_history:
    print(f"Tracking Number: {update['TrackingNumber']}, Status: {update['Status']}, Location: {update['Location']}, Update Date: {update['UpdateDate']}")


#8.Implement a method to find the nearest available courier for a new order using an array of couriers.
import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
couriers = [
    {"CourierID": 1, "Location": (123, 456), "Status": "Available"},
    {"CourierID": 2, "Location": (789, 101), "Status": "Available"},
    {"CourierID": 3, "Location": (234, 567), "Status": "Busy"}]
new_order_location = (111, 222)
nearest_courier = None
min_distance = float('inf')

for courier in couriers:
    if courier["Status"] == "Available":
        courier_location = courier["Location"]
        distance = calculate_distance(new_order_location[0], new_order_location[1],
                                      courier_location[0], courier_location[1])
        if distance < min_distance:
            min_distance = distance
            nearest_courier = courier

if nearest_courier:
    print(f"The nearest available courier is CourierID: {nearest_courier['CourierID']} "
          f"at a distance of {min_distance} units from the pickup location.")
else:
    print("No available couriers found.")



#9.Create a program that allows users to input a parcel tracking number.Store the
#tracking number and Status in 2d String Array. Initialize the array with values. Then, simulate the
#tracking process by displaying messages like "Parcel in transit," "Parcel out for delivery," or "Parcel
#delivered" based on the tracking number's status.

class CourierTrackingSystem:
    def _init_(self):
        self.tracking_data = [
            ['TRK123', 'In Transit'],
            ['TRK456', 'Delivered'],
            ['TRK789', 'Pending'],
            ['TRK987', 'In Transit'],
            ['TRK654', 'Delivered']
        ]

    def track_parcel(self, tracking_number):
        for data in self.tracking_data:
            if data[0] == tracking_number:
                return data[1]
        return None

    def display_status(self, status):
        if status == 'In Transit':
            print("Parcel is in transit.")
        elif status == 'Pending':
            print("Parcel is pending.")
        elif status == 'Delivered':
            print("Parcel has been delivered.")
        else:
            print("Invalid tracking number.")

    def run(self):
        while True:
            tracking_number = input("Enter tracking number (or 'quit' to exit): ")
            if tracking_number.lower() == 'quit':
                break

            status = self.track_parcel(tracking_number)
            if status is not None:
                self.display_status(status)
            else:
                print("Tracking number not found.")

if _name_ == "_main_":
    tracking_system = CourierTrackingSystem()
    tracking_system.run()


#10.Write a function which takes 2 parameters, data-denotes the data and
#detail-denotes if it is name addtress or phone number.Validate customer information based on
#following critirea. Ensure that names contain only letters and are properly capitalized, addresses do not
#contain special characters, and phone numbers follow a specific format

import re

def validate_customer_info(data, detail):
    if detail == 'name':
        if data.isalpha() and data.istitle():
            return True
        else:
            return False
    elif detail == 'address':
        # Validate address: doesn't contain special characters
        if bool(re.match("^[A-Za-z0-9 ]*$", data)):
            return True
        else:
            return False
    elif detail == 'phone number':
        if bool(re.match("^\d{3}-\d{3}-\d{4}$", data)):
            return True
        else:
            return False
    else:
        return False  # Return False for invalid 'detail' parameter

# Example usage:
name_validation = validate_customer_info('John Doe', 'name')
print(f'Is Name Valid? {name_validation}')

address_validation = validate_customer_info('123 Main St', 'address')
print(f'Is Address Valid? {address_validation}')

phone_validation = validate_customer_info('123-456-7890', 'phone number')
print(f'Is Phone Number Valid? {phone_validation}')


#11. Develop a function that takes an address as input (street, city, state, zip code) and formats it correctly, including capitalizing the first letter of each word and properly formatting the zip code.
def format_address(street, city, state, zip_code):
    formatted_street = ' '.join(word.capitalize() for word in street.split())
    formatted_city = city.capitalize()
    formatted_state = state.upper()

    formatted_zip = str(zip_code)
    if len(formatted_zip) > 5:
        formatted_zip = formatted_zip[:5] + '-' + formatted_zip[5:]

    formatted_address = f"{formatted_street}, {formatted_city}, {formatted_state} {formatted_zip}"
    return formatted_address

street_address = "123 example street"
city_name = "city"
state_name = "state"
zip_code = "123456789"

formatted_result = format_address(street_address, city_name, state_name, zip_code)
print(formatted_result)



#12.Create a program that generates an order confirmation email. The email
#should include details such as the customer's name, order number, delivery address, and expected
#delivery date.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Email configuration
email_sender = 'your_email@gmail.com'
email_password = 'your_email_password'
email_recipient = 'recipient_email@example.com'
def send_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date):
    # Email content
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = 'Order Confirmation'

    # Email body
    email_body = f"Dear {customer_name},\n\n"\
                 f"Your order ({order_number}) has been confirmed.\n"\
                 f"Delivery Address: {delivery_address}\n"\
                 f"Expected Delivery Date: {expected_delivery_date}\n\n"\
                 "Thank you for choosing our services!\n"\
                 "Best regards,\n"\
                 "Courier Management System"

    msg.attach(MIMEText(email_body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_recipient, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

customer_name = 'John Doe'
order_number = 'TRK123'
delivery_address = '123 Main St, City, Country'
expected_delivery_date = '2023-12-15'  # Example delivery date

expected_delivery_date = datetime.strptime(expected_delivery_date, '%Y-%m-%d').strftime('%B %d, %Y')

send_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date)

#13. Develop a function that calculates the shipping cost based on the distance
#between two locations and the weight of the parcel. You can use string inputs for the source and
#destination addresses.

def calculate_shipping_cost(source_address, destination_address, weight):
    distances = {
        ('123 Main St, City, Country', '456 Oak Ave, Town, Country'): 30,
        ('789 Elm St, Village, Country', '101 Pine St, City, Country'): 50,
        ('222 Cedar Ave, Town, Country', '123 Main St, City, Country'): 20,
        ('456 Oak Ave, Town, Country', '789 Elm St, Village, Country'): 40,
        ('101 Pine St, City, Country', '222 Cedar Ave, Town, Country'): 25
    }

    try:
        if (source_address, destination_address) in distances:
            distance = distances[(source_address, destination_address)]
        else:
            return "Distance not available for the given addresses."

        cost_per_mile = 0.5
        shipping_cost = distance * cost_per_mile + (weight * 2)

        return shipping_cost

    except Exception as e:
        return f"An error occurred: {str(e)}"

source_address = '123 Main St, City, Country'
destination_address = '456 Oak Ave, Town, Country'
parcel_weight = 5.2

estimated_cost = calculate_shipping_cost(source_address, destination_address, parcel_weight)

if isinstance(estimated_cost, (int, float)):
    print(f"The estimated shipping cost is: ${estimated_cost:.2f}")
else:
    print(estimated_cost)



#14. Create a function that generates secure passwords for courier system accounts. Ensure the passwords contain a mix of uppercase letters, lowercase letters, numbers, and special characters.

import random
import string

def generate_secure_password(length=12):
    # Define characters for each category
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation
    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters

    password = random.choice(uppercase_letters)
    password += random.choice(lowercase_letters)
    password += random.choice(numbers)
    password += random.choice(special_characters)

    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

generated_password = generate_secure_password()
print("Generated Password:", generated_password)



#15.Implement a function that finds similar addresses in the system. This can be useful for identifying duplicate customer entries or optimizing delivery routes. Use string functions to implement this.
def similarity_ratio(s1, s2):
    def clean_and_split(address):
        return set(address.lower().replace(',', '').replace('.', '').split())

    words1 = clean_and_split(s1)
    words2 = clean_and_split(s2)

    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))

    similarity = intersection / union if union != 0 else 0
    return similarity

def find_similar_addresses():
    users_addresses = [
        '123 Main St, City, Country',
        '456 Oak Ave, Town, Country'
    ]

    courier_addresses = [
        '123 Main St, City, Country',
        '456 Oak Ave, Town, Country'
    ]

    receiver_addresses = [
        '123 Main St, City, Country',
        '456 Oak Ave, Town, Country'
    ]

    all_addresses = users_addresses + courier_addresses + receiver_addresses

    similar_addresses = {}

    for i, addr1 in enumerate(all_addresses):
        for j, addr2 in enumerate(all_addresses):
            if i != j and addr1 != addr2:
                ratio = similarity_ratio(addr1, addr2)
                if ratio > 0.6:
                    if addr1 in similar_addresses:
                        similar_addresses[addr1].append(addr2)
                    else:
                        similar_addresses[addr1] = [addr2]

    return similar_addresses

similar_addrs = find_similar_addresses()
for addr, similar in similar_addrs.items():
    print(f"Similar addresses to '{addr}': {similar}")