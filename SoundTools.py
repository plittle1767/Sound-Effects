
# Functions to process audio.
# For CS 1400, written by David E. Johnson.
# Function implementations by

# Add your functions below this line
import random

"""For this function we will take the sample audio and reverse it."""
def make_reversed_samples(num_list):
    reversed_num_list = []
    for number in range(len(num_list)-1, -1, -1):
        reversed_num_list.append(num_list[number])
    return reversed_num_list


"""This second function takes the audio and makes it sound louder"""
def make_louder_samples(current_sound, scale):
    louder_list = []
    for number in current_sound:
        louder_list.append(number * scale)
    return louder_list


"""Here we're going to clip the sound. In audio work, a clipped sound is one where, for example, it is too 
loud for the microphone to capture the full range of the signal. This function is approximating that effect"""
def make_clipped_samples(num_list, clip_level_number):
    clipped_list = []
    for number in num_list:
        if -number <= number <= clip_level_number:
            clipped_list.append(number)
        else:
            if number < 0:
                clipped_list.append(-clip_level_number)
            else:
                clipped_list.append(clip_level_number)
    return clipped_list


"""With this function we're going to cause the audio to randomly fluctuate. We can approximate this by adding random 
numbers to the samples."""
def make_noisy_samples(noise_list, new_sound):
    random_list = []
    for number in noise_list:
        random_sound_level = random.randint(-new_sound, new_sound)
        random_list.append(number + random_sound_level)
    return random_list


"""This function was suppose to average an element in the list with the surrounding elements but to be honest I 
couldn't figure it out. I tried my best and spent 6 hours working on this one function but I just couldn't get 
it right."""
def make_smoothed_samples(smoothed_list):
    new_smoothed_list = []
    for number in range(len(smoothed_list)):
        if number == 0:
            new_smoothed_list.append(smoothed_list[0] + smoothed_list[1] // 2)
        if number == -1:
            new_smoothed_list.append(smoothed_list[-2] + smoothed_list[-1] // 2)
        else:
            new_smoothed_list.append((number - 1) + (number + 1) // 3)
    return new_smoothed_list


# You can add small test examples here and see results from running this file instead of the SoundApp
def main():
    print(make_reversed_samples([4, 5, 6]))
    print(make_louder_samples([1, 2, 3], 2))
    print(make_clipped_samples([-5, -1, 2, 5, 10], 4))
    print(make_noisy_samples([5, 3, 1], 5))
    print(make_smoothed_samples([0, 100, 500, 100]))


if __name__ == "__main__":
    main()
