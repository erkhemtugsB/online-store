document.addEventListener('DOMContentLoaded', function () {
    const newProductButton = document.querySelector('.header-button button');
    const addProductModal = document.querySelector('.add-product-modal');
    const modalOverlay = document.createElement('div');
    modalOverlay.classList.add('modal-overlay');
    document.body.appendChild(modalOverlay);

    newProductButton.addEventListener('click', function () {
        addProductModal.style.display = 'block';
        modalOverlay.style.display = 'block';
    });

    modalOverlay.addEventListener('click', function () {
        addProductModal.style.display = 'none';
        modalOverlay.style.display = 'none';
    });
});

function openEditModal(button) {
    const productDiv = button.closest('.product');
    const productName = productDiv.querySelector('h3').textContent;
    const productPrice = productDiv.querySelector('p:nth-of-type(1)').textContent.replace('Price: $', '');
    const productDescription = productDiv.querySelector('p:nth-of-type(2)').textContent;

    document.getElementById('edit-product-name').value = productName;
    document.getElementById('edit-product-price').value = productPrice;
    document.getElementById('edit-product-description').value = productDescription;

    document.getElementById('edit-product-modal').style.display = 'block';
    document.getElementById('modal-overlay').style.display = 'block';
}

function closeEditModal() {
    document.getElementById('edit-product-modal').style.display = 'none';
    document.getElementById('modal-overlay').style.display = 'none';
}

document.getElementById('edit-product-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Handle saving the changes here
    closeEditModal();
});