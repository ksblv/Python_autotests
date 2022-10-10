import requests
data_pet = {
  "id": 13,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "tema",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post(url="https://petstore.swagger.io/v2/pet", json = data_pet)
print(response.text)

data_pet = {
  "id": 13,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "temo4ka",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put(url="https://petstore.swagger.io/v2/pet", json = data_pet)
print(response.text)

response = requests.get(url="https://petstore.swagger.io/v2/pet/13")
print(response.text)