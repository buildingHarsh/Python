def apply_discount(price, discount):
    if type(price) not in (int, float):
        return "The price should be a number"

    if type(discount) not in (int, float):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    return price - (discount / 100 * price)

print(apply_discount(100, 20))
# 80.0

print(apply_discount(200, 50))
# 100.0

print(apply_discount(50, 0))
# 50.0

print(apply_discount(50, 100))
# 0.0

print(apply_discount(74.5, 20.0))
# 59.6

print(apply_discount("abc", 20))
# The price should be a number

print(apply_discount(100, "20"))
# The discount should be a number

print(apply_discount(-10, 20))
# The price should be greater than 0

print(apply_discount(100, 150))
# The discount should be between 0 and 100