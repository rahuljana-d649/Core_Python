from datetime import datetime

class StoreBase:
    def __init__(self):
        self.customers = []
        self.products = []

    def generate_customer_id(self):
        if not self.customers:
            return "C001"
        last_id = self.customers[-1]["ID"]
        number = int(last_id[1:])+1
        return f"C{number:03d}"
    
    def generate_product_id(self):
        if not self.products:
            return "P001"
        last_id = self.products[-1]["P_ID"]
        number = int(last_id[1:])+1
        return f"P{number:03d}"
    
# ========================== CUSTOMER CLASS ========================== #
    
class Customer(StoreBase):
    def add_customer(self):
        while True:
            name=input("Enter Customer's Name: ")
            if all(ch.isalpha() or ch.isspace() for ch in name):
                break
            else:
                print("Invalid Name!!")
                continue

        while True:
            try:
                age:int=int(input("Enter Customer's Age: "))
                break
            except ValueError:
                print("Invalid Input!!")
                continue

        while True:
            mobile=input("Enter Customer's Mobile: ")
            if mobile.isdigit() and len(mobile)==10:
                break
            else:
                print("Invalid Input!!")
                continue

        while True:
                    email=input("Enter Customer's Email: ")
                    try:
                        if '@' not in email or '.' not in email:
                            raise ValueError("Invalid Email Format!!")
                        break

                    except ValueError as e:
                        print(e)
                        continue

        address=input("Enter Customer's Address: ")
        while True:
            password=input("Enter Password: ")
            confirm_password=input("Re-Enter Password: ")
            if(password==confirm_password):
                final_password=password
                break
            else:
                print("Don't Match... Try Again!")
                continue


        customer_info:dict={
            'ID':self.generate_customer_id(),
            'Name': name,
            'Age': age,
            'Mobile': mobile,
            'Email': email,
            'Address': address,
            'Password': final_password,
            'Products':{},
            'Buy_Return':[]
        }

        self.customers.append(customer_info)
        print(f"Customer added Successfully!..ID: {customer_info['ID']}")


    def display_customers(self):
        if not self.customers:
            print("No Customers to Display!!")
            return
        print("\nCustomer Details: ")
        for idx, customer in enumerate(self.customers, start=1):
            print(f"{idx}. ID: {customer['ID']}, Name: {customer['Name']}, Age: {customer['Age']}, Mobile: {customer['Mobile']}, Email: {customer['Email']}, Address: {customer['Address']}")
                  
    def remove_customer(self):
        if not self.customers:
            print("No Customers to Remove!!")
            return

        c_id=input("Enter Customer ID: ")
        for idx, customer in enumerate(self.customers, start=1):
            if customer['ID']==c_id:
                del self.customers[idx-1]
                print(f"Customer with the ID {c_id} has been successfully Deleted!")
                return  
        print(f"Customer with the ID {c_id} is not Valid!!")

    def update_customer(self):
        if not self.customers:
            print("No Customers to Update!!")
            return

        c_id=input("Enter Customer ID: ")      
        for customer in self.customers:
            if customer['ID']==c_id:
                print("\nLeave for the Same")
                while True:
                    new_name=input("Enter Customer's  New Name: ")
                    if all(ch.isalpha() or ch.isspace() for ch in new_name) or new_name=="":
                        break
                    else:
                        print("Invalid Customer Name!!")
                        continue

                while True:
                    new_age=input("Enter New Age: ")
                    if new_age=='':
                        break
                    try:
                        int(new_age)
                        break

                    except ValueError:
                        print("Invalid Input!!")
                        continue

                while True:
                    new_mobile=input("Enter New Mobile No.: ")
                    if new_mobile=='':
                        break
                    try:
                        new_mobile.isdigit() and len(new_mobile)==10
                        break

                    except ValueError:
                        print("Invalid Input!!")
                        continue
                
                while True:
                    new_email=input("Enter New Email: ")
                    if new_email=='':
                        break
                    try:
                        if '@' not in new_email or '.' not in new_email:
                            raise ValueError("Invalid Email Format!!")
                        break

                    except ValueError as e:
                        print(e)
                        continue


                new_address=input("Enter New Address: ")

                if new_name:
                    customer['Name']=new_name
                if new_age:
                    customer['Age']=int(new_age)
                if new_mobile:
                    customer['Mobile']=new_mobile
                if new_address:
                    customer['Address']=new_address
                if new_email:
                    customer['Email']=new_email
                print(f"Updation Successful for the Customer of ID {c_id}")
                return
        print(f"Customer for the ID {c_id} is not Valid!!")

    def search_customer(self):
        if not self.customers:
            print("No Customers to Search!!")
            return
            
        c_id=input("Enter Customer ID: ")

        for customer in self.customers:
            if customer['ID']==c_id:
                print(f"ID: {customer['ID']}, Name: {customer['Name']}, Age: {customer['Age']}, Mobile: {customer['Mobile']}, Email: {customer['Email']}, Address: {customer['Address']}")
                return
        
        print(f"{c_id} is not Valid!!")


    def buy_return(self):
        if not self.customers:
            print("No Customers to Buying")
            return
        if not self.products:
            print("No Products Here")
            return

        c_id=input("Enter Customer ID: ")
        for customer in self.customers:
            if customer['ID']==c_id:
                for i in customer['Buy_Return']:
                    print(i)
                return
        print("Invalid ID")

# ========================== PRODUCT CLASS ========================== #

    
class Product(StoreBase):
    def add_product(self):
        while True:
            name=input("Enter Product's Name: ")
            if all(ch.isalpha() or ch.isspace() for ch in name) and name!="":
                break
            else:
                print("Invalid Product Name!!")
                continue
        if any(s['Name']==name for s in self.products):
            print(f"Product with the Name {name} is already Exists!!")
            return
            
        
        while True:
            try:
                no_Product:int=int(input("Enter No of Products: "))
                break
            except ValueError:
                print("Invalid Input!!")
                continue

        while True:
            try:
                P_price:int=int(input("Enter Price: "))
                break
            except ValueError:
                print("Invalid Input!!")
                continue
        product_info:dict={
            'P_ID':self.generate_product_id(),
            'Name': name,
            'Count': no_Product,
            'Price': P_price

        }

        self.products.append(product_info)

    def display_products(self):
        if not self.products:
            print("No Products to Show")
            return
        print("\n Product Details: ")
        for idx, product in enumerate(self.products,start=1):
            print(f"{idx}. ID: {product['P_ID']}, Name: {product['Name']}, Available: {product['Count']}, Price: {product['Price']}")

    def remove_product(self):
        if not self.products:
            print("No Products to Remove!!")
            return
        p_id=input("Enter Product ID: ")
        for idx, product in enumerate(self.products, start=1):
            if product['P_ID']==p_id:
                del self.products[idx-1]
                print(f"Product for the ID: {p_id} has been deleted successfully!!")
                return
        print(f"Product with the ID {p_id} is not Valid!!")

    def update_product(self):
        if not self.products:
            print("No Products to Show!!")
            return
        p_id=input("Enter Product ID to Update: ")
        for product in self.products:
            if product['P_ID']==p_id:
                print("---Press Enter to Skip---")
                
                while True:
                    new_name=input("Enter Product's  New Name: ")
                    if all(ch.isalpha() or ch.isspace() for ch in new_name) or new_name=="":
                        break
                    else:
                        print("Invalid Product Name!!")
                        continue


                while True:
                        new_count=input("Enter New Count of the Product: ")
                        if new_count=='':
                            break
                        try:
                            int(new_count)
                            break

                        except ValueError:
                            print("Invalid Input!!")
                            continue

                while True:
                        new_price=input("Enter New Price of the Product: ")
                        if new_price=='':
                            break
                        try:
                            int(new_price)
                            break

                        except ValueError:
                            print("Invalid Input!!")
                            continue

                if new_name:
                    product['Name']=new_name
                if new_count:
                    product['Count']=int(new_count)
                if new_price:
                    product['Price']=int(new_price)
                print(f"Updation Successfull for the ID {p_id}")
                return
        print(f"{p_id} is not Valid!!")
    
    def search_product(self):
        if not self.products:
            print("No Products to Search!!")
            return
        p_id=input("Enter Product ID to Search: ")
        for product in self.products:
            if product['P_ID']==p_id:
                print(f"ID: {product['P_ID']}, Name: {product['Name']}, Available: {product['Count']}, Price: {product['Price']}")
                return
        print(f"{p_id} not Valid!!")

# ========================== BuyReturn CLASS ========================== #

class BuyReturn(Customer, Product):
    def buy_product(self):
        if not self.customers:
            print("No Customers for Buying")
            return
        if not self.products:
            print("No Product for Buying")
            return
        
        c_id=input("Enter Customer ID: ")
        c_password=input("Enter Password: ")
        c_found=False
        for customer in self.customers:
            if customer['ID']==c_id and customer['Password']==c_password:
                c_found=True
                print(f"Logged in Successfully...")
                print(f"Welcome {customer['Name']}!")
                print("\nProduct Details: ")
                for product in self.products:
                    print(f"Name: {product['Name']}, Availiability: {product['Count']}, Price: {product['Price']}")
             
                buy_p_name=input("Enter Product's Name: ")
                found=False
                for product in self.products:
                    
                    if product['Name']==buy_p_name:
                        found=True
                
                        while True:
                            try:
                                qty:int=int(input("Enter Quantity: "))
                                break
                            except ValueError:
                                print("Invalid Input!!")
                                continue
                        
                        if qty>0 and qty<=product['Count']:
                            product['Count']-=qty
                            price:int=product['Price']*qty
                            print(f"Product Name: {buy_p_name}, Quantity: {qty}, Price: {price} ")
                            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            customer['Buy_Return'].append(f"[{timestamp}] (Bought) Product: {buy_p_name}, Qty: {qty}, Price: {price}")
                            print("Order Successfully Placed!!")
                            if buy_p_name in customer['Products']:
                                customer['Products'][buy_p_name]+=qty
                
                            else:
                                customer['Products'][buy_p_name]=qty
                        else:
                            print("Quantity is not Valid!!")
                    
                print("Products of Customer: ")
                for key, value in customer['Products'].items():
                    print(f"Product Name: {key}")
                    print(f"Quantity: {value}")
                    
                if not found:
                    print("Product is not available!!")
        if c_found==False:
            print("Invalid Customer ID or Password!!")
    
    
    def return_product(self):
        if not self.customers:
            print("No Customers for Buying")
            return
        if not self.products:
            print("No Product for Buying")
            return

        c_id=input("Enter Customer ID: ")
        c_password=input("Enter Password: ")
        c_found=False
        for customer in self.customers:
            if customer['ID']==c_id and customer['Password']==c_password:
                c_found=True
                print("Logged in Successfully!")
                print(f"Welcome {customer['Name']}")
                for key, value in customer['Products'].items():
                    print(f"Product Name: {key}")
                    print(f"Quantity: {value}")
                return_p_name=input("Enter Product Name: ")
                if return_p_name not in customer['Products']:
                    print(f"Customer did not buy this {return_p_name}")
                    return
                for product in self.products:
                    if product['Name']==return_p_name:
        
                        while True:
                            try:
                                qty:int=int(input("Enter Quantity: "))
                                break
                            except ValueError:
                                print("Invalid Input!!")
                                continue
                        if qty>0 and qty<=customer['Products'][return_p_name]:
                            product['Count']+=qty
                            customer['Products'][return_p_name]-=qty
                            print("Customer's Product: ")
                            for key, value in customer['Products'].items():
                                print(f"Product Name: {key}")
                                print(f"Quantity: {value}")
                            
                            price:int=product['Price']*qty
                            print(f"Product Name: {return_p_name}, Quantity: {qty}, Price: {price} ")
                            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            customer['Buy_Return'].append(f"[{timestamp}] (Returned) Product: {return_p_name}, Qty: {qty}, Price: {price}")
                            print("Return is in Progress...")
                            print(f"Rs. {price} will be refund very shortly.")
                        else:
                            print("Quantity is not Valid!!")

        if c_found==False:
            print("Invalid Customer ID or Password!!")


class ShoppingSystem(BuyReturn):
    pass



def main():
    shop=ShoppingSystem()
    while True:
        print("\n------------------------Main Menu------------------------")
        print("1. Customer Operations")
        print("2. Product Operations")
        print("3. Buy\Return Product")
        print("4. Exit")

        
        while True:
            try:
                ch:int=int(input("Enter Your Choice: "))
                break
            except ValueError:
                print("Invalid Input!!")
                continue


        if ch==1:
            while True:
                print("\n------------------------Customer Menu------------------------")
                print("1. Add Customer")
                print("2. Display Customers")
                print("3. Remove Customer")
                print("4. Update Customer")
                print("5. Search Customer")
                print("6. Buy / Return History")
                print("7. Main Menu")

                while True:
                    try:
                        choice:int=int(input("Enter Your Choice: "))
                        break
                    except ValueError:
                        print("Invalid Input!!")
                        continue
                if choice==1:
                    shop.add_customer()
                elif choice==2:
                    shop.display_customers()
                elif choice==3:
                    shop.remove_customer()
                elif choice==4:
                    shop.update_customer()
                elif choice==5:
                    shop.search_customer()
                elif choice==6:
                    shop.buy_return()
                elif choice==7:
                    print("Exiting...")
                    break
                else:
                    print(f"{choice} is Invalid!!")

        elif ch==2:
            while True:
                print("\n------------------------Product Menu------------------------\n")
                print("1. Add Product")
                print("2. Display Products")
                print("3. Remove Product")
                print("4. Update Product")
                print("5. Search Product")
                print("6. Main Menu")

            
                while True:
                    try:
                        choice2:int=int(input("Enter Your Choice: "))
                        break
                    except ValueError:
                        print("Invalid Input!!")
                        continue

                if choice2==1:
                    shop.add_product()
                elif choice2==2:
                    shop.display_products()
                elif choice2==3:
                    shop.remove_product()
                elif choice2==4:
                    shop.update_product()
                elif choice2==5:
                    shop.search_product()
                elif choice2==6:
                    print("Going to Main Menu...")
                    break
                    
                else:
                    print("Invalid Choice!!")
        elif  ch==3:
            while True:
                print("\n------------------------Buy Menu------------------------")
                print("1. Buy Product")
                print("2. Return Product")
                print("3. Main Menu")

                choice3:int=int(input("Enter Your Choice: "))
                if choice3==1:
                    shop.buy_product()
                elif choice3==2:
                    shop.return_product()
                elif choice3==3:
                    print("Returning to Main Menu...")
                    break
                else:
                    print("Invalid Choice")
                    continue

        elif ch==4:
            print("Exiting...")
            break

        else:
            print("Invalid Choice!!")
                   
        
if __name__=='__main__':
    main()
