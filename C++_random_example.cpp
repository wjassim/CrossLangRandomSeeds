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
