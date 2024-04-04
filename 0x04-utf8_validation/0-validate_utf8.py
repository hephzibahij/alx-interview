#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading 1s in the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # Invalid UTF-8 start byte
            if num_bytes == 0:
                continue

            # Single byte characters are valid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False

        # Decrement the number of bytes remaining in the current character
        num_bytes -= 1

    # All bytes have been processed and no incomplete characters are left
    return num_bytes == 0
