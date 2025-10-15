# Exploraci-n-de-datos-EDA-
Ejercicios en Python usando libreria Pandas

Q1. Pandas version

What version of Pandas did you install?

You can get the version information using the __version__ field:

pd.__version__

 
Getting the data

For this homework, we'll use the Car Fuel Efficiency dataset. Download it from here.

You can do it with wget:

wget https://raw.githubusercontent.com/bigdatadatafan/datasets-clase/main/car_fuel_efficiency.csv

 

Or just open it with your browser and click "Save as...".

Now read it with Pandas.
Q2. Records count

How many records are in the dataset?

    4704
    8704
    9704
    17704

Q3. Fuel types

How many fuel types are presented in the dataset?

    1
    2
    3
    4

Q4. Missing values

How many columns in the dataset have missing values?

    0
    1
    2
    3
    4

Q5. Max fuel efficiency

What's the maximum fuel efficiency of cars from Asia?

    13.75
    23.75
    33.75
    43.75

Q6. Median value of horsepower

    Find the median value of the horsepower column in the dataset.
    Next, calculate the most frequent value of the same horsepower column.
    Use the fillna method to fill the missing values in the horsepower column with the most frequent value from the previous step.
    Now, calculate the median value of horsepower once again.

Has it changed?

    Yes, it increased
    Yes, it decreased
    No

Q7. Sum of weights

    Select all the cars from Asia
    Select only columns vehicle_weight and model_year
    Select the first 7 values
    Get the underlying NumPy array. Let's call it X.
    Compute matrix-matrix multiplication between the transpose of X and X. To get the transpose, use X.T. Let's call the result XTX.
    Invert XTX.
    Create an array y with values [1100, 1300, 800, 900, 1000, 1100, 1200].
    Multiply the inverse of XTX with the transpose of X, and then multiply the result by y. Call the result w.
    What's the sum of all the elements of the result?

    Note: You just implemented linear regression. We'll talk about it in the next lesson.

    0.051
    0.51
    5.1
    51
