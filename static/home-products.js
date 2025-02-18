document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => {
            const productsContainer = document.querySelector('.product__grid');
            productsContainer.innerHTML = ''; // Clear existing content
            data.products.forEach(product => {
                const productElement = document.createElement('div');
                productElement.classList.add('product__card');
                productElement.innerHTML = `
                    <h4>${product.name}</h4>
                    <p>$${product.price}</p>
                    <a href="/product?id=${product.id}"><img src="/static/assets/products/${product.image}" alt="${product.name}" /></a>
                `;
                productsContainer.appendChild(productElement);
            });
        });
});