# Why Duplicate Random Values?
The objective of this post is to generate identical random numbers across Python, MATLAB, C/C++, and Octave. This facilitates the comparison and validation of algorithms or models implemented in various programming languages, ensuring more reliable and reproducible results.

If you find yourself needing to duplicate precisely the same random numbers across different languages, especially with a focus on uniformly distributed random numbers, this repository could be a useful resource for your requirements.

To ensure consistent results, set a fixed seed value for the random number generator across different languages. The following examples demonstrate how to do that:

## Python

Suppose we want to generate ```10``` random numbers from a uniform distribution in Python. Typically, this is achieved using the NumPy library.

```python
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 10 random numbers from a uniform distribution
random_numbers = np.random.rand(10)

# Print the results
print(f"Generated Random Numbers:\n{random_numbers}")
```
This code generates an array of ``10`` random numbers from a uniform distribution between ``0`` (inclusive) and ``1`` (exclusive). The ``np.random.rand`` function in NumPy is commonly used for generating random numbers from a uniform distribution in the specified range. 

The number ``42`` is used as the seed value for the random number generator. The seed value is a starting point for the algorithm that generates random numbers. By using a fixed seed value, you ensure reproducibility, meaning that if you run the code again with the same seed, you'll get the exact same sequence of random numbers.

The specific choice of ``42`` is arbitrary; you could use any integer as a seed value. However, using a well-known number like ``42`` is often done in examples to highlight the concept without any particular significance to the value itself. If you run the code multiple times without changing the seed (``np.random.seed(42)`` in this case), you will actually get the same set of ``10`` random numbers each time. 

```
Generated Random Numbers:
[0.37454012 0.95071431 0.73199394 0.59865848 0.15601864 0.15599452 0.05808361 0.86617615 0.60111501 0.70807258]
````

## MATLAB
To replicate identical values in MATLAB, execute the following commands:

```Matlab
% Set seed for reproducibility
rng(42, 'twister');

% Generate 10 random numbers from a uniform distribution
random_numbers = rand(1, 10);

% Display the results
disp('Generated Random Numbers:');
disp(random_numbers);
```

Output: 
```
Generated Random Numbers:
0.3745    0.9507    0.7320    0.5987    0.1560    0.1560    0.0581    0.8662    0.6011    0.7081
````

In MATLAB, ``twister`` refers to the Mersenne Twister algorithm (mt19937ar), which is a widely used pseudo-random number generator. The Mersenne Twister is known for its long period ``(2^19937 - 1)`` and excellent statistical properties, making it suitable for various applications. Note that when we use ``rng('default')`` in MATLAB, the random number generator is configured to use the Mersenne Twister algorithm, with the seed set to ``0`` by default.

## C/C++
To get identical values in C/C++, run the following function:

```C++
// Modified based on answers from a Stack Overflow post (https://stackoverflow.com/questions/24199376/matlab-rand-and-c-rand)
// Executed with GCC version 13.2.0

#include <iostream>
#include <vector>
#include <random>

// Function to generate a random value using a given random number generator and distribution
float generateRandomValue(std::mt19937& rng, std::uniform_real_distribution<float>& urd) {
    return urd(rng);
}

// Function to skip alternate values in the random number sequence
void skipAlternateValues(std::mt19937& rng) {
    rng();  // skip alternate values
}

int main() {
    // Set the seed to a specific value (e.g., 42)
    unsigned int seed = 42;
    std::mt19937 rng(seed);  // Initialize the Mersenne Twister random number generator with the specified seed

    std::uniform_real_distribution<float> urd(0, 1);  // Create a uniform real distribution between 0 and 1

    std::vector<float> random_numbers;  // Vector to store generated random numbers

    // Generate 10 random numbers
    for (int i = 0; i < 10; ++i) {
        float a = generateRandomValue(rng, urd);  // Generate a random number
        random_numbers.push_back(a);  // Add the random number to the vector

        skipAlternateValues(rng);  // Skip alternate values in the random number sequence
    }

    // Print the generated random vector
    std::cout << "Generated Random Numbers: ";
    for (const auto& value : random_numbers) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    return 0;
}

```
Output:
```
Generated Random Numbers:
0.37454   0.950714   0.731994   0.598659   0.156019   0.155995   0.0580836   0.866176   0.601115   0.708073
```
Here, we utilize the ``skipAlternateValues`` function to skip every other value in the random number sequence. This is accomplished by advancing the internal state of the generator. This approach, involving the omission of every other value following each call to the random number generating function, proves beneficial for replicating results in both MATLAB and Python.

## Octave
In Octave, things are a bit tricky. Octave uses a generator different from MATLAB. According to [Octave's documentation](https://octave.sourceforge.io/octave/function/rand.html), the default generator is initialized from /dev/urandom if available; otherwise, it uses CPU time, wall clock time, and the current fraction of a second.

Various attempts have been made to address this issue, and among the suggested solutions is to force Octave to initialize the Mersenne Twister random number generator's seed approach. As outlined in this [Octave wiki](https://wiki.octave.org/User:Markuman) and discussed in this [Stack Overflow post](https://stackoverflow.com/questions/71845642/rngdefault-for-rand-function-in-matlab-vs-octave), the recommended step is to call the following function before using the ``rand`` command: 

```Octave
function ret = twister_seed(SEED=0)
    % Function to initialize the Mersenne Twister random number generator seed
    % Tested with GNU Octave, version 8.4.0
    % Input:
    %   - SEED: Seed value for the generator (default is 0)
    % Output:
    %   - ret: 625-element column vector representing the generator's state

    ret = uint32(zeros(625,1));  % Initialize ret as a column vector of 625 zeros
    ret(1) = SEED;  % Set the first element of ret to the provided SEED value

    for N = 1:623
        % Initialize generator
        % bit-xor (right shift by 30 bits)
        ans = uint64(1812433253)*uint64(bitxor(ret(N), bitshift(ret(N), -30))) + N;
        
        % Ensure the result is a uint32 and store it in ret
        ret(N+1) = uint32(bitand(ans, uint64(intmax('uint32'))));  % Untempered numbers
    endfor

    ret(end) = 1;  % Set the last element of ret to 1
endfunction

```
To generate the numbers, we execute:

```Octave
% Set the twister generator with a specific seed (42)
rand('twister', twister_seed(42));

% Generate an array of 10 random numbers
random_numbers = rand(1, 10);

% Display the generated random numbers
disp('Generated Random Numbers:');
disp(random_numbers);
```
Output:
```
Generated Random Numbers:
0.374540   0.950714   0.731994   0.598658   0.156019   0.155995   0.058084   0.866176   0.601115   0.708073
```







