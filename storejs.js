const productsDiv = document.getElementById("products");

fetch("/products")
  .then(response => response.json())
  .then(products => {
    products.forEach(product => {
      const productDiv = document.createElement("div");
      productDiv.innerHTML = `
        <h3>${product.name}</h3>
        <p>$${product.price}</p>
      `;
      productsDiv.appendChild(productDiv);
    });
  });
