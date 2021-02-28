## Testing

- [Validator checks](#validator-checks)
- [Testing user stories](#testing-user-stories)
- [Manual testing](#manual-testing)  
- [Additional testing](#additional-testing)
- [Known bugs](#known-bugs)
  
### Validator Checks

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page (apart from the ones where you need to be logged in) of the project to ensure there was no invalid code in the various languages used. There were some errors initially, but these were fixed and detailed in the commit history. 

- [W3C Markup Validator](https://validator.w3.org/) No errors or warnings
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) No errors.
- [JsHint](https://jshint.com/) (0 warnings)
- [PEP-8 checker](http://pep8online.com/) (All right)


### Testing User Stories

Please see the README.md for a detailed table view of the User Stories, including the Site Owner Stories. 

All user stories have been addressed. Screenshots have been included below in order to illustrate examples of this. Where possible, one screenshot will show evidence of multiple user stories being met.

I want to be able to:

**Viewing and Navigation**
1. See what I can do on this website
    * In addition to the section headings on the nav bar, the home page shows 4 sections that clearly and consicely state the services this website provides

2. Navigate around the site easily and not get 'stuck' on pages 
    * Back to top buttons are provided on the pages where there are long lists: shop and events.
    * After paying for an order, the user is shown the checkout success page, which includes  
    
![linkout](/documents/screenshots/UX/2-link-out.PNG)

3. Be reminded that I'm logged in, and be able to easily log out.
    * When logged in, the username is shown in the navbar. Dark text on the yellow background is highly visible. 
    * Next to the username and bag, there is a **logout** button (cursor changes on hover). When clicked, this directs to the log out page, and 1 more click logs them out.

 ![logout](/documents/screenshots/UX/3-logout-nav.PNG)

4. View games and prices
    * The number of games are listed in a responsive manner, so larger screens see more games per row. The smallest screen sees just one game per row.
    * Prices are displayed on the list view.
*See screenshot in Sorting and Searching section below*
 
5. View further details of products I'm interested in
    * The game details page lists information for 8 different attributes of the game, in addition to the categories and mechanics. For an even more detailed description, users can follow the link to an offsite description.
    
![product_detail](/documents/screenshots/UX/5-prod-det.PNG)

6. See suggested games
    * On the home page, after the café section, there is a shop section.  This section displays a card carousel of randomly selected games and their names. Clicking these links the game detail page.
    
![suggested](/documents/screenshots/UX/6-suggested.PNG)

**Sorting and Searching**

7. See membership discount
    * Members and Premium members who are logged in will see their discount reflected in all price displays. This includes the shop page, game detail page, bag and check out pages. 

8. Sort by price, rating and complexity
    * Users can sort by these attributes, both ascending and descending, via the dropdown select at the top of the shop page. 

9. Filter by specific category or mechanic (and sort these)
    * Users can filter by category or mechanic via the dropdowns a the top of the shop page. The filtered lists can be sorted.

10. Search by name
    * Users can enter text into the search box at the top of the shop page and view their results.

11. Quickly view my results
    * Pagination is implemented, and the user is able to select items per page via the dropdown box at the top of the shop page.
    
![membershop](/documents/screenshots/UX/4-7-8-9-10-11-22-member-shop.PNG)

**Registration and User Accounts**

12. Users can register an account, and
13. Receive email confirmation of registration, and after verifiying their email address via link in the email they can
14. Log in and Out.
15. Forgotten passwords can be recovered by clicking 'Forgot password?' on the login page, and following the instructions per email.

16.-21 View my user profile
    * Clicking on the User icon or the username in the navbar directs to the My Profile page. This is where users can view information related to their profile, and save their address. This covers **user stories 16 - 21**, as evidenced by the below screenshot.

![profile](/documents/screenshots/UX/16-21-profile.PNG)

22. See in the nav bar that my purchase has been added to bag
    * When there are no items in the bag, only the bag icon is displayed in navbar. Upon adding items, the number of items is shown next to bag icon. The user receieved further feedback after adding an item via a success toast.
    
![feedback](/documents/screenshots/UX/22-bag-feedback.PNG)

23. Click on my bag to see what's been added
    * The shopping bag page shows a table that displays the product image, name, price, discount if applicable, quantity, and subtotal per item.
24. The user is able to update the quantity, and remove an item from the bag.
    * Pagination is implemented, and the user is able to select items per page via the dropdown box at the top of the shop page.
26. A member can again see their discount automatically applied with the Total, Discount and Grand Total fields.

![bag](/documents/screenshots/UX/23-24-26-bag.PNG)

25. Have my address pre-populated
    * If the user has registered an address in the my profile page, the address form will be pre-populated.

27. Recieve feedback of successfull payment
    * After the payment processing loading screen, the user is shown the checkout success page, and sees a toast.

**Membership**

28. Easily view and compare the different options and their costs.
    * The cards are laid out side by side on all but the smaller screens, lining up so features can be compared.

29. See my membership details
    * A member can see their membership level and expiration date both on the membership page and the my profile page.

30. Buy new membership
    * All registered users can buy membership, which will begin after their existing membership expires, if they already are members.

**Events**

31.-33. See Events, sign up and unsign from them.
    * Events are displayed to all, but only registered users (or members if members only) can sign up.

**Admin and Shop Management**

34.-36 CRUD operations for users designated as **staff** by the superuser in the Django admin panel
    * CRUD available for games, categories, mechanics, and events.
    * Not available for membership, but editing this would be a business decision rather than a day-to-day task, so I am happy not to have this option available to staff members. 
    
![staffarea](/documents/screenshots/UX/staffarea.PNG)
![staffedit](/documents/screenshots/UX/staffedit.PNG)
![gameedit](/documents/screenshots/UX/gameedit.PNG)


#### Site owner goals:
37. Extend discounts and offers to existing café customers
    * Becoming a member allows them to play for free at the café, depending on membership level, and the discount at the shop should entice them to shop for games at the Hexagon.

38 Make it more attractive to come to the café
    * The membership discount allows playing for free at the café.
    * A range of events is advertised, on the home page and events page in order to entice people to the café.
 
39.Invite/inform existing customers of events
    * Registered users and members will be sent newsletters and invitations.
    
40. Have my staff members able to Add/Edit/Delete games and events
    * See the **Admin and Shop Management** above.

### Manual testing

#### Testing during development

The majority of testing occured during development. Chrome Development Tools were used extensively, both for front-end styling as well as checking what is being POSTed. The CRUD functionality and filtering was tested both on the website and by checking within Django admin. Print() and console.log() functions were used in their respective languages to test logic such as IF statements.

#### Testing the finished website

The site was tested first as a logged-out user (desktop and mobile) and then as a logged-in user.


<details>
<summary>Manual Testing Log:</summary>
  
 | Functionality | Page | User | Expected Behaviour Seen? | 
 | --- | --- | --- | --- |
 | Nav bar and footer visible and responsive | Nav / Footer | All | Yes | 
 | Links on nav bar working correctly from all pages | Nav / Footer | All | Yes | 
 | Hamburger menu appears at expected breakpoint and functions | Nav / Footer | All | Yes | 
 | User name displayed in nav when logged in | Nav / Footer | All | Yes | 
 | Number of items in bag visible | Nav / Footer | All | Yes | 
 | Footer visible and responsive | Nav / Footer | All | Yes | 
 | Links on footer working correctly from all pages | Nav / Footer | All | Yes | 
 | Styles and Scripts correctly loading on all pages | All | All | Yes | 
 | In-page links visible and working, both to internal and external pages | All | All | Yes | 
 | Buttons working  | All | All | Yes | 
 | Hover-over working | All | All | Yes | 
 | Sections visible and responsive | Home | All | Yes | 
 | Carousels funcional and responive | Home | All | Yes | 
 | Page shows correct number of items per row for all breakpoints | Shop | All | Yes | 
 | Images and cards responsive and visible | Shop | All | Yes | 
 | Category and Mechanic filters working and displaying selected | Shop | All | Yes | 
 | Sort options working and displaying selected | Shop | All | Yes | 
 | Filter and sorting working and displaying in combination | Shop | All | Yes | 
 | Applying / reappplying filter/sort combinations | Shop | All | Yes | 
 | Clear filters/sorting removing filters/sorting | Shop | All | Yes | 
 | Pagination working correctly, maintaining any filters/sorting | Shop | All | Yes | 
 | Number of products per page working | Shop | All | Yes | 
 | Discounted price shown if member, not if not member | Shop | All | Yes | 
 | Search working correctly and can combine with sort | Shop | All | Yes | 
 | Discounted price shown if member, not if not member | Product Detail | All | Yes | 
 | Images and page responsive and visible | Product Detail | All | Yes | 
 | Categories and Mechanics visible | Product Detail | All | Yes | 
 | Clicking on Cat/Mech leads to relevant filtered shop page  | Product Detail | All | Yes | 
 | Discounted price shown if member, not if not member | Bag | All | Yes | 
 | Buttons for + and - increase/decrease quantity of items | Bag | All | Yes | 
 | Update / Remove working correctly | Bag | All | Yes | 
 | Table visible and responsive | Bag | All | Yes, but introduces horizontal scroll on smallest mobile screens | 
 | Form correctly displayed and responsive | Checkout | All | Yes | 
 | Form fields provide feedback if not correctly filled in | Checkout | All | Yes | 
 | Address is saved to profile if logged in | Checkout | All | Yes | 
 | Can 'Edit Bag' and return to bag page | Checkout | All | Yes | 
 | Loading screen while checking card details | Checkout | All | Yes | 
 | Appropriate messages when checkout fail | Checkout | All | Yes | 
 | Correctly checking out leads to checkout success page | Checkout | All | Yes | 
 | Top paragraphs display intended text depending on user: | Membership | All | Yes | 
 | - User name / Current membership level / Expiration Date | Membership | Members | Yes | 
 | - Some paragraphs advertising benefits of membership | Membership | Non-members | Yes | 
 | Cards and content visible and responsive | Membership | All | Yes | 
 | Dropdown adds correct duration of membership | Membership | All | Yes | 
 | Buy buttons add to bag correctly | Membership | All | Yes | 
 | Cards and content visible and responsive | Events | All | Yes | 
 | Correct content displayed | Events | All | Yes | 
 | Only Registered Users can sign up and unsign for events | Events | All | Yes | 
 | Event is added to/removed from profile page | Events | All | Yes | 
 | Clicking Sign up or Unsign multiple times gives no errors on page or db | Events | All | Yes | 
 | Shows Log in and Register buttons when not signed in | Profile | Logged out  | Yes | 
 | Shows appropriate info (Membership, Address, Order History, Events) | Profile | Registered, Members | Yes | 
 | Save / Update address working | Profile | Registered, Members | Yes | 
 | Shows link to staff-only section  | Profile | Staff | Yes | 
 | Username minimum 4 characters | Profile | All | Yes | 
 | Password cannot be same as username | Profile | All | Yes | 
 | Password confirm must match | Profile | All | Yes | 
 | Email fields must be email format | Register | All | Yes | 
 | Confirm email must be same as first email | Register | All | Yes | 
 | Cannot register with username that already exists | Register | All | Yes | 
 | Cannot register with email that already exists | Register | All | Yes | 
 | Can see and access staff area on profile page | Staff | All | Yes | 
 | Can delete multiple items in one go | Staff | All | Yes | 
 | Can addgames, categories, mechanics and events | Staff | All | Yes | 
 | Can edit games, categories, mechanics and events | Staff | All | Yes | 
 | Can remove games, categories, mechanics and events | Staff | All | Yes | 
 | Pagination and items per page functions | Staff | All | Yes | 
 | Search functions | Staff | All | Yes | 

</details>
  

### Additional testing

-   The website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.
-   The website was viewed, using Chrome Developer Tools with responsive mode, as well as on a variety of actual devices such as Desktop, Laptop, iPhone 11 and a Motorola phone.
-   Friends and family members were asked to review the site to point out any bugs and/or user experience issues.

### Known Bugs

**Applying multiple sort filters can occasionally not work properly**

Due to the fragile method used for handling URL parameters, changing a lot of filters or sorting can sometimes break pagination or display the wrong thing. This could be fixed by improving the code quality in the URL parameter handling, but this was too big a task for the remaining time that I had.

**Changing membership type causes unexpected behaviour**

Steps to reproduce are as follows:
- Buy one year of Premium Membership
- Buy one month of standard Membership
- Note that the site will now think you have 13 months of standard Membership, and you will have lost the Premium Membership discount

This issue was an oversight when designing the membership system. Fixing it would probably take the form of allowing users to "upgrade" their normal membership to Premium for a cost, and disallowing buying normal membership when already Premium. Fixing it was simply too much work for the remaining time, and it didn't seem to be very high priority.

**Membership implementation is very fragile**

When approaching membership as a concept, I didn't want to have to add a new payment system just for these. As such, I retrofitted memberships as Products. This was a simple solution but led to a number of problems and I have ended up with lots of hacky solutions and workarounds. For example, referring to the membership products directly by ID, or having to add "is_membership" to the Product model.

To fix this, I would come up with a more elegant solution to decouple membership from product, but this was too much work.

**Incorrect Toast**

After checkout success users are shown a toast that says they are sent an email confirmation of their order. As noted elsewhere in this readme, this feature has not yet been implemented.

