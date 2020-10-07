names = ['diMA', 'ANdrEY', ' george', 'aRTem', 'V']
print({name[0].upper() + name[1:].lower() for name in names if len(name) > 1})
