# -*- coding: utf-8 -*-
"""NumPy UltraQuick Tutorial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/168AvyhVVgbbwATrbHnvpMOKbWSD4VR0e
"""

#@title Copyright 2020 Google LLC. Double-click here for license information.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from google.colab import drive
drive.mount('/content/gdrive')

"""# NumPy UltraQuick Tutorial

NumPy is a Python library for creating and manipulating vectors and matrices. This Colab is not an exhaustive tutorial on NumPy.  Rather, this Colab teaches you just enough to use NumPy in the Colab exercises of Machine Learning Crash Course.

## About Colabs

Machine Learning Crash Course uses Colaboratories (**Colabs**) for all programming exercises. Colab is Google's implementation of [Jupyter Notebook](https://jupyter.org/). Like all Jupyter Notebooks, a Colab consists of two kinds of components:

  * **Text cells**, which contain explanations. You are currently reading a text cell.
  * **Code cells**, which contain Python code for you to run. Code cells have a light gray background.

You *read* the text cells and *run* the code cells.

### Running code cells

You must run code cells in order. In other words, you may only run a code cell once all the code cells preceding it have already been run. 

To run a code cell:

  1. Place the cursor anywhere inside the [ ] area at the top left of a code cell. The area inside the [ ] will display an arrow.
  2. Click the arrow.

Alternatively, you may invoke **Runtime->Run all**. Note, though, that some of the code cells will fail because not all the coding is complete. (You'll complete the coding as part of the exercise.)

### If you see errors...

The most common reasons for seeing code cell errors are as follows:

  * You didn't run *all* of the code cells preceding the current code cell.
  * If the code cell is labeled as a **Task**, then:
    *  You haven't yet written the code that implements the task.
    *  You did write the code, but the code contained errors.

## Import NumPy module

Run the following code cell to import the NumPy module:
"""

import numpy as np

"""## Populate arrays with specific numbers

Call `np.array` to create a NumPy matrix with your own hand-picked values. For example, the following call to `np.array` creates an 8-element vector:
"""

one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

"""You can also use `np.array` to create a two-dimensional matrix. To create a two-dimensional matrix, specify an extra layer of square brackets. For example, the following call creates a 3x2 matrix:"""

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

"""To populate a matrix with all zeroes, call `np.zeros`. To populate a matrix with all ones, call `np.ones`.

## Populate arrays with sequences of numbers

You can populate an array with a sequence of numbers:
"""

sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

"""Notice that `np.arange` generates a sequence that includes the lower bound (5) but not the upper bound (12).

## Populate arrays with random numbers

NumPy provides various functions to populate matrices with random numbers across certain ranges. For example, `np.random.randint` generates random integers between a low and high value. The following call populates a 6-element vector with random integers between 50 and 100.
"""

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

"""Note that the highest generated integer `np.random.randint` is one less than the `high` argument.

To create random floating-point values between 0.0 and 1.0, call `np.random.random`. For example:
"""

random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1)

"""## Mathematical Operations on NumPy Operands

If you want to add or subtract two vectors or matrices, linear algebra requires that the two operands have the same dimensions. Furthermore, if you want to multiply two vectors or matrices, linear algebra imposes strict rules on the dimensional compatibility of operands. Fortunately, NumPy uses a trick called [**broadcasting**](https://developers.google.com/machine-learning/glossary/#broadcasting) to virtually expand the smaller operand to dimensions compatible for linear algebra. For example, the following operation uses broadcasting to add 2.0 to the value of every item in the vector created in the previous code cell:
"""

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

"""The following operation also relies on broadcasting to multiply each cell in a vector by 3:"""

random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

"""## Task 1: Create a Linear Dataset

Your goal is to create a simple dataset consisting of a single feature and a label as follows:

1. Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named `feature`.
2. Assign 15 values to a NumPy array named `label` such that:

```
   label = (3)(feature) + 4
```
For example, the first value for `label` should be:

```
  label = (3)(6) + 4 = 22
 ```
"""

feature = ? # write your code here
print(feature)
label = ?   # write your code here
print(label)

#@title Double-click to see a possible solution to Task 1.
feature = np.arange(6, 21)
print(feature)
label = (feature * 3) + 4
print(label)

"""## Task 2: Add Some Noise to the Dataset

To make your dataset a little more realistic, insert a little random noise into each element of the `label` array you already created. To be more precise, modify each value assigned to `label` by adding a *different* random floating-point value between -2 and +2. 

Don't rely on broadcasting. Instead, create a `noise` array having the same dimension as `label`.
"""

noise = ?    # write your code here
print(noise)
label = ?    # write your code here
print(label)

#@title Double-click to see a possible solution to Task 2.

noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise 
print(label)
