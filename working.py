from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "Phone": "Iphone",
        "Laptop": "HP 360",
        "Network": "MTN"
    },
    2: {"Phone": "Android",
        "Laptop": "MacBook",
        "Network": "Airtel"
        },
    3: {"Phone": "Windows",
        "Laptop": "Dell latitude",
        "Network": "MTN"
        }
}

@app.get("/")
def home():
     response = {
        "id": "call_id",
        "name": "Hassan",
        "phone": "07035044307",
         "Other names": "Tunde",
         "House Number": 53,
         "IsGreatMan": True
    }
     return response

@app.get("/about")
def about():
     return "About page"

@app.get("/get_item/{item_id}")
def get_items(item_id: int):
    return inventory[item_id]

@app.get("/get-by-phone")
def get_item(phone: str):
    for item_id in inventory:
        if inventory[item_id]["phone"] == phone:
          return inventory[item_id]
    return {"Data": "Not found 404"}