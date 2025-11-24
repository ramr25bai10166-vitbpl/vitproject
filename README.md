**Project Title**: Multi-purpose Program

**Overview of the Project**

This Python project brings together several small but commonly needed
tools into one menu-based script. Instead of opening different apps for
basic math, geometry, or quick timing, the program gives everything in
one place. It's simple to use, and is meant to be beginner-friendly.

You can choose between performing arithmetic, calcalating areas and
volumes of shapes, solving quadratic equations, or using a built-in
stopwatch. All options run inside a single Python file.

**Features**

The program offers:

1.  **Basic Arithmetic Calculator:** Performs addition, subtraction,
    multplication, and division using high-precision decimal numbers and ensuring no floating pont errors.

2.  **2D Geometry:** Calculates the area and perimeter/circumference for
    four common shapes like:

    - Square

    - Rectangle

    - Triangle (also supports Heron\'s formula and Right-Angled triangle
      methods)

    - Circle

3.  **3D Geometry:** Calculates the surface area and volume for four
    common shapes:

    - Cube

    - Cuboid

    - Sphere

    - Cylinder

4.  **Quadratic Equation Roots finder:** Finds the roots of a quadratic
    equation (standard form)(ax\^2 + bx + c = 0), handling real and
    complex (imaginary) roots (uses cmath library for complex roots).

5.  **Stopwatch:** A simple stopwatch for timing small tasks. It uses
    time module.

**Technologies/Tools Used**

- **Language:** Python 3.14

- **Core Libraries:**

  - math: For constants (eg: pi) and standard mathematical functions.

  - sys: For exiting the program using sys.exit().

  - decimal: for precision in calculations

  - cmath: for complex roots is quadratic equation

  - time: Used for the stopwatch.

**How to Run the Project**

1.  **Requirements:** Ensure you have Python 3.14 (or higher version)
    installed in your devicw. You can download it from
    [python.org](https://www.python.org/).

2.  **Save the file:** Save the program code into any file having any
    name ending with .py.

3.  **Run the program:** The program can be run through idle, pycharm,
    etc.

4.  **Interaction:** A menu will appear, you can enter a number
    corresponding to what task you would like to peform with it.

**Instructions for Testing**

You can test the program by selecting the relevant option from the main
menu and providing specific test values. Eg:

| **Feature No.** | **Function**               | **Test Input & Expected Output**                           |
|-----------------|----------------------------|------------------------------------------------------------|
| **1**           | Basic Calculator           | **Input:** 5 \* 2.5<br>**Output**: 12.5<br><br>**Input:** 10 / 0<br>**Output**: Division by zero is undefined. Please try again. |
| **2**           | 2D Shapes Perimeter & Area calculator | **Input (Length/Width):** 5, 10<br>**Output:** Area: 50, Perimeter: 30 |
| **3**           | 3D Shapes surface area & volume calculator | **Input (Radius):** 1<br>**Output:** Surface Area: 12.56637061, Volume: 4.188790204 |
| **4**           | Quadratic Equation Roots finder | **Input** (a, b, c)**:** 1, -3, 2 (x\^2 - 3x + 2 = 0)<br>**Output:** The roots of the equation 1.0x\^2 + -3.0x +2.0 are 2.0,1.0 |
| **5**           | Stopwatch                  | Start, wait 5 seconds, Stop<br>**Output:** Elapsed time: 5.0 seconds |

**Screenshots**

1.  Basic Calculator

<img width="940" height="452" alt="image" src="https://github.com/user-attachments/assets/66fa0084-1f2f-47ba-acfb-6b8c64a55bfa" />


2.  2D Shapes Perimeter & Area calculator

<img width="940" height="604" alt="image" src="https://github.com/user-attachments/assets/73c513e1-f224-407b-8acc-df074e638f04" />


3.  3D Shapes surface area & volume calculator

<img width="939" height="564" alt="image" src="https://github.com/user-attachments/assets/715e23f6-9f14-483f-a04b-f32c165f9616" />


4.  Quadratic Equation Roots finder

<img width="940" height="439" alt="image" src="https://github.com/user-attachments/assets/23a0159d-634f-4516-9412-3012126e7d94" />


5.  Stopwatch

<img width="940" height="404" alt="image" src="https://github.com/user-attachments/assets/1d9f6fcd-4591-4d15-bb0a-7bfea08c7d2d" />


6.  Examples of some error handling

<img width="940" height="861" alt="image" src="https://github.com/user-attachments/assets/68d9145a-d0e9-458d-aeff-630e0421c4a0" />

