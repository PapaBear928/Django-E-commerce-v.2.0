<h1> Predatory Plants Shop - E-commerce shop </h1>
<h2> This is my variation on an e-commerce theme created using Django. Fully functional, with CRUD system, and BLOG module </h2>

*Link to version 1.0 here: https://github.com/PapaBear928/Django-E-commerce<br>
*Link to version 1.1 here: https://github.com/PapaBear928/Django-E-commerce-v.1.1



<h4>What's new?</h4>
-Adding the BLOG module with commentary system.<br>
-Adding missing or empty pages (e.g. stationary shops)<br>
-STRIPE was replaced by PayPal<br>
-Tests<br>
-Minor changes<br>



<h4>Used tech:<br>
Python 3.10.2<br>
Django 4.0.4<br>
HTML5<br>
CSS<br>
AJAX<br>
Bootstrap 5.1.3<br>
Swagger UI 4.12.0 <br></h4>


<h3>SETUP(as if someone didn't know that):</h3>

<h4>To run setup first create virtual environment:</h4>
<i>py -m venv venv</i>

<h4>Then, after your venv folder is created open it by: </h4>
<i>venv\scripts\activate</i>

<h4>And then install requirements included in field requirements.txt :</h4>
<i>pip install -r requirements.txt</i>

<h4>And then migrate files </h4>
<i>py manage.py migrate --run-syncdb</i>

<h4>After installation complete you can run server with project :</h4>
<i>py manage.py runserver</i>

<h3>This app has email verification system, so be attention to use existing email address!</h3>

<h4>Of course, you can use one of my test accounts.</h4>
<h5>Admin account</h5>
<i>login: test@test.com	  password:superuser </i>


<h5>Regular account</h5>
<i>Name: Bob bob@bob.com  password:anotherpassword1</i>



<h2>Features</h2>
The main feature of this project was creating an online store, which will include all features that the real shop has.In addition, following the example of many other shops, a blog has been added so that the shop developers can share their thoughts with shoppers. The blog module also has a comment system implemented.

<h3>Home</h3>
In home screen I've decided to put little greeting. If the user is logged in, there will be a button to go to the store. If not, the button will redirect him to the login page.He can also click on the navbar, where there are links to the store, not yet implemented website functions and to the user panel and login.

<h3>Stationary stores</h3>
After clicking on this button, the user will be redirected to a page where the locations of stationary shops are listed. All locations are of course fictitious and chosen humorously.

<h3>Our blog</h3>
When the user clicks on this button, they will be redirected to the blog-quasi page. The articles are displayed in reverse order of publication. After clicking on one of the articles, a page with the article will be displayed, where at the very bottom the user is given the opportunity to comment on the article, and return to the previous page.

<h3>Our products</h3>
Under the name "Our products" there is a store divided according to categories assigned by the administrator who places the product in the store. Added ability to add products to Wish lists and save for later.Additionally, the names of product categories added by the administrator will create categories in the shop. E.g. plants, accessories, seeds.

<h3>Account</h3>
In the "account" panel, the user can change his basic data, such as an email address. The user can add delivery addresses themselves. At the same time, the possibility of setting one of them as the default delivery address has been added.There is also an icon which refers the user to their Wish list. If nothing has been selected, the user will read an appropriate message about the lack of favourite products.

<h3>Login</h3>
In the "Login" panel, the user can recover his password, register or log in to the website.

<h3>Shopping Cart</h3>
If the user is logged in,he has access to his shopping cart. If the cart is empty, the user will only find a link to the store there. If there are any items in the basket, the user will add up the information about the total cost of the order, including shipping. From the same panel it is possible to change the number of ordered products or to delete the order. After clicking "Checkout" we will be taken to the payment finalization.

<h3>Payment</h3>
Once you have proceeded to payment, the implemented PayPal will guide you through the entire payment process.


