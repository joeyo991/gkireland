# **GK Ireland**

![Home Page](/readme-assets/gkireland-home.png)

## **About**

The live site can be accessed by this [link](https://gk-ireland.herokuapp.com/).

GK Ireland is an online store that sells goalkeeper gloves and accessories.

## **User Experience Design**

### **Strategy**

Developed to give goalkeepers all they need in one place.

### **Target Audience**

Soccer players, particularly goalkeepers.

## **User Stories**

### **Customer/Site User Goals**
- As a shopper I can view a list of products so that I can select something to purchase
- As a shopper I can view individual product details so that I can learn more about each product
- As a shopper I can view the total of my purchases so that I can avoid spending too much
- As a Site User I can easily register for an account so that I can have a personal account and be able to view my profile
- As a Site User I can easily login or out so that I can access my personal account information
- As a Site User I can easily recover my password in case I forget it so that I can recover access to my account
- As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful
- As a Site User I can have a personalized profile so that I can view my order history/confirmations and save my payment information
- As a Shopper I can sort the list of available products so that I can easily identify the best priced, best rated and categorically sorted products
- As a Shopper I can easily select the size and quantity of the products I am purchasing so that I don't accidentally select the wrong product quantity or size
- As a shopper I can view items in my bag so that I can identify the total cost of my purchase and the items I will receive
- As a shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase
- As a shopper I can easily enter my payment information so that checkout quickly with no hassle
- As a shopper I can feel my personal and payment information is secure so that I can confidently provide the needed information to make a purchase
- As a shopper I can view a summary of my order so that I can verify my order was correct
- As a shopper I can receive an email confirmation after checking out so that I can keep the confirmation of my purchases for my records

### **Store Owner/Admin Goals**
- As a Store Owner I can add products so that I can update my store catalogue
- As a Store Owner I can edit/update products so that I can alter prices, descriptions, images and other information
- As a Store Owner I can delete products so that I can remove items that are no longer for sale

## **Technologies Used**
### **Languages:**
- [Python](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
- [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

### **Frameworks and Libraries:**
- [Django](https://www.djangoproject.com/): python framework used to create all the backend logic of the website.
- [Bootstrap](https://getbootstrap.com/): HTML and CSS templates used throughout the site.

### **Databases**
- [SQLite](https://www.sqlite.org/): was used as a database during the development stage of the website.
- [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

### **Other tools**
- [Git](https://git-scm.com/): the version control system used to manage the code.
- [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
- [AWS](https://aws.amazon.com/): Used to host the applications static and media files.
- [Psycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
- [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
- [GitHub](https://github.com/): used to host the website's source code.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
- [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
- [PEP8](https://pep8.org/): was used to validate Python code for the website.
- [Stripe](https://stripe.com/): Used to process card payments.

## **Features**

### **Home Page**

The home page is designed to draw users in with colours that pop and also with a picture of one of Ireland's best goalkeepers, Gavin Bazunu.

![Home Page](/readme-assets/gkireland-home.png)

### **Navbar**

![Navbar](/readme-assets/navbar.png)

The navbar remains at the top of the site at all times, giving the users easy access to it.
It contains the logo, which acts as a link to the home page.

![Logo Link](/readme-assets/logo-link.png)

When one of the the options on the navbar is clicked, a dropdown menu appears revealing my choices for the user to choose from.

![All Products dropdown](/readme-assets/all-products.png)

![Gloves dropdown](/readme-assets/gloves.png)

![Clothing dropdown](/readme-assets/clothing.png)

If a user is not signed in and they click the account icon, they are given the option to register for an account, or sign in if they have one already.

![Account dropdown (logged out)](/readme-assets/account.png)

If the user is signed in, they can view their profile or log out.

![Account dropdown (logged in)](/readme-assets/account_in.png)

If a superuser/admin clicks the account icon, they have the option to enter product management.

![Account (superuser)](/readme-assets/account_super.png)

The shopping basket icon directs the user to their basket. If there is items in their basket, the price will be visible.

![Navbar basket](/readme-assets/nav-basket.png)

The navbar also contains a search bar so that the user can search for a specific item.

![Searchbar](/readme-assets/searchbar.png)

On mobile screens, the navbar is compressed down into a dropdown menu.

![Mobile navbar](/readme-assets/mobile-nav.png)

![Mobile dropdown](/readme-assets/mobile-dropdown.png)

### **Products Page**

The products page displays all products to the user. They are displayed in a grid and each item shows their name, price, category and image.

![Products Page](/readme-assets/products-page.png)

It also contains a dropdown menu which allows the user to sorth the products in whatever way they like.

![Products sorting dropdown](/readme-assets/products-sort.png)

### **Product Detail**

The product detail page allows the user to get a better look at an individual item.
The user can read the description, pick a size and the amount of the product they want to add to their basket.

![Product detail](/readme-assets/product-detail.png)

For superusers/admins, they also have the option to delete or edit the item from this page.

![Product detail admin](/readme-assets/product-detail-admin.png)

### **Shopping Basket**

 The shopping basket allows users to store items until they are ready to complete their order. It also gives them a chance to review their order before completing it. Clicking the Secure checkout button will bring the user to the checkout form.

 ![Basket](/readme-assets/basket.png)

 ### **Checkout Form**

 This is where the user enters their payment and shipping details in order to complete the transaction. They also get one last look at their order summary.

 ![Checkout form](/readme-assets/checkout-form.png)

The checkout form uses Stripe to take debit card transactions.

![Stripe](/readme-assets/stripe.png)

### **Order Confirmation**

When the user completes an order, they are redirected to the order confirmation page where they are given a summary of their order and a notification that an email was sent containing a summary also.

![Order confirmation](/readme-assets/order-confirmation.png)

### **User Profile**

If the customer chooses to, they can create an account which allows them to save their default delivery information. The user can do this manually, or by selecting the option for it to save automatically upon order completion. They also get a list of past orders which they can view at any time.

![User Profile](/readme-assets/profile.png)


### **Product Management**

Superusers/admins can manage the products available on the site. They can add, edit and delete products.

![Add product](/readme-assets/add-product.png)

![Edit product](/readme-assets/edit-product.png)

### **Footer**

The sites footer contains links to the social media sites and also a form to allow users to sign up for the GK Ireland newsletter.

![Footer](/readme-assets/footer.png)

### **404 Page**

If for some reason there is an error with the site, there is a custom 404 page which lets the user know there has been an error and gives them a link back to the home page.

![404 Page](/readme-assets/404page.png)