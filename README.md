# Cafe Menu Order Management System

A Python-based command-line interface (CLI) application that simulates a simple Point of Sale (POS) backend for a cafe. The system facilitates food and beverage ordering, validates user input, applies promotional discounts automatically, and processes final payment verification.

## Core Features

*   **Structured Menu Display:** Presents a formatted list of main courses (like Beef Rendang and Gyudon Bowl) and extra toppings sequentially to the customer.
*   **Fault-Tolerant Input Validation:** Strictly utilizes `try...except` blocks to prevent the application from crashing when users input invalid data formats (e.g., typing letters instead of numbers), ensuring the ordering cycle continues smoothly.
*   **Automated Discount Calculation:** Implements conditional logic to instantly reduce the customer's total bill by 10% if the final order total exceeds 50.
*   **Payment Verification:** Uses a `while` loop to suspend the transaction's completion until the customer enters a payment amount equal to or greater than the final calculated total.

## How to Run

1. Ensure Python 3 is installed on your local machine.
2. Save the source code into a file named `main.py`.
3. Open your terminal or command prompt, navigate to the directory containing the file, and execute the following command:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts: input the corresponding number (1-5) to add a main course to your cart, (6-9) for extra toppings, and type `0` to finish the order and print the final receipt.

## Technologies & Concepts

This project is built entirely using built-in Python features, requiring no external libraries or dependencies. Core software engineering concepts implemented include:
*   **List Data Structures:** Utilizing index access and dynamic list manipulation (e.g., `.append()`).
*   **Control Flow:** Managing application state using `while` and `for` loops.
*   **Exception Handling:** Catching and resolving `ValueError` exceptions to enforce business logic.
*   **Arithmetic Operations:** Handling real-time transactional math and discount processing.

---
**Developed by:** Michael Joseph Salusu
