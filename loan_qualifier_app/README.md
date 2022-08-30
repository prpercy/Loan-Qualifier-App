# Loan Qualifier App (Module 2 Challenge)

Loan Qualifier App checks whether applicant's loan requirements adhere to banks' loan criteria. 

Qualifier app essentially looks at following paramters:
Credit score - Whether applicant's credit score is higher than minimum provided by banks
Loan size - Whether applicant's loan size is lower than offered by banks
Debt to Income - Whether applicant's debt to income ratio is lower than prescribed by banks
Loan to Value - Whether applicant's loan to value ratio is lower than prescribed by banks

In order to do so, it reads bank loans from the CSV file, performs the qualification process and eventually helps user to either store the qualified loans to CSV file or prompts them as per user's wish.


---

## Technologies

> Program uses Python 3.10.6 version. 

Program relies on 'questionary' and 'fire' libraries to ensure a dynamic CLI (command line interface) experience for the user (user recieves prompts/questions and answers to those are used as input by the program for further processes).

Program also imports from Path and CSV libraries to read and write files.

---

## Installation Guide

In order to use libraries such as 'fire' and 'questionary', please first install these libraries from Python Package Index as follows:
> pip install fire

> pip install questionary

---

## Contributors

Main author is : Pravin Patil. His linkedin profile is [Profile](https://www.linkedin.com/in/pravin-patil-5880301)

---

## License

MIT License