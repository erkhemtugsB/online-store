document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => {
            const productsContainer = document.querySelector('.active-products');
            productsContainer.innerHTML = ''; // Clear existing content
            data.products.forEach(product => {
                const productElement = document.createElement('div');
                productElement.classList.add('product');
                productElement.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Price: $${product.price}</p>
                    <p>${product.description}</p>
                    <div>
                        <button class="edit" onclick="openEditModal(${product.id})">
                            <i class="ri-edit-line"></i>
                        </button>
                        <button class="delete" onclick="deleteProduct(${product.id})">
                            <i class="ri-delete-bin-line"></i>
                        </button>
                    </div>
                `;
                productsContainer.appendChild(productElement);
            });
        });
});

function openEditModal(productId) {
    // Implement the logic to open the edit modal and populate it with product data
}

function deleteProduct(productId) {

    fetch(`/api/products/delete/${productId}`, {
        method: 'DELETE'
    })
        .then(response => {
            if (!response.ok) throw new Error('Failed to delete product.');
            return response.json();
        })
        .then(data => {
            // Refresh product list dynamically
            location.reload();
        })
        .catch(error => {
            alert('Error: ' + error.message);
            console.error('Error:', error);
        });
}