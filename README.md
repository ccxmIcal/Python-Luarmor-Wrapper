# **Luarmor Api Wrapper**
### _Made by sufi#1337_

---
# **Usage**

* Importing and initializing
```py
import wrapper.wrapper as luaArmor
luaArmor = luaArmor.Luarmor() # --> Init(must have)
```
* Creating an entry (Whitelisting someone)
```py
luaArmor.create_entry() # --> Returns the created key
data = {'identifier': 'whatever', 'auth_expire': 1, 'note': 'gay?', 'discord_id': '123456789'}
# All of these are optional you can use whatever.
luaArmor.create_entry(data)
# This will create the entry with whatever data you add
```
* Getting an entry (getting a user)
```py
luaArmor.get_entry('123456789') # This will return a json object with the data of 123456789 # Only discord ID is permitted
# Getting all the users
luaArmor.get_entry() # It returns all of the users. You need to format the data yourself.
```
* Changing an entry (Modifying a user)
```py
data = {'user_key': 'Must have', 'identifier': 'Optional', 'auth_expire': 'Optional', 'note': 'Optional', 'discord_id': 'Optional'}
# This will modify the values that you provide of "user_key". If a value is missing it will just be skipped.
luaArmor.set_entry(data)
```
* Deleting an entry
```py
luaArmor.del_entry('user_key') # This will delete the entry | whitelist of the user with the specified key.
```
* Reseting a HWID
```py
luaArmor.reset_hwid('user_key') # This will reset the hwid of the user with the specified key.
```
* Linking a discord
```py
luaArmor.link_discord('user_key', 'discord_id') # This will change the discord id linked to the key with the "user_key"
```

* Getting the key stats
```py
luaArmor.get_key_stats() # Returns a json object with your key stats
```

* Getting the key details
```py
luaArmor.get_key_details() # Returns a json object with your key details.
```
