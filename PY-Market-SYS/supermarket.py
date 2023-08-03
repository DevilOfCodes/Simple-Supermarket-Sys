import json

def view_products():
  with open("products.json", "r") as f:
    data = json.load(f)

  for index, product in enumerate(data["products"]):
    print("***************************")
    print(f"{index + 1}. {product['name']}")
    print("*******")
    print(f"Price: ${product['price']}")
    print("***************************")

def order():
  products = []
  while True:
    print("******************************************************")
    index = int(input("Enter the number of the product to order: "))
    print("******************************************************")

    with open("products.json", "r") as f:
      data = json.load(f)

    for product in data["products"]:
      if index == product["id"]:
        products.append(product)
        break

    print("Do you want to order another product? (Y/N)")
    print("*******************************************")
    choice = input()
    if choice == "n":
      break

  print("Your order is:")
  print("***************************")
  for product in products:
    print(f"{product['name']}")
    print("*********")
  bill = 0
  for product in products:
    bill += product["price"]

  print("Your bill is: $" + str(bill))

def main():
  while True:
    print("Welcome to the Supermarket!")
    print("***************************")
    print("1. View products")
    print("********")
    print("2. Order")
    print("********")
    print("3. Exit")
    print("***************************")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      view_products()
    elif choice == 2:
      order()
    elif choice == 3:
      break

if __name__ == "__main__":
  main()
