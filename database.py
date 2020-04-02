import mysql.connector


    
mydb = mysql.connector.connect(
host="127.0.0.1",
user="username",
passwd="",
database="test"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") 
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #add primary key 
#mycursor.execute("CREATE TABLE seller (name VARCHAR(255), phone VARCHAR(255))")
#mycursor.execute("CREATE TABLE item (name VARCHAR(255), price VARCHAR(255))")


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid) #print id


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# sql = "INSERT INTO seller (name, phone) VALUES (%s, %s)"
# val = [
#   ('Pet', '613233233'),
#    ('Alise', '111111111')
#    ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print("seller record inserted, ID:", mycursor.lastrowid)
# 
# sql = "INSERT INTO item (name, price) VALUES (%s, %s)"
# val = [
#   ('Aaa', '11.11'),
#    ('Bbb', '22.22')
#    ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print("item record inserted, ID:", mycursor.lastrowid)

select_customer_query = "SELECT * FROM customers"
select_seller_query = "SELECT * FROM seller"
select_item_query = "SELECT * FROM item"
select_where = "SELECT * FROM customers WHERE address ='Park Lane 38'"

table = ("customers", "seller", "item")

def executeSql(myQuery, rowName):
    mycursor.execute(myQuery)
    myresult = mycursor.fetchall()
    print("\n","Total number of rows in ", rowName, "is: ", mycursor.rowcount)
    return myresult

def print_customer():
   for x in executeSql(select_customer_query,table[0]):
    print("Name = ", x[0])
    print("Address = ", x[1])
    print("ID = ", x[2])
    
def print_seller():
   for x in executeSql(select_seller_query, table[1]):
    print("Name = ", x[0])
    print("Phone = ", x[1])
    
def print_item():
   for x in executeSql(select_seller_query, table[2]):
    print("Name = ", x[0])
    print("Price = ", x[1])
    
def print_customer_where():
   for x in executeSql(select_where,table[0]):
       print(x)
#     print("Name = ", x[0])
#     print("Address = ", x[1])
#     print("ID = ", x[2])

print_customer()
print_seller()
print_item()
print_customer_where()



#for x in executeSql(select_customer_query):       
#       
    
# mycursor.execute(select_seller_query)
# myresult = mycursor.fetchall()
# print("Total number of rows in seller is: ", mycursor.rowcount, "\n")
# for x in myresult:
#     print("Name = ", x[0])
#     print("Phone = ", x[1])
#      
# mycursor.execute(select_item_query)
# myresult = mycursor.fetchall()
# print("Total number of rows in item is: ", mycursor.rowcount, "\n")
# for x in myresult:
#     print("Name = ", x[0])
#     print("Price = ", x[1])
#      
# mycursor.execute(select_where)
# myresult = mycursor.fetchall()
# print("SELECT * FROM customers WHERE address ='Park Lane 38': ", mycursor.rowcount, "\n")
# for x in myresult:
#     print(x)
    
