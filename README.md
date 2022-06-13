# Bookworm

![Screenshot of mockup](#)

View the deployed site [here:](https://bookworm-project3.herokuapp.com/)

## Introduction
Bookworm is an interactive book review site for all book fans. The site allows registered users to search through the listed books for reviews and find their next book. Bookworm allows users to share their book reviews with fellow book lovers on the site. The site also allows registered users to keep a library of their own added books on their profile page. 

---
## User Experience (UX)
### User Stories 

- Unregistered User
    1. As an unregistered user, I want to be able to search for books on the site.
    2. As an unregistered user, I want to  be able to view reviews for each book.
    3. As an unregistered user, I want to  be able to Register as a new User on the site.    
    4. As an unregistered user, I want to  be able to get visual feedback when an action is completed.
    5. As an unregistered user, I want to  be able to contact the Site Owner with any questions or suggestion.

* Registered user
    1. As a registered user, I want to be able to login and logout of the site.
    2. As a registered user, I want to be able to search for books.
    3. As a registered user, I want to be able to add books.
    4. As a registered user, I want to be able to view all books that I have added on my profile page.
    5. As a registered user, I want to be able to write reviews about any book.
    6. As a registered user, I want to be able to edit my books and my reviews.
    7. As a registered user, I want to be able to delete my books.
    8. As a registered user, I should not be able to delete or edit other user’s books.

- Site Admin
    1. As the site owner, I want to be able to add books.
    2. As the site owner, I want to be able to edit any book.
    3. As the site owner, I want to be able to delete any book.
    7. As the site owner, I want to be able to add a genre.
    8. As the site owner, I want to be able to edit a genre.
    9. As the site owner, I want to be able to delete a genre.
    10. As the site owner, I want to be able to reset a user’s password.
    11. As the site owner, I want to be able to delete a user’s account.  


---
## Features
### Current Features

* Site is responsive on all screen sizes.
* Nav menu adjusts accordingly to unregistered, registered users and Admin depending on the users log in status.
* Identical footer and Navigation bar displayed across the site to provide continuity.
* Search bar on home page and profile page enables both registered and unregistered users to search for books by book title or author.
* Site visitors can register on the site.
* Registered users can log in and out of the site.
* Registered users can add books to the site, the book will also be displayed in their Library shown on their Profile page.
* Registered users can only edit their own added book.
* Registered users can only delete their own books.
* Admin users can add, edit and delete any books.
* Admin user can add, edit and delete any genre.
* Before a user deletes a book a confirmation is required preventing accidental deletion.
* Cancel buttons are also shown alongside edit and delete buttons in case the user changes their mind and wants to cancel changes.
* Social Media Links displayed in the footer on all pages.
* Contact Page allows user to contact site owner.
* Flash messages providing user feedback for registered users when initially registered, logged in, logged out.

### Future Features

* Registered Users can review books before adding them to the site.
* Admin users can edit the users password.
* Admin users can delete any users account.
* Pagination for the Home and Profile Pages
* Separate review section linked to the book for more in depth reviews.
* Allow all users to review any book and to rate the book
* Function to add all rating scores provide an average overall rating for the book.

---
## Design
### Colour Scheme
*I used [Coolors](https://coolors.co/) to generate a colour scheme, I chose this particular colour scheme because I did not want to go with the usual browns of a book review site. I wanted the site to stand out from other book review sites by including a more colourful palette.

![palette used for Project 3](static/images/screenshots/palette.png)

The colours chosen are intended to convey the feeling of relaxation and calmness when reading a book, while also attracting new user to the site. I selected only three of the colours to keep the site simple and less busy. 

The main colour used on all nav bars and footers was #297373 with the lighter #CCFFFF to ensure excellent readability. The main background colour was left as white #ffffff to ensure the book covers stood out on the page. This background colour was also perfect to use the #297373 again for the text. All cards use the colour #E6E6E6 from my colour palette with the text colour of #297373, once again ensuring that it could be easily read and complimented the background colour. 

[Adobe Color-Wheel](https://color.adobe.com/create/color-wheel) was used to match a complimentary colour for all buttons on the #297373 background, #F7C9AD was chosen as this colour stood out and highlighted the buttons on the page.

### Typography

I used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site. 
The __Source Serif Pro__ font is used for all headers and titles. Designed by Frank Grießhammer, from the Adobe Originals program started in 1989 as an in-house type foundry at Adobe.
__Source Sans Pro__ was designed to perfectly compliment Source Serif Pro, I used the Source Sans Pro font for the main text throughout the site. Both fonts work perfectly together, they are easy to read and help convey the subject of the site.
Both fonts are fully cleared for both personal and commercial use.

### Imagery
I have not used a background image on this site because I felt it would distract from the main focus of the site, the actual books with their cover images. Book cover images were taken directly from [Amazon](https://www.amazon.co.uk/).

Icons from [Font Awesome](https://fontawesome.com/) are used throughout the site. The icons help inform the user of the purpose of a particular section and lead to a more enjoyable user experience. I have also used a Font Awesome icon as my main logo displayed throughout the site <i class="fa-solid fa-book-open"></i>

---
## Wireframes

The wireframes for the Bookworm site were produced using Balsamiq. 
* Mobile Wireframes:
  - [Home Logged Out/Not Registered Page](static/wireframes/home-logged-out-mobile.png)
  - [Register Page](static/wireframes/register-mobile.png)
  - [Log In Page](static/wireframes/login-mobile.png)
  - [Profile Page](static/wireframes/profile-mobile.png)
  - [Add Book Page](static/wireframes/add-book-mobile.png)
  - [Edit Book Page](static/wireframes/edit-book-mobile.png)
  - [Admin Profile Page](static/wireframes/admin-profile-mobile.png)
  - [Admin Manage Genres](static/wireframes/manage-genres-mobile.png)
  - [Admin Manage Users](static/wireframes/…………..png)
  - [Contact Page](static/wireframes/contact-page-mobile.png)

* Desktop Wireframes:
  - [Home Logged Out/Not Registered Page](static/wireframes/home-logged-out-desktop.png)
  - [Register Page](static/wireframes/register-desktop.png)
  - [Log In Page](static/wireframes/logged-in-desktop.png)
  - [Profile Page](static/wireframes/profile-desktop.png)
  - [Add Book Page](static/wireframes/add-book-desktop.png)
  - [Edit Book Page](static/wireframes/edit-book-desktop.png)
  - [Admin Profile Page](static/wireframes/admin-profile-desktop.png)
  - [Admin Manage Genres](static/wireframes/manage-genres-desktop.png)
  - [Admin Manage Users](static/wireframes/…………..png)
  - [Contact Page](static/wireframes/contact-page-desktop.png)

---

