import json, random
from datetime import datetime

deals = [
    {"title": "Amazon Bluetooth Speaker", "discount": "25%", "link": "#", "platform": "Amazon"},
    {"title": "Flipkart Smartwatch", "discount": "40%", "link": "#", "platform": "Flipkart"},
    {"title": "Myntra Sneakers", "discount": "30%", "link": "#", "platform": "Myntra"},
    {"title": "Ajio Jeans", "discount": "50%", "link": "#", "platform": "Ajio"}
]

# Save 3 random deals
with open("data/deals.json", "w") as f:
    json.dump(random.sample(deals, 3), f, indent=2)