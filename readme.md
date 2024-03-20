# CECS 342 Lab Assignment 4 - Decorators

## Objective
Learn and implement decorators in Python to extend the functionality of functions at runtime without modifying the original function code. This lab will focus on applying decorators to add authorization checks to functions.

## Due Date
Wednesday, March 27

## Total Points
20 points

## Background
A decorator in Python is a function that takes another function and extends its behavior without explicitly modifying it. Decorators allow for the dynamic alteration of the functionality of your functions or methods. This lab introduces the concept of decorators and their application in implementing authorization checks in a DRY (Don't Repeat Yourself) manner.

## Task Description

### Problem 1: Implement Authorization Checks using Decorators (10 Points)
You are provided with several functions, each performing separate tasks. Your job is to add authorization checks to these functions in an efficient way that avoids redundancy and adheres to the DRY principle.

## Instructions

### Step 1: Understanding Decorators
- Familiarize yourself with the basic concept of decorators as shown in the introductory example. Understand how decorators can wrap a function to modify its behavior.
- Notice how the `@decorator` syntax simplifies the application of decorators.

### Step 2: Implement the Authorization Decorator
- Create a decorator that checks for authorization before executing the function it decorates.
- The decorator should only allow the function to run if `is_authorized()` returns `True`. Otherwise, it should return a message indicating the lack of authorization.
- Apply this decorator to the provided functions (`do_A`, `do_B`, `do_C`) to enforce authorization checks.

### Step 3: Apply the Decorator
- Modify the provided functions to use your authorization decorator, ensuring that each function adheres to the authorization requirement.

### Step 4: Testing
- Test your implementation to ensure that the authorization checks are working as expected. Functions should only execute if authorized, and an appropriate message should be returned if not authorized.

## Submission Requirements
- Submit a `Lab4.py` file containing your code. (Failure to submit will result in a deduction of 10 points)
- Submit a PDF file containing a copy of your `Lab4.py` file and screenshots of your runtime output. (Missing this file and its contents will result in a deduction of 5 points)

## Grading Criteria
- Program runs successfully with correct output: 100% completion
- Program runs successfully with incorrect output: 60% completion
- Program has syntax errors or is incomplete: 40% completion
- Program has few coding and syntax errors: 30% completion
- No submission: 0%
