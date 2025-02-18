document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const productId = urlParams.get('id');

    if (productId) {
        fetch(`/api/products/${productId}`)
            .then(response => response.json())
            .then(product => {
                const productInfo = document.querySelector('.product-info');
                productInfo.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Price: $${product.price}</p>
                    <img src="/static/assets/products/${product.image}" alt="${product.name}" />
                    <p>${product.description}</p>

                `;
            })
            .catch(error => {
                alert('Error: ' + error.message);
            });
    }
});