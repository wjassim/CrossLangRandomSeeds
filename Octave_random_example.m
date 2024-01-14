function ret = twister_seed(SEED=0)
    % Modified from https://wiki.octave.org/User:Markuman
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
end



% Set the twister generator with a specific seed (42)
rand('twister', twister_seed(42));

% Generate an array of 10 random numbers
random_numbers = rand(1, 10);

% Display the generated random numbers
disp('Generated Random Numbers:');
disp(random_numbers);

