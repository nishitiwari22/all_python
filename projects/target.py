import math  # Import the math module for mathematical operations
import random  # Import the random module for generating random numbers
import time  # Import the time module for tracking elapsed time
import pygame  # Import the pygame module for creating games
pygame.init()  # Initialize pygame modules

# Set up the window dimensions
WIDTH, HEIGHT = 800, 600

# Create a window for the game
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")  # Set the window's caption

# Define constants for timing and padding
TARGET_INCREMENT = 400  # Time increment for target appearance (milliseconds)
TARGET_EVENT = pygame.USEREVENT  # Custom event for target creation

TARGET_PADDING = 30  # Padding for target appearance
BG_COLOR = (0, 25, 40)  # Background color
LIVES = 3  # Number of lives before game ends
TOP_BAR_HEIGHT = 50  # Height of the top bar (displaying time, speed, etc.)

# Font for displaying text in the top bar
LABEL_FONT = pygame.font.SysFont("comicsans", 24)

# Define the Target class to represent each aim target in the game
class Target:
    MAX_SIZE = 30  # Maximum size of a target
    GROWTH_RATE = 0.2  # Growth rate for targets (how fast they grow)
    COLOR = 'red'  # Primary color of the target
    SECOND_COLOR = "white"  # Secondary color for the target

    def __init__(self, x, y):
        # Initialize target at a specific (x, y) position
        self.x = x
        self.y = y
        self.size = 0  # Initial size of the target
        self.grow = True  # Flag to indicate if the target is growing

    def update(self):
        # Update the size of the target (grow or shrink)
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False  # Stop growing when reaching the maximum size
        
        if self.grow:
            self.size += self.GROWTH_RATE  # Increase the size
        else:
            self.size -= self.GROWTH_RATE  # Decrease the size

    def draw(self, win):
        # Draw the target using multiple circles with different sizes and colors
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        # Check if a point (x, y) collides with the target
        dis = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return dis <= self.size  # Return True if the point is within the target's size

# Draw the game window and all active targets
def draw(win, targets):
    win.fill(BG_COLOR)  # Fill the background with the specified color

    # Draw each target in the list of targets
    if targets:
        for target in targets:
            target.draw(win)

    pygame.display.update()  # Update the display to show changes

# Format time into minutes:seconds.milliseconds format
def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)  # Milliseconds
    seconds = int(round(secs % 60, 1))  # Seconds
    minutes = int(secs // 60)  # Minutes

    return f"{minutes:02d}:{seconds:02d}.{milli}"  # Return formatted time

# Draw the top bar with time, speed, hits, and remaining lives
def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))  # Draw the top bar
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "white")

    # Calculate speed (targets per second)
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")

    # Display the number of hits and lives remaining
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "white")
    lives_label = LABEL_FONT.render(f"Lives: {misses}", 1, "white")

    # Blit (display) the labels on the top bar
    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (400, 5))
    win.blit(lives_label, (600, 5))

# Display the end screen with final stats
def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill(BG_COLOR)  # Clear the screen and fill it with the background color
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")

    # Calculate speed (targets per second) and accuracy
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")
    accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

    # Display the final stats in the middle of the screen
    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(time_label), 200))
    win.blit(hits_label, (get_middle(time_label), 300))
    win.blit(accuracy_label, (get_middle(time_label), 400))

    pygame.display.update()  # Update the display to show the end screen

    # Wait for the player to quit or press a key to exit
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()  # Quit the game

# Helper function to center a surface horizontally
def get_middle(surface):
    return WIDTH / 2 - surface.get_width() / 2

# Main game loop
def main():
    run = True  # Flag to keep the game running
    targets = []  # List to hold active targets
    clock = pygame.time.Clock()  # Create a clock to control the frame rate

    target_pressed = 0  # Counter for successful target hits
    clicks = 0  # Counter for total clicks
    misses = 0  # Counter for missed targets
    start_time = time.time()  # Record the start time of the game

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)  # Set a timer for new target generation

    while run:
        clock.tick(60)  # Limit the frame rate to 60 FPS
        click = False  # Track if a mouse click occurred
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
        elapsed_time = time.time() - start_time  # Calculate elapsed game time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Exit the game loop if the window is closed
                break

            if event.type == TARGET_EVENT:
                # Generate a random position for the new target
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)  # Create a new target
                targets.append(target)  # Add the new target to the list

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True  # Set the click flag to True when mouse is clicked
                clicks += 1  # Increment the click counter

        # Update and check each target in the game
        for target in targets:
            target.update()  # Update the size of the target

            if target.size <= 0:
                targets.remove(target)  # Remove targets that shrink to size 0
                misses += 1  # Increment the miss counter

            if click and target.collide(*mouse_pos):
                targets.remove(target)  # Remove the target if clicked
                target_pressed += 1  # Increment the hit counter

        if misses >= LIVES:
            end_screen(WIN, elapsed_time, target_pressed, clicks)  # Show the end screen if player loses

        draw(WIN, targets)  # Draw the targets on the window
        draw_top_bar(WIN, elapsed_time, target_pressed, misses)  # Draw the top bar with stats
        pygame.display.update()  # Update the game display

    pygame.quit()  # Quit pygame when the game loop ends

if __name__ == "__main__":
    main()  # Run the main function to start the game
