import sqlite3

def queryOrdersByDate(date):
    result = {}
    with sqlite3.connect("ecommerce.db") as connection:
        c = connection.cursor()
        orderLinesDateQuery = c.execute(
            "SELECT orders.ID,\
                    orders.created_at,\
                    orders.vendor_id,\
                    orders.customer_id,\
                    order_lines.quantity,\
                    order_lines.full_price_amount,\
                    order_lines.discounted_amount,\
                    order_lines.discount_rate\
                FROM orders INNER JOIN order_lines ON orders.ID = order_lines.order_id\
                WHERE orders.created_at between '"+date+"' and '"+date+" 23:59:59'").fetchall()

        totalQuantity, discountAmount, averageDiscountRate, averageOrderTotal= 0,0,0,0
        totalAmountCommision, uniqueCustomers , count=0, set(), 0

        # print(orderLinesDateQuery)

        if orderLinesDateQuery:
            for row in orderLinesDateQuery:
                count += 1
                uniqueCustomers.add(row[3])
                totalQuantity += row[4]
                averageOrderTotal += row[5]
                discountAmount += row[6]
                averageDiscountRate += row[7]
            
            result["numberOfItems"] = totalQuantity,
            result["numberOfCustomers"]= len(uniqueCustomers),
            result["totalDiscount"]= discountAmount,
            result["averageDiscountRate"]= averageDiscountRate/count,
            result["averageOrderTotal"]= averageOrderTotal/count
    return result