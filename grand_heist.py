from cs1robots import *
from cs1media import *
from cs1graphics import *
import math

create_world()
hubo = Robot() 


# --- Global Scope Variable (Phase 4 Constraint) ---
blueprints_generated = 0

# --- Phase 1: The Vault Navigator ---
# Feel free to define your Hubo helper functions (turn_right, etc.) above this function.

def count_beepers(robot):
    beeper_number = 0
    while robot.on_beeper():
        robot.pick_beeper()
        beeper_number += 1
    return beeper_number

def face_north(robot):
    while not robot.facing_north():
        robot.turn_left()

def face_south(robot):
    while not robot.facing_north():
        robot.turn_left()
    turn_back(robot)

def face_east(robot):
    while not robot.facing_north():
        robot.turn_left()
    turn_right(robot)

def face_west(robot):
    while not robot.facing_north():
        robot.turn_left()
    robot.turn_left()

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def turn_back(robot):
    for i in range(2):
        robot.turn_left()

def left_is_clear(robot):
    robot.turn_left()
    if robot.front_is_clear():
        turn_right(robot)
        return True
    else:
        turn_right(robot)
        return False

def u_left(robot):
    robot.turn_left()
    robot.move()
    robot.turn_left()

def u_right(robot):
    turn_right(robot)
    robot.move()
    turn_right(robot)
    
def right_is_clear(robot):
    turn_right(robot)
    if robot.front_is_clear():
        robot.turn_left()
        return True
    else:
        robot.turn_left()
        return False
    
def find_orientation(robot):
    if robot.facing_north():
        return "N"
    else:
        robot.turn_left()
        if robot.facing_north():
            turn_right(robot)
            return "E"
        else:
            robot.turn_left()
            if robot.facing_north():
                turn_back(robot)
                return "S"
            else:
                robot.turn_left()
                if robot.facing_north():
                    robot.turn_left()
                    return "W"   

def infiltrate_vault(hubo, target_count):
    """
    Find a pile with exactly 'target_count' beepers.
    Pick them up, face North, drop one marker, and break.
    If the pile doesn't match, put them back, continue searching.
    NO global variables for Hubo's state.
    """

    face_south(hubo)
    while hubo.front_is_clear():
        hubo.move()
    turn_right(hubo)
    while hubo.front_is_clear():
        hubo.move()
    turn_back(hubo)

    while True:

        if hubo.on_beeper():
            found_direction = find_orientation(hubo)
            found_count = count_beepers(hubo)
            if found_count == target_count:
                face_north(hubo)
                hubo.drop_beeper()
                return "Target count successfully found!"
            else:
                while hubo.carrying_beepers():
                    hubo.drop_beeper()
                if hubo.front_is_clear():
                    hubo.move()
                    continue
                elif not hubo.front_is_clear() and found_direction == "E":
                    if left_is_clear(hubo):
                        u_left(hubo)
                        continue
                    else:
                        return "Target count not found!"
                elif not hubo.front_is_clear() and found_direction == "W":
                    if right_is_clear(hubo):
                        u_right(hubo)
                        continue
                    else:
                        return "Target count not found!"      
        else:
            found_direction = find_orientation(hubo)
            while hubo.front_is_clear() and not hubo.on_beeper():
                hubo.move()
            if hubo.on_beeper():
                continue
            elif not hubo.front_is_clear():
                if found_direction == "E":
                    if left_is_clear(hubo):
                        u_left(hubo)
                        continue
                    else:
                        return "Target count not found!"
                elif found_direction == "W":
                    if right_is_clear(hubo):
                        u_right(hubo)
                        continue
                    else:
                        return "Target count not found!"

    pass

# --- Phase 2: The Security Feed Decrypter ---
def decrypt_feed(image, key_color, strict_threshold):
    """
    Return a NEW image.
    If Euclidean color distance < strict_threshold -> Grayscale (luma).
    Else -> Invert colors.
    OPTIMIZE FOR SPEED in the inner loop.
    """

    width, height = image.size()

    new_img = create_picture(width, height)

    sqrd_threshold = float(strict_threshold ** 2)

    m, n, o = key_color
    
    for x in range(width):
        for y in range(height):
            r, g, b = image.get(x,y)
            distance = ((r-m)**2) + ((g-n)**2) + ((b-o)**2)

            if distance < sqrd_threshold:
                luma = int(0.213 * r + 0.715 * g + 0.072 * b)
                new_img.set(x, y, (luma, luma, luma))
            else:
                new_r = 255 - r
                new_g = 255 - g
                new_b = 255 - b
                new_img.set(x, y, (new_r, new_g, new_b))

    return new_img

    pass

# --- Phase 3: The Passcode Cracker ---
def crack_passcode(data_sequence):
    """
    1. Extract integers -> filter for primes (optimized sieve/trial division) -> sort descending.
    2. Extract strings -> reverse them -> concatenate into one single string.
    Return a tuple: (sorted_primes_list, final_string)
    """


    integers = []

    for item in data_sequence:
        item_type = type(item)
        if item_type == int:
            integers.append(item)
    
    integers.sort()

    ub = max(integers)
    sqrtn = int(math.sqrt(ub))

    our_list = [2] + list(range(3, ub+1, 2))

    i=0

    while i < len(our_list) and our_list[i] <= sqrtn:
        
        no = our_list[i]

        for j in range(len(our_list)-1, i, -1):
            x = our_list[j]
            if x % no == 0:
                our_list.pop(j)
        
        i += 1

    our_list = set(our_list)

    integers = [x for x in integers if x in our_list]
        
    integers.reverse()

    strings = []

    for item in data_sequence:
        item_type = type(item)
        if item_type == str:
            strings.append(item)

    master_string = []

    for item in strings:
        a = item
        for i in range(len(a)-1, -1, -1):
            master_string.append(a[i])

    master_word = "".join(master_string)

    return (integers, master_word)

    pass

# --- Phase 4: The Escape Blueprint ---
def draw_blueprint(primes, passcode_string):
    """
    Increment global 'blueprints_generated'.
    Create Canvas and Layer.
    Draw Path based on primes: (index * 50, prime_val * 10).
    Draw Text with passcode_string at (100, 100).
    Rotate the whole layer 45 degrees.
    """

    global blueprints_generated

    main_canvas = Canvas(400,400)
    main_canvas.setBackgroundColor('light blue')
    main_canvas.setTitle('Main Background Canvas')

    main_layer = Layer()

    main_canvas.add(main_layer)

    points_list = []

    i = 0

    for i in range(len(primes)):
        p =  primes[i]
        m = i * 50
        n = p * 10
        point = Point(m,n)

        points_list.append(point)

    path = Path(*points_list)

    main_layer.add(path)

    text = Text(passcode_string)
    text.move(100,100)

    path.rotate(45)

    main_layer.add(text)

    blueprints_generated += 1

    pass

# --- Main Execution Block ---
if __name__ == "__main__":
    print("Initiating Grand Heist Protocol...\n")
    
    # 1. Parse raw_color into a tuple of integers
    raw_color = input("Enter the security key color (R,G,B) [e.g., 0,255,0]: ")
    color_parts = raw_color.split(',')
    key_color = (int(color_parts[0]), int(color_parts[1]), int(color_parts[2]))
    
    # 2. Phase 1 Setup & Execution
    # Hubo is already dropped into the world at the top of your script!
    if hubo.carries_beepers():
        hubo.drop_beeper() # Drop a test beeper to ensure the world isn't empty
    print("Phase 1: Searching for Vault...")
    infiltrate_vault(hubo, 5) # Let's say 5 is our target count
    
    # 3. Phase 2 Setup & Execution
    print("Phase 2: Decrypting Security Feed...")
    # Assuming you have a test photo in your folder named 'vault.jpg'
    try:
        raw_feed = load_picture("vault.jpg") 
        decrypted_img = decrypt_feed(raw_feed, key_color, 100)
        decrypted_img.show()
    except Exception as e:
        print("Skipping Phase 2 (No test image found).")
    
    # 4. Phase 3 Setup & Execution
    print("Phase 3: Cracking Passcode...")
    test_sequence = [14, "tcejorp", (1, 2), 7, 23, "looc", 8, 97, "101SC"]
    primes, passcode = crack_passcode(test_sequence)
    print(f"Decrypted Data -> Primes: {primes} | Passcode: {passcode}")
    
    # 5. Phase 4 Execution
    print("Phase 4: Drawing Escape Blueprint...")
    draw_blueprint(primes, passcode)
    
    print(f"\nHeist complete. Blueprints generated: {blueprints_generated}")