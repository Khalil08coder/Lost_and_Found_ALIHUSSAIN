Ali Hussain Lost And Found App
Lost and Found is a desktop app that tracks lost and found items around Macleans College. It involves logins, report items, found items, and the ability to browse both. Built using Python, Tkinter, and SQLite

Feature: Student login Report lost items View all reported items View all found items About section Search Bar (currently not working)

Strucutres

| File | Role |

run.py|Entry point of the entire app gui4.py|Window with mmost of the code and is shown after a successfull login report.py|Window that is opened when interacting with report button, responsible for reporting items found.py|Window for inputed found items dbinformation.py|Main database connections colours.py|Colours constants used across all windows setup_db.py|Script used one time to create database tables

HOW TO RUN

FOR THE FIRST RUN : Run setup_db.py to create the Lost_and_found.db with the required tables and the 4 test logins. If the database ever needs rebuilding, there is corruption, this file can be ran to fix the problem

Then run run.py to launch the intended app. Login using one of the credentials listed below

Student ID 22000 password123 23456 mypassword 23567 pass111 22222 pass222

## Requirements
Python 3.14.5+
tkinter (included with standard Python)
sqlite3 (included with standard Python)
datetime (included with standard Python)
re (included with standard Python — used in Validate.py for regex)
os (included with standard Python — used in dbinformation.py for file paths)
Pillow (PIL) — NOT included with standard Python, must be installed separately
