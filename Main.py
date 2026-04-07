import Modules
from cli import main

if __name__ == "__main__":
    Modules.db.connect('accounts.db')
    main()



'''password = Modules.auth.hash("hello")

stored = Modules.auth.hash("hello")  
print(Modules.auth.verify("hello", stored))        
print(Modules.auth.verify("wrong", stored))
'''