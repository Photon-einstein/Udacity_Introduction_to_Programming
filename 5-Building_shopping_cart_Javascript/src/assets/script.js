const products = [];
let total_paid = 0;

const cherry = {
  image: "./images/cherry.jpg",
  name: "cherry",
  price: Number(2).toFixed(2),
  productId: 1,
  quantity: 0
};

const orange = {
  image: "./images/orange.jpg",
  name: "orange",
  price: Number(1.5).toFixed(2),
  productId: 2,
  quantity: 0
};

const strawberry = {
  image: "./images/strawberry.jpg",
  name: "strawberry",
  price: Number(2.5).toFixed(2),
  productId: 3,
  quantity: 0
};

products.push(cherry);
products.push(orange);
products.push(strawberry);

/* Images provided in /images folder. All images from Unsplash.com
   - cherry.jpg by Mae Mu
   - orange.jpg by Mae Mu
   - strawberry.jpg by Allec Gomes
*/

const cart = [];

/**
* @description Increases the quantity of a product with a given productId,
* if the product is not already in the cart, it is added into the cart
* @method addProductToCart
* @param {number} productId
*/
function addProductToCart(productId) {
  for(let i = 0; i < products.length; ++i) {
    if (products[i].productId == productId) {
      ++products[i].quantity;
      if (cart.indexOf(products[i]) == -1) {
        cart.push(products[i]);
      }
    }
  }
}

/**
* @description Increases the quantity of a product with a given productId
* @method increaseQuantity
* @param {number} productId
*/
function increaseQuantity(productId) {
  for(let i = 0; i < products.length; ++i) {
    if (products[i].productId == productId) {
      ++products[i].quantity;
    }
  }
}

/**
* @description Decrease the quantity of a product with a given productId,
* if the the function decreases the quantity to 0, the product is removed
* from the cart.
* @method decreaseQuantity
* @param {number} productId
*/
function decreaseQuantity(productId) {
  for(let i = 0; i < products.length; ++i) {
    if (products[i].productId == productId) {
      --products[i].quantity;
      if (products[i].quantity == 0) {
        removeProductFromCart(productId);
      }
    }
  }
}

/**
* @description This function gets the correct product based on the productId,
* updates the product quantity to 0 and then removes the product from
* the cart.
* @method removeProductFromCart
* @param {number} productId
*/
function removeProductFromCart(productId) {
  for(let i = 0; i < products.length; ++i) {
    if (products[i].productId == productId) {
      products[i].quantity = 0;
      const index = cart.indexOf(products[i]);
      cart.splice(index, 1);
    }
  }
}

/**
* @description This function gets the total cost of all products in
* the cart
* @method cartTotal
* @returns {number} Sum of the cost of all the items in the cart
*/
function cartTotal() {
  let total = 0;
  for(let i = 0; i < cart.length; ++i) {
    total += cart[i].quantity * cart[i].price;
  }
  return total;
}

/**
* @description This function empties the products from the cart
* @method emptyCart
*/
function emptyCart() {
  cart.splice(0, cart.length);
  total_paid = 0;
}

/**
* @description This function returns the difference between the
* amount given by the customer and the total price of the items in the
* cart
* @method pay
* @param {number} amount
* @returns {number} The difference between the amount given by the customer
* and the total price of the items in the cart
*/
function pay(amount) {
  total_paid +=amount;
  let returnAmount = 0;
  const required = cartTotal();
  returnAmount = total_paid - required;
  if (returnAmount > 0) {
    total_paid = 0;
  }
  return returnAmount;
}

/* Place stand out suggestions here (stand out suggestions can be found at
the bottom of the project rubric.)*/


/* The following is for running unit tests.
   To fully complete this project, it is expected that all tests pass.
   Run the following command in terminal to run tests
   npm run test
*/

module.exports = {
   products,
   cart,
   addProductToCart,
   increaseQuantity,
   decreaseQuantity,
   removeProductFromCart,
   cartTotal,
   pay,
   emptyCart,
   /* Uncomment the following line if completing the currency converter bonus */
   // currency
}
