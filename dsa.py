import js2py

with open("")
f = js2py.eval_js('temp = [{"accountCreationIp" : {"accountId" : "2977649117","userCreationIp" : "105.237.85.167"}}]')

print(f[0]['accountCreationIp'])