# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package name in kilograms: "))
rate = float(input("Enter the shipping rate in kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"shipping_cost: {shipping_cost} USD")
