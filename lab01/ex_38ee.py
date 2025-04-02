orders = [
    {
        "country": "USA",
        "customers": [
            {
                "customer_id": "C001",
                "orders": [
                    {"product": "Laptop", "quantity": 1, "unit_price": 1200},
                    {"product": "Mouse", "quantity": 2, "unit_price": 25}
                ]
            },
            {
                "customer_id": "C002",
                "orders": [
                    {"product": "Smartphone", "quantity": 1, "unit_price": 800}
                ]
            }
        ]
    },
    {
        "country": "Canada",
        "customers": [
            {
                "customer_id": "C003",
                "orders": [
                    {"product": "Laptop", "quantity": 2, "unit_price": 1150},
                    {"product": "Keyboard", "quantity": 1, "unit_price": 100}
                ]
            }
        ]
    }
]


result = {
    "C001": {
        "country": "USA",
        "products": ["Laptop", "Mouse"],
        "total_amount": 1250  # (1 x 1200) + (2 x 25)
    },
    "C002": {
        "country": "USA",
        "products": ["Smartphone"],
        "total_amount": 800
    },
    "C003": {
        "country": "Canada",
        "products": ["Laptop", "Keyboard"],
        "total_amount": 2400  # (2 x 1150) + (1 x 100)
    }
}

def order_by_customers(orders):
    result = {}

    for ctr in orders:  # 나라별(ctr = 딕셔너리)
        country = ctr['country']
        for customer in ctr["customers"]: # 고객 정보(customer = 딕셔너리)
            id = customer["customer_id"]

            prods = []
            total = 0
            
            for order in customer['orders']:  # 주문 정보
                total += order["unit_price"] * order["quantity"]
                prods.append(order['product'])
            # 최근엔 이렇게 함...
            # procudcts = [ order['product'] for order in customer['orders'] ]
            # total = sum( [ 
            #               order["unit_price"] * order["quantity"] for order in customer['orders'] 
            #             ] )       
            result[id] = {'country': country,
                          'products': prods,
                          'total_amount': total}
    return result


print(order_by_customers(orders))