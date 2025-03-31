from apps.transactions.fixtures import ProductDataType
from apps.transactions.models import Product

product_data = [
    ProductDataType(name="Dairy Milk", price=100),
    ProductDataType(name="iPhone 15", price=75000),
    ProductDataType(name="Samsung Galaxy S24", price=65000),
    ProductDataType(name="Sony WH-1000XM5 Headphones", price=29000),
    ProductDataType(name="Apple MacBook Air M2", price=110000),
    ProductDataType(name="Nike Air Max Sneakers", price=8500),
    ProductDataType(name="Adidas Ultraboost Shoes", price=12000),
    ProductDataType(name="Samsung 55-inch 4K Smart TV", price=55000),
    ProductDataType(name="Boat Airdopes 441", price=2500),
    ProductDataType(name="Canon EOS R5 Camera", price=320000),
    ProductDataType(name="Rolex Submariner Watch", price=850000),
    ProductDataType(name="LG 1.5 Ton Split AC", price=42000),
    ProductDataType(name="Sony PlayStation 5", price=50000),
    ProductDataType(name="Amazon Echo Dot (5th Gen)", price=4500),
    ProductDataType(name="Logitech MX Master 3 Mouse", price=7500),
    ProductDataType(name="HP Envy x360 Laptop", price=98000),
    ProductDataType(name="Levi's Denim Jacket", price=4500),
    ProductDataType(name="Ray-Ban Aviator Sunglasses", price=12000),
    ProductDataType(name="Woodland Leather Wallet", price=1500),
    ProductDataType(name="Puma Running Shoes", price=6000),
]


def add_product_data():
    for product in product_data:
        (_product, _) = Product.objects.update_or_create(
            name=product.name,
            create_defaults={
                "price": product.price,
            },
        )
