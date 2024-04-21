# Homework 10.

## Issues and its solutions.
### 1. OpenAPI Docs page login and register example data mismatch

In this issue we found that the user data we had for creating a user and the data used for an example in code to login was not the same and this was the reason why we were getting errors while logging in. TO solve this issue we made sure that the username password was same for the creating a user and the data that we used to login to the webpage. This helped the end user to have a easy time interacting with the web application.

link to the issue: [https://github.com/Kiran-Ramisetti-kr483/event_manager/pull/2/files](https://)

### 2. AsyncSession app/dependencies.py

In this issue we had a function which was not defined or it was outdated. SO we had to rewrite the code to do the same thing as intended but using different packages and functions. The second issue I found was there were few mistakes while validating the username while reading it. It was taking a mixture of capital letters and small letters wich i changed to read only small letters. I forgot to commit na dpush it to the branch associated with the issue which is the reason you can see any changes in the files. 

link to the issue: [https://github.com/Kiran-Ramisetti-kr483/event_manager/pull/4](https://)

### 3. password validation

In this issue I found that it was taking wrong password and there were few issues like the application was taking an extra space. I had to change few lines of code to make sure that the application accepts only the data given to it without any extra space. I had to rewrite few test cases with respect to the changes I made in the codes in app folder.

link to the issue: [https://github.com/Kiran-Ramisetti-kr483/event_manager/pull/6/files](https://)

### 4. resolved internal server error and added few test cases

I was getting this issue while registering the user because there were few lines of code missing which was causing the internal server to fail and give a response as internal server error. I added the missing variables, functions and resolving import error. Thi shelped me to register the user with the data i gave without any insternal server error.

link to the issue: [https://github.com/Kiran-Ramisetti-kr483/event_manager/pull/8/files](https://)

### 5. Issue in deleting

In this issue I found that the user delete function had few errors in the output and things related to HTTPS codes. I changed few line of code in user delete function and add few test cases to make sure it is working fine.

link to the issue: [https://github.com/Kiran-Ramisetti-kr483/event_manager/pull/10/files](https://)

### 6. Issue in production.yml

In this issue I cound not build the docker images because it had few mistakes in the dockder file creation and pushing. I changes few lines in order to make it work.

link to the issue: [https://github.com/Kiran-Ramisetti-kr483/event_manager/pull/12/files](https://)

Working on Homework 10 proved to be a comprehensive exercise in both technical proficiency and collaborative skills development. Throughout the assignment, I faced a range of technical challenges that pushed me to delve deeper into software development practices. For instance, resolving discrepancies in the OpenAPI documentation for user login and registration processes was a significant issue. The mismatch between example data and actual requirements led to user login errors, impacting the application's usability. The solution involved aligning the example data with the actual data needed for user creation, which taught me the critical importance of consistency and accuracy in software documentation.

Another technical challenge involved updating dependencies and refining functions within the AsyncSession in app/dependencies.py. This task required adapting existing code to incorporate new software packages and modifying user input validation processes. Through this experience, I learned about the evolving nature of software tools and the necessity of staying updated with the latest developments in technology. Correcting these technical issues not only enhanced the functionality of the application but also reinforced my attention to detail and the significant impact of minor errors on the overall software performance.

Collaboratively, this assignment enhanced my skills in project management and effective communication within a team setting. An oversight in not committing and pushing changes after modifying validation rules highlighted the importance of maintaining regular updates and transparent communication with team members. This experience underscored the need for structured project management practices, such as regular check-ins and peer reviews before merging changes. These practices would not only improve the quality of the project output but also ensure a more cohesive and productive team environment.


![Screenshot (43)](https://github.com/Kiran-Ramisetti-kr483/event_manager/assets/157845848/b82f789a-ba1a-4642-8e59-3a4610d6bd74)
