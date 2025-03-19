document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/orders')
        .then(response => response.json())
        .then(data => {
            const ordersContainer = document.querySelector('.active-orders');
            ordersContainer.innerHTML = ''; // Clear existing content
            data.orders.forEach(order => {
                fetch(`/api/products/${order.product_id}`)
                    .then(response => response.json())
                    .then(product => {
                        const orderElement = document.createElement('div');
                        orderElement.classList.add('order-card');
                        orderElement.innerHTML = `
                            <h3>Product Name: ${product.name}</h3>
                            <p>Buyer: ${order.customer_name}</p>
                            <p>Quantity: ${order.quantity}</p>
                            <p>Total: $${order.quantity * product.price}</p>
                            <p>Phone: ${order.customer_phone}</p>
                            <p>Address: ${order.customer_address}</p>
                            <img src="../static/assets/products/${product.image}" alt="Product Image">
                            <div>
                                <button class="mark-delivered" onclick="markAsDelivered(${order.id})">
                                    <i class="ri-check-line"></i> Mark as Delivered
                                </button>
                                <button class="delete" onclick="deleteOrder(${order.id})">
                                    <i class="ri-delete-bin-line"></i> Delete
                                </button>
                            </div>
                        `;
                        ordersContainer.appendChild(orderElement);
                    });
            });
        });
});

function markAsDelivered(orderId) {
    // Implement the logic to mark the order as delivered
}

function deleteOrder(orderId) {
    fetch(`/api/orders/delete/${orderId}`, {
        method: 'DELETE'
    })
        .then(response => {
            if (!response.ok) throw new Error('Failed to delete order.');
            return response.json();
        })
        .then(data => {
            // Refresh order list dynamically
            location.reload();
        })
        .catch(error => {
            alert('Error: ' + error.message);
            console.error('Error:', error);
        });
}