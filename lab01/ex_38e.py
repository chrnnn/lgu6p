products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 5},
            {"name": "Smartphone", "price": 800, "stock": 10}
        ]
    },
    {
        "category": "Home Appliances",
        "items": [
            {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
            {"name": "Air Conditioner", "price": 500, "stock": 3}
        ]
    }
]

# 결과값이 이렇게 나와야 함
# result = {
#     "Laptop": {"price": 1200, "stock": 5},
#     "Smartphone": {"price": 800, "stock": 10},
#     "Vacuum Cleaner": {"price": 150, "stock": 7},
#     "Air Conditioner": {"price": 500, "stock": 3}
# }

# 코드
def convert_data(products):
    result = {}
    for ctg in products:
        for item in ctg["items"]:
            result[item["name"]] = {
                "price": item["price"], 
                "stock": item["stock"]}
    return result


def convert_data2(products):
    result = {}
    for ctg in products:
        for item in ctg["items"]:
            name = item.pop("name") # name을 반환하고 삭제
            result[name] = item
    return result

print(convert_data(products))
print(convert_data2(products))