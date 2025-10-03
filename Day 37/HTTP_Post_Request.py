import requests
from datetime import date
USERNAME = "kiet"
TOKEN = "n1ggag4yw5t"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Coding Graph",
    "unit" : "commit",
    "type" : "int",
    "color" : "shibafu",
}
headers = {
    "X-USER-TOKEN" : TOKEN,
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
now = date.today()
result = now.strftime(r"%Y%m%d")
graph_config = {
    "date" : result,
    "quantity" : "1",
}
# response = requests.post(url=post_endpoint,json=graph_config,headers=headers)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{result}"
new_pixel_data = {
    "quantity" : "2",
}
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{result}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)