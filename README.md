![header](static/images/readme/header.png)

<u><b>Overview</b></u>

Next Book Please is aimed at the avid readers out there. It is a database where readers can find book reviews quickly and easily with minimal fuss. Users can also leave reviews to help others choose which books they would like to read next.

For users who are less digitally confident, there are little hints and tips along the way to make the experience smoother and, for those who are not used to leaving reviews, there are also hints on what makes a good review.

It is designed as a space for anyone to use; younger and older, new reviewers and the more experienced ones and everyone in-between.

<u><b>Site Overview & UX</b></u>

![responsive](static/images/readme/responsive.png)

With the use of Bootstrap, the site is fully responsive on all platforms, as can be seen above. The nav bar collapses on small screens and the site is fully functioning and attractive on different screen sizes.

I went for dark, neutral colours for the design as a starting point however, when my test group checked it, they felt the greys and whites worked well with the background image; as such I left it those colours as they got a positive response.

The home screen is a simple box where users can login or register; if they wish to do neither, they can browse books via the navbar. The design is uncomplicated and easily navigable. This page however, is not accessible via the navbar if a user is logged in as it is unnecessary for logged-in users.

I designed the login and registration system to be as simple as possible; just a username and a double password check. When my test group came to trying it out they were pleased; although at the time I did not have the hint buttons; these were added as a result of my test group some of whom got confused regarding how to create a secure password without being told. 

When it came to adding a book, for the purposes of this project, I have asked users to add a link; again, as a result of the test group, I have added a hint box as some users were not aware of how to do this.

As an avid reader, I knew what I would look for in a review site however, I researched with other book readers what they would like to see. The overwhelming majority said they'd like it simple if they were adding a book with the only information being required being: image, title, author, genre. They also said they would like to see everything related to the books in one page (e.g. the book, the reviews and the ability to add a review) for ease of navigation; they did not want to have to go to many different pages to do what the site was intended; this is the reason for the layout. The only exception to this is the add book function which is only accessible from the user profile.

The final design and accessibility of all features has been checked by my test group who all said it was easy to navigate and the areas where they had struggled initially, were now clearly labelled with help.

<u><b>Home Page</b></u>

![homepage](static/images/readme/homepage.png)

The home page is plain, simple and easily navigable.

<u><b>Register</b></u>

![register](static/images/readme/register.png)

![register](static/images/readme/register1.png)

The registration page fits the same card design as the home and login pages. However, it provides handy hints on how to create a username and password. It also links back to the login page should the user have pressed register by accident.

![register](static/images/readme/errorregister.png)

Users are required to enter a username and their password twice; if they don't they are prompted to as can be seen above.

![register](static/images/readme/usernameexists.png)

![register](static/images/readme/passwords.png)

If a username already exists; the user is informed so they can choose another one or, if they enter two different passwords, they are informed so they can try again.

<u><b>Log In</b></u>

![login](static/images/readme/login.png)

The login page is again, plain and simple and allows users to go to the register page if required.

![login](static/images/readme/errorlogin.png)

Users are required to enter their username and password; if they don't they are prompted to as can be seen above.

![login](static/images/readme/incorrectlogin.png)

If the username or password are incorrect, a message is displayed; for security purposes it does not say which one is incorrect.

<b><u>User Profile</u></b>

![profile](static/images/readme/userprofile.png)

The user profile is a simple card with the users username on. The picture is randomly created; something the test group liked as a bit of fun. From the profile, a user can add a book, view their reviews and logout.

You can also see here, the different navbar when a user is logged in; they can easily access their profile and logout from there.

<b><u>Add Book</u></b>

![addbook](static/images/readme/addbook.png)

![addbook](static/images/readme/bookexists.png)

![addbook](static/images/readme/newbook.png)

The form for adding a book is consistent with all the other forms on the site. There is a hover-over informing users how to get a URL for an image.

If a book already exists in the DB, users are informed. If it doesn't, they're informed it has been added and redirected to the browse books page where their book will be at the top to easily add a review.

<b><u>My Reviews</u></b>

![myreviews](static/images/readme/myreviews.png)

![myreviews](static/images/readme/noreview.png)

In this area, users can see a quick overview of reviews they have left; these are in collapsible formats as on the browse books page for consistency. Users can easily return to their profile if they clicked 'My Reviews' by accident. When they expand a book, they can see the options to edit and delete their reviews.

If a user has not left any reviews yet, they are informed as such.

<b><u>Edit</u></b>

![edit](static/images/readme/edit.png)

When the user presses edit, they are taken to this page. The title is not-editable so it links to the DB and the book correctly. After it was tested, users asked if their initial review could be auto-filled into the review area and thus, this was implemented. 

Users can also return to their reviews if they pressed the wrong book.

<b><u></u></b>

<u><b>Browse Books</b></u>

![browsebooks](static/images/readme/browsebooks.png)

![browsebooks](static/images/readme/browsebooks1.png)

![browsebooks](static/images/readme/goodreview.png)

![browsebooks](static/images/readme/rating.jpg)

The browse books page again, is easily navigable with all items available on this page. As you can see, users who are not logged in cannot leave a review but can easily access the log in page, but those who are, can. The new rating link has a help button to show users the criteria for their rating. There is also a pop-out helping readers understand what makes a good review. There is also a link to a generic amazon page for books; this would book hooked up to the actual book.

![browsebooks](static/images/readme/viewreview.png)

![browsebooks](static/images/readme/addreview.png)

The view review and add review (when logged in), both collapse and expand easily with a click. For the add review, the user is not required to input anything other than their review and rating and then press submit.

<b><u>Log Out</u></b>

![logout](static/images/readme/logout.png)

When a user logs out, they are redirected to the home page where they can easily re-log back in.

<b><u>Wireframes</u></b>

<i>Home Page</i>

My Wireframes were created on [GIMP](https://www.gimp.org/). Other than the nav bar, which needs to collapse on small screens, I wanted my design to be the same across devices.

![wireframe](static/images/readme/homepage.jpg)

<i>Browse Books</i>

![wireframe](static/images/readme/browsebooks.jpg)

<i>Profile</i>

![wireframe](static/images/readme/profile.jpg)

<i>My Reviews</i>

![wireframe](static/images/readme/myreviews.jpg)

<b><u>User Stories</u></b>

As a reader, I want somewhere to leave reviews.

![userstory](static/images/readme/userstory1.png)

As a reader, I want to easily be able to see reviews about books I might be interested in.
As a reader, I don't want to see all information about a book in one place.

![userstory](static/images/readme/userstory2.png)

As a reader, I want to be able to search by my favourite genre or author.

![userstory](static/images/readme/userstory3.png)

As a reader, I want to be able to edit and delete reviews I leave in case I make typing errors/change my mind about a book.

![userstory](static/images/readme/userstory4.png)

As a reader, I'd like to have a link to where I can buy a book I am interested in. 

![userstory](static/images/readme/userstory5.png)

<u><b>Next steps</b></u>

To improve the site, the links to purchase would be accurate. There would also be pagination and a more interactive rating system.

<b><u>Testing and Validation</u></b>

<i>Pep8</i>

![pep8](static/images/readme/pep.png)

Due to getting some errors in the Git workspace which couldn't ever be fixed no matter what I tried, I ran my code through [pep8](http://pep8online.com/checkresult) and all the Python code is pep8 compliant.

<i>Speed Test</i>

![speedtest](static/images/readme/speedtest.jpg)

![speedtest](static/images/readme/speedtest1.jpg)

When I ran my site through [GTMetrix](https://gtmetrix.com/), I tested both the home page and the browse book page (due to the number of images on there). Initially both came back as a B rating due to the size of the background image; after a couple of tries, I managed to reduce this in size, without reducing quality, to achieve an a rating on both pages.

<i>Colour Contrast Check for Accessibility</i>

![colorcheck](static/images/readme/color.jpg)

As all pages have the same colour scheme, I just checked the main page on the [a11y](https://color.a11y.com/Contrast/)check and it passed accessibility.

<i>CSS Validator</i>

![css](static/images/readme/css.jpg)

My CSS code passed checks at [W3C](https://jigsaw.w3.org/css-validator/validator)

<i>JS Validator</i>

![js](static/images/readme/js.jpg)

My JS code is taken from Bootstrap but it passed checks at [JSHint](https://jshint.com/).

<i>HTML Validation</i>

<u>Home</u>

![html1](static/images/readme/html1.png)

<u>View Reviews</u>

![html2](static/images/readme/html2.png)

<u>View Books</u>

![html8](static/images/readme/html8.png)

<u>Edit</u>

![html3](static/images/readme/html3.png)

<u>Add Book</u>

![html4](static/images/readme/html4.png)

<u>Login</u>

![html5](static/images/readme/html5.png)

<u>Register</u>

![html6](static/images/readme/html6.png)

<u>Edit Book</u>

![html7](static/images/readme/html7.png)

Using the [W3C](https://www.w3.org/), I found a couple of small errors which have now been fixed as can be seen. The user profile page cannot be viewed due to requiring being logged in; I ran to code manually through the checker and the only errors received were about the Jinja templating. Other pages were checked before being user locked.

<b><u>Deployment</u></b>

The site has been deployed and is available to view [here](https://next-book-please.herokuapp.com/).

<b><u>Relational Database Model</u></b>

Due to the change in criteria close to the end of the project, we have been advised to show how our site would work in a relational database model. This can be viewed below.

![relational](static/images/readme/relational.png)

In this model, each book as a unique Book ID; this is then referenced as a foreign key in reviews to ensure that each review goes to the correct book. The Review ID is referenced in users so users can edit and delete their own reviews only and, the User ID is referenced in reviews so people can see who left what review.

<b><u>Issues and Bugs</u></b>

One of the bigger issues I have encountered was using the accordion system to display books, reviews and the ability to add reviews. Initially it was because I had styled all 'card' elemements the same way, once I had changed this, I couldn't get the cards to open individually; if one was clicked, they all expanded. I resolved this by adding {{ book._id }} to each accordion section so the code realised each new book was it's own individual item and therefore needed to act individually.

When I was trying to ensure duplicate books could not be added, I had difficulty getting the coding to work as I was trying to code it the same way as checking a username; this resulted in either all books being able to added (even if they were duplicates) or no book being able to be added (even if they weren't duplicates). I realised this was not the correct way and I managed to get it functioning by pulling out just the author and title and then checking for those initially.

I had some problems with getting reviews to display for all books; they were only displaying for the first book; this was because, in the Python, the reviews were not being compiled as lists so iteration was being stopped after the first round. Once I had changed reviews to a list, this fixed the problem.

There was a bug where the accordion when viewing your own reviews was jumping slightly when it was expanded. I coulnd't find the problem behind it so I rewrote the code and this fixed the problem.

One of the largest, repeated problems I have had has been with indenting in Python; I had to constantly check and recheck if it was correct and then change. There is still one problem with indentation which I cannot fix; I have tried everthing I can think of and, in the terminal, no matter what I have tried, it hasn't worked. I'm unsure what else to try to fix this.

<b><u>Technology, Languages and Tools</u></b>

This site has been created using HTML, CSS, JS & Python.

[GitHub](https://github.com/) for buiding the webpage.

[Heroku](https://www.heroku.com/) for webpage deployment.

[MongoDB](https://www.mongodb.com) to create the database.

[GoogleFonts](https://fonts.google.com/) for the fonts used in the project.

[GIMPSoftware](https://www.gimp.org/) to edit photos and create wireframes.

[GTMetrix](https://gtmetrix.com/) to check site speed.

[FontAwesome](https://fontawesome.com/) for the icon.

[W3C](https://www.w3.org/) for code validation.

[AmIResponsive](http://ami.responsivedesign.is/#) to check responsivity of the site.

[JSHint](https://jshint.com/) to check JavaScript code.

[a11y](https://color.a11y.com/Contrast/) to check accessibility of colours.

[word](https://www.microsoft.com/) to create relational tables.

[pep8](http://pep8online.com/checkresult) to check my Python was pep8 compliant.

[geeksforgeeks](https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/) for the code for expanding textareas.

<b><u>Media</u></b>

[NitinArya](https://www.pexels.com/photo/photography-of-book-page-1029141/) for the background image

<b><u>Acknowledgements</u></b>

With special thanks to Richard Wells for being a fabulous mentor.