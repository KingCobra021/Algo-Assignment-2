'''

Arshia Mortazavinezhad 100860353

'''

try:
    from time import sleep
    import pygame
    sound = True
except ImportError:
    sound = False

step_counter = 0

if sound:
    pygame.mixer.init()
    sound = pygame.mixer.Sound('ding-sound-effect_1.mp3')
    channel = pygame.mixer.Channel(0)



def sound_play():
    global sound
    if sound:
        channel.play(sound)
        sleep(1)
        channel.stop()
        sleep(0.2)


def Sort(ID_List):
    global step_counter

    if len(ID_List) > 1:

        print("\033[38;2;255;165;0m" + f"Start: {ID_List}" + "\033[0m")
        print("-" * 8)
        sleep(0.5)
        Middle = len(ID_List) // 2  # finds the middle of the list
        print(
            "\033[94m" + f"take the middel of the list and break it into two\n" + "\033[0m" + "\033[38;5;213m" + f"\nMiddle = index {Middle}\n" + "\033[0m")
        Left = ID_List[:Middle]  # takes the left side of the list
        print("Left =", Left, "\n")
        Right = ID_List[Middle:]  # takes the right side of the list
        sleep(0.5)
        print("Right =", Right, "\n")
        print("-" * 8)

        sleep(0.5)

        #
        Sort(Left)
        # sort left and right side of the list individually using the same algorithm
        Sort(Right)
        #

        i = j = k = 0
        print("Left =", Left, "\n")
        print("Right =", Right, "\n")

        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                step_counter += 1
                print(
                    "\033[93m" + f"step {step_counter}:" + "\033[0m" + "\033[94m" + f"\nMerging {Left[i]} from Left into main list" + "\033[0m")
                print(Left[i], "<=", Right[j])
                print("\033[91m" + "don't swap left and right" + "\033[0m")
                print("-" * 8)
                sleep(0.5)
                ID_List[k] = Left[i]
                i += 1
            else:
                step_counter += 1
                print("\033[93m" + f"step {step_counter}:" + "\033[0m" + "\033[94m" + f"\nMerging {Right[j]} from Right into main list" + "\033[0m")
                ID_List[k] = Right[j]
                print(Left[i], ">", Right[j])
                print("\033[92m" + "swap left and right" + "\033[0m")
                print("-" * 8)
                sound_play()
                j += 1

            k += 1

        # Copy the remaining elements of Left, if there are any
        while i < len(Left):
            ID_List[k] = Left[i]
            i += 1
            k += 1

        # Copy the remaining elements of Right, if there are any
        while j < len(Right):
            ID_List[k] = Right[j]
            j += 1
            k += 1

    return ID_List


if __name__ == '__main__':
    input_array =[]
    while True:
        try:
            temp = int(input("Enter the array elements seperated by space enter any negative number when done: "))
            if temp < 0:
                break
            else:
                input_array.append(temp)
        except ValueError:
            break

    temp = input_array.copy()
    Sort(input_array)
    print("Original List:\n", temp)
    print("Final List:\n", input_array)
    sleep(10)
