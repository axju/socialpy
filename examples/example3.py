from socialpy import Gateway
import json

def plot(LastJson):
    try:
        print(json.dumps(LastJson, indent=4, sort_keys=True))
    except Exception as e:
        pass

gateway = Gateway()
#gateway.load_from_file('.env')

gateway['instagram'].setup(user='...', pw='...')

id = gateway['instagram'].api.username_id
print(id)

print(gateway['instagram'].api.getUserFeed(id))
plot(gateway['instagram'].api.LastJson)

print(gateway['instagram'].api.getUsernameInfo(id))
plot(gateway['instagram'].api.LastJson)

print(gateway['instagram'].api.getSelfUsernameInfo())
print(json.dumps(gateway['instagram'].api.LastJson, indent=4, sort_keys=True))
