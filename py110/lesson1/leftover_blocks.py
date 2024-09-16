# You have a number of building blocks that can be used to build a valid structure. 
# There are certain rules about what determines a valid structure:

# - The building blocks are cubes.
# - The structure is built in layers.
# - The top layer is a single block.
# - A block in an upper layer must be supported by four blocks in a lower layer.
# - A block in a lower layer can support more than one block in an upper layer.
# - You cannot leave gaps between blocks.

# Write a program that, given the number of available blocks, calculates the number 
# of blocks left over after building the tallest possible valid structure.

# Input: number of blocks
# Output: number of blocks left

# Explicit:
# - 1 top block 
# - Each block is supported by 4 blocks
# - Each block can support several blocks
# - No gaps between blocks
# Implicit:
# - Tall = number of layers
# - Valid layer is 

# What if a layer has more blocks than it needs? Either a block
# is the top level block of it supports at least 1 other block

# Take a number as input
# Compute the number of layers we can make
# - Iterate from 1 to the input number:
# - Keep track of the previous layer and check if we have enough blocks
#   to build a new layer
# Compute the number of blocks we need in our layers
# Return the difference between previous and the input

# If the number of blocks is higher than 1
# check if we can build layer n+1: do we have n+1 * n+1 blocks? If yes continue, if no
# compute remaining and return

def calculate_leftover_blocks(blocks):
    if blocks <= 1:
        return 0
    
    layer = 1
    remaining_blocks = blocks - 1
    while remaining_blocks > 0:
        required_blocks = (layer + 1) * (layer + 1) # out of the loop
        if remaining_blocks < required_blocks: # should be the loop condition
            break
        else:
            remaining_blocks -= required_blocks
            layer += 1

    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True