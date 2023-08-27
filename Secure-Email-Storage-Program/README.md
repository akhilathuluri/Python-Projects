# Secure-Email-Storage-Program

This is a Python script that creates a GUI application using the tkinter module. The application is a simple email storage program that allows the user to add, display and delete email addresses and their corresponding passwords. The script uses a text file to store the email addresses and passwords.

The script defines a class named popupWindow that creates a popup window asking the user for a password. The user needs to enter the correct password to gain access to the main window where they can add, display and delete email addresses and passwords.

The script defines two classes named entity_add and entity_display. The entity_add class is responsible for adding email addresses and their corresponding passwords to the text file. The entity_display class is responsible for displaying the email addresses and their corresponding passwords on the main window.

The script defines three functions named onsubmit, clearfile and readfile. The onsubmit function is called when the user clicks the submit button to add a new email address and password. The clearfile function is called when the user wants to delete all the email addresses and passwords from the text file. The readfile function is called to read the email addresses and passwords from the text file and display them on the main window.

The script creates a global variable named objects, which is a list that stores instances of the entity_display class. The objects list is used to keep track of the email addresses and passwords that are displayed on the main window so that they can be deleted if necessary.
