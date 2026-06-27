# ============================================
# Number Guessing Game (Magic Math Trick)
# Author: Dhiraj Kumar
# ============================================

import time

def pause(seconds=2):
    time.sleep(seconds)

print("=" * 55)
print("        🎩 Welcome to the Magic Number Game 🎩")
print("=" * 55)

print("\nThink of ANY whole number.")
input("Once you've chosen a number, press Enter...")

print("\nFollow these steps carefully.\n")

steps = [
    "1. Multiply your number by 2.",
    "2. Add 10.",
    "3. Divide the result by 2.",
    "4. Subtract the original number you first thought of."
]

for step in steps:
    print(step)
    input("Press Enter after completing this step...")

print("\n🔮 Reading your mind...")
pause(1)
print("✨ Analyzing your thoughts...")
pause(1)
print("🧠 Detecting your secret number...")
pause(2)

print("\n🎉 Your final answer is...")
pause(1)
print("""
███████╗
██╔════╝
███████╗
╚════██║
███████║
╚══════╝
""")

print("✨ The answer is: 5 ✨")

print("\nDid I guess correctly? 😄")

choice = input("Enter (Y/N): ").strip().lower()

if choice == "y":
    print("\n🎩 Magic never lies!")
else:
    print("\n😄 Double-check the steps and try again.")

print("\nThanks for playing!")
