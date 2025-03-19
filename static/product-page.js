document.addEventListener('DOMContentLoaded', function () {
    // Fetch product information and display it
    const productId = 1; // Replace with the actual product ID you want to fetch
    fetch(`/api/products/${productId}`)
        .then(response => response.json())
        .then(product => {
            document.querySelector('.product-info').innerHTML = `
                <h3>${product.name}</h3>
                <p>Price: $${product.price}</p>
                <p>${product.description}</p>
                <img src="../static/assets/products/${product.image}" alt="Product Image">
            `;
            // Set the product ID in the hidden input field
            document.getElementById('product-id').value = product.id;
        });

    // Add event listener to the order button
    document.getElementById('order-button').addEventListener('click', function () {
        const productId = document.getElementById('product-id').value;
        console.log(`Ordering product with ID: ${productId}`);
    });
});