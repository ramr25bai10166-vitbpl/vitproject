**Project Title**: Multi-purpose Program

**Overview of the Project**

This project, made in Python, is a multi-purpose program designed to
handle common mathematical calculations and utility tasks.

The program presents a main menu to the user, allowing them to select
from basic arithmetic calculator, 2D shape perimeter/area calculator and
3D shape surface area/volume, solving quadratic equations, and a simple
stopwatch feature.

It is built using the multiple modules for high-precision arithmetic,
ensuring accuracy for scientific and geometric calculations, performing
required tasks.

**Features**

The program offers the following core functionalities:

1.  **Basic Arithmetic Calculator:** Performs addition, subtraction,
    multplication, and division using high-precision decimal numbers.
    Includes error handling features like for division by 0.

2.  **2D Geometry:** Calculates the area and perimeter/circumference for
    four common shapes:

    - Square

    - Rectangle

    - Triangle (supports Heron\'s formula and Right-Angled triangle
      methods)

    - Circle

3.  **3D Geometry:** Calculates the surface area and volume for four
    common shapes:

    - Cube

    - Cuboid

    - Sphere

    - Cylinder

4.  **Quadratic Equation Solver:** Finds the roots of a quadratic
    equation (ax\^2 + bx + c = 0), handling real and complex (imaginary)
    roots.

5.  **Stopwatch:** A simple, interactive stopwatch utility that
    calculates elapsed time between two \"Enter\" key presses.

**Technologies/Tools Used**

- **Language:** Python 3.14

- **Core Libraries:**

  - math: For constants like pi and standard mathematical functions.

  - sys: For exiting the program gracefully.

  - decimal: Used extensively to ensure high-precision floating-point
    arithmetic.

  - cmath: Used for calculating the roots of quadratic equations,
    especially when the discriminant is negative (complex roots).

  - time: Used for the stopwatch functonality.

**Steps to Install & Run the Project**

Since this is a single-file Python script, installation is
straightforward.

1.  **Prerequisites:** Ensure you have Python 3.14 installed on your
    system. You can download it from
    [python.org](https://www.python.org/).

2.  **Save the file:** Save the provided code into a file having any
    name ending with .py.

3.  **Run from Command Line:** Open your terminal or command prompt,
    navigate to the directory where you saved the file, and execute the
    script.

4.  **Interaction:** The program will launch the main menu, and you can
    interact with it by typing the corresponding number (1-6) and
    pressing Enter.

**Instructions for Testing**

You can test the core functionalities by selecting the relevant option
from the main menu and providing specific test values. Eg:

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

