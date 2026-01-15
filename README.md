# Overview

This is a simple Customer Relationship Management software for a dental clinic.

I've created a dashboard where staffs can have access to and manage patient data. Used django authentication


Staff roles include: dentist, receptionist and admin


Functionalities include managing patients and patient appointments.


Each role has specific capabilities:

--Dentist can only view

--Receptionist can create patients and appointments as well as delete appointments

-- Admin can do everything including deleting patients


I've also activated the admin page where staffs can be managed.


I've created two staffProfiles to aid sampling - receptionist and dentist.
Only staffs can log in to access the dashboard.


Use any of the staff profiles above to login.


Password is qwerty54321


I integrated the software with google firebase where the patients data and appointments are stored. The appoinment table has a many-to-one relationship with the patients table in firebase. While dbSQLite is used for storing staff profiles.

I also created a superuser to aid sampling :
- username: superuser
- pwd: superuser12345
Only admins can access the admin panel

To use the software, simply login with any of the staff profiles above explore all the functionalities.


I developed this software to help dental clinics manage patients effectively and improve patient communication and appointmnets.



[Software Demo Video](https://www.loom.com/share/f0ef127cd74a444b96632fddacfbd235)

# Cloud Database

I used google firebase and dbsqlite
The firebase databse is used to store appointments and patient data.
The dbsqlite is used to store staff profiles.

# Development Environment

- Visual Studio Code
- Python
- Django

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django#_types-of-databases)
- [Google Firebase](https://www.google.com/aclk?sa=L&ai=DChsSEwj13pzy5I2SAxWTklAGHdakEoMYACICCAEQABoCZGc&ae=2&co=1&ase=2&gclid=CjwKCAiAvaLLBhBFEiwAYCNTf1mCyPgW6_OlNywrIfCkW8DPFFoNYe9nmMBVVSzd5iMDy9P5TtJpgBoCQcEQAvD_BwE&cid=CAASuwHkaHFXBH7Fy7QJdwaXdb6bVlFhAWP4r02TAnhlVAMXx56aH6cZHdiRawPRho5Hxb-KrBjF3CoBa2DR962kHNDp5vFNwriQlY_4aLY4i5AxNyIaxeaEVDA_OleoTnW3fEw2iKf4_WM2IQ0Gjrb9LwfRrKt6EBz9ijuyY9ZBYKVBh87Pn6SKY0OS-j-NnZpo_DqBjAhCHUPdgWYIOdyWJJOu3SNolKVG9ga-HRZ6kHNUsM3_ITJNUaHAPGWo&cce=2&category=acrcp_v1_71&sig=AOD64_0XT8E8zuNKMq8nHPQD8KmV9PUxMQ&q&nis=4&adurl&ved=2ahUKEwjKqZfy5I2SAxW0dUEAHXFnEAIQ0Qx6BAgMEAE)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Better css styling
- Notifications using Node.js
- Ability to send bulk emails
- Analysis