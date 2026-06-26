# CS50P - Introduction to Programming with Python

> Harvard University's course on Python programming, offered free via [cs50.harvard.edu/python](https://cs50.harvard.edu/python/)

This repository contains my problem set solutions and final project for **CS50P**, taught by David J. Malan. The course covers Python from the ground up — no prior programming experience required.

---

## What is CS50P?

CS50P is Harvard's dedicated Python course. Unlike CS50x (which covers computer science broadly across multiple languages), CS50P focuses entirely on Python — from basic syntax to real-world programming patterns like OOP, file I/O, and unit testing.

---



## Topics Covered

| Week | Topic |
|------|-------|
| 0 | Functions & Variables |
| 1 | Conditionals |
| 2 | Loops |
| 3 | Exceptions |
| 4 | Libraries |
| 5 | Unit Tests |
| 6 | File I/O |
| 7 | Regular Expressions |
| 8 | Object-Oriented Programming |
| 9 | Et Cetera (type hints, `map`/`filter`, closures, and more) |

---

## Repository Structure

```
CS50P/
├── cheat_sheets/       # Personal reference notes
├── week_0/             # Functions & Variables
├── week_1/             # Conditionals
├── week_2/             # Loops
├── week_3/             # Exceptions
├── week_4/             # Libraries
├── week_5/             # Unit Tests
├── week_6/             # File I/O
├── week_7/             # Regular Expressions
├── week_8/             # Object-Oriented Programming
├── week_9/             # Et Cetera
└── final_project/      # Bitcoin Profit Calculator
```

---

## Final Project - Bitcoin Profit Calculator

**Video Demo:** [youtube.com/shorts/MgiQjQdDda0](https://youtube.com/shorts/MgiQjQdDda0)

[![Bitcoin Profit Calculator Demo](https://img.youtube.com/vi/MgiQjQdDda0/0.jpg)](https://youtube.com/shorts/MgiQjQdDda0)

A CLI tool that calculates profit/loss and ROI from a Bitcoin investment between any two dates.

The program pulls historical prices from a local `bitcoin.csv` (daily closing prices from 2010 to early 2026) and falls back to the live [CoinCap REST API](https://coincap.io/) for current prices — directly building on the Week 4 problem set `bitcoin.py`, which only fetched a live price. This project extends that idea by combining historical data with live pricing to calculate actual returns.

**Key files:**

| File | Purpose |
|------|---------|
| `project.py` | Main program — input handling, CSV lookup, API call, profit calculation |
| `test_project.py` | `pytest` tests for `calculate_profit_loss`, `get_price_from_csv`, and the API response type |
| `requirements.txt` | External dependency: `requests` |
| `bitcoin.csv` | Historical Bitcoin daily closing prices (2010–2026) |

---

## Certificate

[![CS50P Certificate](https://certificates.cs50.io/e8b3fda7-3a89-4189-890a-9a319adc1056.png?size=letter)](https://certificates.cs50.io/e8b3fda7-3a89-4189-890a-9a319adc1056.pdf?size=letter)
