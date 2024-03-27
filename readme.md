# CECS 342 - Lab Assignment 4

## Due Date

- **Sunday, March 31**

## Total Points

- **20 points**

---

## Overview

In this lab assignment, we're diving into two powerful features of Python: decorators and asynchronous programming. The lab is divided into two main parts, each focusing on a distinct aspect of Python programming.

- **Part 1**: Utilizes decorators to streamline the process of adding authorization checks to multiple functions, ensuring code remains DRY (Don't Repeat Yourself) and maintainable.
- **Part 2**: Explores asynchronous programming by scheduling concurrent execution of functions to calculate factorials, showcasing the use of `async`, `await`, `asyncio.sleep()`, `asyncio.gather`, and `asyncio.run()`.

## Part 1: Understanding and Applying Decorators (`decorator.py`)

### Objective

Implement a decorator to add authorization checks to functions, eliminating redundant code and adhering to the DRY principle.

### Task

- Create a decorator that checks if a user is authorized before allowing function execution.
- Apply this decorator to multiple functions, ensuring that each function only executes if the user is authorized.
- Implement this in a file named `decorator.py`.

### Grading Criteria

Submissions will be graded based on:

- Correct implementation of the decorator.
- Successful application of the decorator to multiple functions.
- Adherence to Python coding standards and practices.

## Part 2: Concurrent Execution with Asyncio (`coroutine.py`)

### Objective

Demonstrate the use of Python's asynchronous capabilities to run multiple factorial calculations concurrently.

### Task

- Define an asynchronous function `factorial` that calculates the factorial of a given number with a delay, simulating a time-consuming task.
- Schedule concurrent execution of multiple instances of the `factorial` function with different parameters.
- Implement this in a file named `coroutine.py`.

### Grading Criteria

Submissions will be evaluated based on:

- Correct use of `async`, `await`, `asyncio.sleep()`, `asyncio.gather`, and `asyncio.run()`.
- Successful concurrent execution of factorial calculations.
- Output correctness and adherence to the provided output sample.

---

## Submission Instructions

Each team member must submit the following files to Canvas:

- `decorator.py` and `coroutine.py` files.
- A PDF file containing a copy of `decorator.py` and `coroutine.py` along with the runtime output.

Points will be deducted for missing files, incorrect outputs, syntax errors, or incomplete programs as outlined in the assignment details.

## Team Collaboration

- Clearly indicate the completion level of the lab assignment for each team member in the submission comments.
- All team members must agree on the completion level of each member, ranging from 100% for a fully successful program to 0% for no submission.
