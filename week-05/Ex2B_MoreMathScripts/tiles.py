# Calculate the total number of tile boxes needed for a room.
# Each tile is 1 foot by 1 foot, and each box contains 12 tiles.
# Buy 10% extra tiles for breakage and mistakes.

from math import ceil

length = float(input("Enter the room's length (feet): "))
width = float(input("Enter the room's width (feet): "))

room_area = length * width

total_tiles_needed = room_area * 1.10

total_boxes = ceil(total_tiles_needed / 12)

print(f"For a {length} by {width} feet room, you need {total_boxes} boxes of tiles.")