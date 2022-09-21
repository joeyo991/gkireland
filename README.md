# **GK Ireland**

![Home Page](/readme-assets/gkireland-home.png)

## **About**

The live site can be accessed by this [link](https://gk-ireland.herokuapp.com/).

GK Ireland is an online store that sells goalkeeper gloves and accessories.

_*This site is for training purposes only, the company is fictional and no orders will be charged or products received.* _

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

### **Sign Up Page**

This page allows the user to create an account.

![Sign Up page](/readme-assets/sign-up.png)

### **Log In Page**

This page allows the user to sign in if they have created an account.

![Login page](/readme-assets/login.png)

## Future Improvements and Features

### **Wish list**

In the future I would like for there to be a wish list feature where the user can save items they like so that they can purchase them in the future.

### **Bigger Catalogue**

I think if this were to be a real business/store, the site would need a much bigger catalogue of items.

### **Product Ratings**

In the future it could be a good idea to add a feature which allows users to rate the products they have purchased.

## **Design**

The central theme of the site is simplicity of use. It is aimed to guide the user to the best experience. I used the boutique ado project as an inspiration.

### **Colour Scheme**

![Colour Scheme](/readme-assets/colors.png)

I used this colour scheme because black and white always work well together, but I also though that the green made everything pop.

### **Typography**

Then main font used in the application is Lato. It's known for its round edges and is one of the most popular fonts on Google fonts and widely used pretty much everywhere.

### **Imagery**

I used this image for the home page because Gavin Bazunu is one of Ireand's best talents. He is a young Irish goalkeeper and an inspiration to many. I thought it was fitting for an Irish goalkeeping store.

![Background Image](/readme-assets/homepage-background-cropped.jpg)

## **Testing**

### **Testing User Stories**

| Customer/Site User Goals | Requirement met |
| ------------------------- | --------------- |
| As a shopper I can view a list of products so that I can select something to purchase | Yes |
| As a shopper I can view individual product details so that I can learn more about each product | Yes |
| As a shopper I can view the total of my purchases so that I can avoid spending too much | Yes |
| As a Site User I can easily register for an account so that I can have a personal account and be able to view my profile | Yes |
| As a Site User I can easily login or out so that I can access my personal account information | Yes |
| As a Site User I can easily recover my password in case I forget it so that I can recover access to my account | Yes |
| As a Site User I can receive an email confirmation after registering so that I can verify that my account registration was successful | Yes |
|  As a Site User I can have a personalized profile so that I can view my order history/confirmations and save my payment information | Yes |
| As a Shopper I can sort the list of available products so that I can easily identify the best priced, best rated and categorically sorted products | Yes |
| As a Shopper I can easily select the size and quantity of the products I am purchasing so that I don't accidentally select the wrong product quantity or size | Yes |
| As a shopper I can view items in my bag so that I can identify the total cost of my purchase and the items I will receive | Yes |
| As a shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase | Yes |
| As a shopper I can easily enter my payment information so that checkout quickly with no hassle | Yes |
| As a shopper I can feel my personal and payment information is secure so that I can confidently provide the needed information to make a purchase | Yes |
| As a shopper I can view a summary of my order so that I can verify my order was correct | Yes |
| As a shopper I can receive an email confirmation after checking out so that I can keep the confirmation of my purchases for my records | Yes |

| Store Owner/Admin Goals | Requirement met |
| ----------------------- | --------------- |
| As a Store Owner I can add products so that I can update my store catalogue | Yes |
| As a Store Owner I can edit/update products so that I can alter prices, descriptions, images and other information | Yes |
| As a Store Owner I can delete products so that I can remove items that are no longer for sale | Yes |

### **HTML Validation**

- HTML validation was done by using the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code (Ctrl+U) and pasting it into the validator.

#### **Base Template**

**base.html**

![base.html validation](/readme-assets/base-validation.png)

- These errors had no effect on the project and were because I was using Django.

#### **Basket app html**

**basket-total.html**

![basket-total](/readme-assets/basket-total.png)

**basket.html**

![basket](/readme-assets/basket-val.png)

**checkout-buttons.html**

![checkout-buttons](/readme-assets/checkout-buttons.png)

**product-image.html**

![product-image](/readme-assets/product-image.png)

**product-info.html**

![product-info](/readme-assets/product-info.png)

**quantity-form.html**

![quantity-form](/readme-assets/quantity-form.png)


### **checkout app html**

**checkout-success.html**

![checkout-success](/readme-assets/checkout-success.png)

**checkout.html**

![checkout](/readme-assets/checkouthtml.png)

### **home app html**

**index.html**

![index](/readme-assets/index.png)

### **products app html**

**quantity_input_script.html**

(JS file)

![quantity_input_script](/readme-assets/quantity-input-script.png)

**add_product.html**

![add_product](/readme-assets/add_product.png)

**edit_product.html**

![edit_product](/readme-assets/edit_product.png)

**product_detail.html**

![product_detail](/readme-assets/product_detail.png)

### **user_profiles html**

**profile.html**

![profile](/readme-assets/profilehtml.png)

### **CSS Validation**

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator.

### **checkout app css**

**checkout.css**

![checkout css](/readme-assets/checkoutcss.png)

### **user_profiles app css**

**profile.css**

![profile css](/readme-assets/profilecss.png)

### **base.css**

![base css](/readme-assets/basecss.png)

### **Python Validation**

- No errors were found when the code was passed through Valentin Bryukhanov's [online validation tool](http://pep8online.com/). According to the reports, the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code from all the files and pasting it into the validator.

- Although there were no errors, I did receive warnings about lines being too long and imports being unused. I decided against manually fixing all of these lines as they did not affect the code. Using "python3 -m flake8" I got a list of these lines.

![flake8](/readme-assets/flake8.png)

### **Lighthouse Reports**

**Home Page**

![Home page lighthouse](/readme-assets/homepage-lighthouse.png)

**Products Page**

![Products page lighthouse](/readme-assets/products-lighthouse.png)

**Shopping basket Page**

![Basket lighthouse](/readme-assets/basket-lighthouse.png)

**Checkout Page**

![checkout page lighthouse](/readme-assets/checkout-lighthouse.png)

**Profile Page**

![Profile page lighthouse](/readme-assets/products-lighthouse.png)

### **Compatibility**

Testing was conducted on the following browsers:
- Chrome
- Brave
- Firefox

The site worked and functioned as it should on all of the tested browsers.

### **Responsiveness**

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

![Responsiveness test](/readme-assets/responsive.png)

The screens shown above (from left to right) are:
- Large laptop 1440 x 900
- iPhone 8/7/6 Plus
- Galaxy S9/S8 Plus
- iPad

## **Bugs**

I came across one major bug during this project. When trying to deploy my project I received an error regarding some of my dependencies. I couldn't figure out how to fix the issue and ended up contacting Student Support. After a while the tutor I was chatting with (John) realised that dj_database_url needed to be at an earlier release. I then had to return django_database_url to the earlier version (0.5.0) and create a runtime.txt file specifying which version of django to run on heroku (3.9.14). When I did these two things the deployment went through fine.

![deployment error](/readme-assets/deployment-error.png)

![runtime.txt](/readme-assets/runtime.png)

## **Marketing**

### **Facebook Page**

I created a Facebook page for GK Ireland in order to market the site on the web.
The page has a profile picture, cover photo, general information, a few posts and a link to the site.

There is a link to the Facebook page [here](https://www.facebook.com/profile.php?id=100086035780598).

In case the page is taken down, here are some screenshots:

![Facebook Page 1](/readme-assets/facebook-1.png)

![Facebook Page 2](/readme-assets/facebook-2.png)

### **MailChimp**

I also added a form from MailChimp in the footer to allow site users to sign up to a GK Ireland monthly newsletter if they wish. Although the users who sign up won't actually receive a newsletter, if the site were to one day become a real e-commerce store, I would defintely create a newsletter to be sent out.

![MailChimp](/readme-assets/mailchimp.png)

## **Deployment**

### **Heroku**

The website is hosted on Heroku and can be accessed by visiting this [link](https://gk-ireland.herokuapp.com/).


The process for deploying the website to Heroku is as follows:

1. Create a Heroku account if you don't already have one.

2. Create a new app on Heroku.

    1. Go to the [Heroku dashboard](https://dashboard.heroku.com/apps).
    2. Click on the "New" button.
    3. Click on the "Create new app" button.
    4. Choose a name for your app.
    5. Choose a region.
    6. Click on the "Create app" button.

3. In your app go to the "Resources" tab.

    - Add a Heroku Postgres database.

4. In your app go to the "Settings" tab, press "Reveal Config Vars", and add the following config vars if they are not already set:

    1. ```AWS_ACCESS_KEY_ID``` = AWS key.
    2. ```AWS_SECRET_ACCESS_KEY``` = AWS secret key.
    3. ```DATABASE_URL``` = The url of your heroku postgres database.
    4. ```EMAIL_HOST_PASS``` = Email host password.
    5. ```EMAIL_HOST_USER``` = Host email.
    6. ```SECRET_KEY``` = A secret key for your app.
    7. ```STRIPE_PUBLIC_KEY``` = Stripe key.
    8. ```STRIPE_SECRET_KEY``` = Stripe secret key.
    9. ```STRIPE_WH_SECRET``` = Stripe webhook key.
    10. ```USE_AWS``` = Set to True.
    11. ```DISABLE_COLLECTSTATIC``` = 1 during development. Remove this when deploying to production.

5. In your app go to the "Deploy" tab.

    1. If it's already possible, connect your Heroku account to your GitHub account and then click on the "Deploy" button.
    2. If not, you need to copy the Heroku CLI command to connect your heroku app and your local repository.

        - ```heroku git:remote -a <your-heroku-app-name>```

6. Go to your local repository.

7. Login to your Heroku account in your terminal and connect your local repository to your heroku app.

    1. ```heroku login -i``` - Enter all your Heroku credentials it will ask for.
    2. Paste the command you copied from step 5 into your terminal.

8. Create Procfile.

    For this project I used gunicorn, so in my case I had the following Procfile:
    - ```web: gunicorn gkireland.wsgi:application``` - This runs the app on heroku.

9. Create ```requirements.txt```. This can be done by running the following command:

    - ```pip freeze --local > requirements.txt```

10. Add and commit all changes.

11. Push your changes to Heroku.

    - ```git push heroku master```
    or
    - ```git push heroku main```

12. Check the logs of your app in heroku dashboard and make sure everything is working.

## **Credits**
- [Django](https://www.djangoproject.com/) for the framework.
- [Bootstrap](https://getbootstrap.com/): for the templates.
- [Django-allauth](https://django-allauth.readthedocs.io/) for the authentication library.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://www.heroku.com/): for the free hosting of the website.
- [AWS](https://aws.amazon.com/): for the free access to the image/static file hosting service.
- [Stripe](https://stripe.com/en-ie): for the free payment processing.
- [Coolors](https://coolors.co/): for providing a free platform to generate your own colour palette.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [Google Fonts](https://fonts.google.com/): for providing a free platform to use Google Fonts.
- [KenBroTech](https://www.youtube.com/c/KenBroTech): for the django tutorials.
- [Code Institute](https://codeinstitute.net/ie/): for all of the course material and also the Boutique Ado walkthrough project which I relied heavily on for this.

_*This site is for training purposes only, the company is fictional and no orders will be charged or products received.* _