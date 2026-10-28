from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
bills = []

PAGE = """
<!doctype html>
<html>
<head><title>Shopping Bill Calculator v2</title></head>
<body>
<h1>Shopping Bill Calculator (v2 with Discounts)</h1>
<form method="post" action="/calculate">
<input type="number" step="0.01" name="price" placeholder="Item Price" required>
<input type="number" name="quantity" placeholder="Quantity" required>
<input type="number" step="0.1" name="discount" placeholder="Discount % (0-100)" required>
<button type="submit">Calculate Bill</button>
</form>
<h2>Recent Calculations</h2>
<ul>
{% for bill in bills %}
<li>Price: ${{ bill.price }} x Qty: {{ bill.quantity }} (Disc: {{ bill.discount }}%) = <strong>Final Total: ${{ bill.total }}</strong></li>
{% else %}
<li>No calculations performed yet.</li>
{% endfor %}
</ul>
</body>
</html>
"""

def calculate_total(price, quantity, discount_percentage=0):
    if price < 0 or quantity < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid pricing or discount percentage boundaries.")
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percentage / 100)
    return round(subtotal - discount_amount, 2)

@app.get("/")
def home():
    return render_template_string(PAGE, bills=bills)

@app.post("/calculate")
def handle_calculate():
    try:
        price = float(request.form.get("price", 0))
        quantity = int(request.form.get("quantity", 0))
        discount = float(request.form.get("discount", 0))
        total = calculate_total(price, quantity, discount)
        bills.append({"price": price, "quantity": quantity, "discount": discount, "total": total})
    except ValueError:
        pass
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

