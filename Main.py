import Modules

Modules.db.connect()
'''password = Modules.auth.hash("hello")

stored = Modules.auth.hash("hello")  
print(Modules.auth.verify("hello", stored))        
print(Modules.auth.verify("wrong", stored))
'''