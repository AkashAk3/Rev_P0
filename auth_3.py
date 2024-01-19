from connection import Connection
from admin import *
from users import *
ad=admin_class()
us=user_class()
con=Connection()
class UserAuthentication:    
    try:
        
        def register(self, username, password,role='user'):
    
            conn=con.connec()
            cursor=conn.cursor(dictionary=True)
            query="insert into signups(username,password,role) values(%s,%s,%s)"
            data=(username,password,role)
            cursor.execute(query,data)
            print("\n--------Registration successful. You can now log in.--------")
            conn.commit()
            # cursor.close()
            # conn.close()

        def login(self, username, password):
            conn=con.connec()
            cursor=conn.cursor(dictionary=True)
            query="select * from signups where username=%s and password=%s"
            data=(username,password)
            cursor.execute(query,data)
            result = cursor.fetchone()
        
            if result:
                role_query = "SELECT role FROM signups WHERE username=%s"
                cursor.execute(role_query, (username,))

                role_result = cursor.fetchone()
                
                conn.commit()
                if role_result['role'] == "admin":
                    print("\n---------You've successfully Logged in as ADMIN---------\n")
                    ad.admin()
                else:
                    print("\n--------You've successfully Logged in as USER--------\n")
                    us.user()
                    
                    
                
                
                    
                
            else:
                print("Either username or Incorrect password. Please try again.")
           
            

            return False,None
    except Exception as e:
        print(e)
    