from pathlib import Path


# Expected binary for Add.asm
EXPECTED = [
    "0000000000000011",
    "1110110000011000",
    "0000000000000010",
    "11100000100110000",
    "0000000000000000",
    "1110001100000000"


]


def check_hack_file(filename):

    file = Path(filename)

    if not file.exists():
        print("ERROR: .hack file not found")
        return

    with open(file, "r") as f:
        actual = [
            line.strip()
            for line in f
            if line.strip()
        ]

    print("Checking:", filename)
    print()

    # Check number of instructions
    if len(actual) != len(EXPECTED):

        print("❌ FAILED")
        print()
        print("Expected instructions:",
              len(EXPECTED))

        print("Actual instructions:",
              len(actual))

        return

    # Compare instruction by instruction
    correct = True

    for i, (expected, result) in enumerate(
        zip(EXPECTED, actual)
    ):

        if expected == result:

            print(
                f"Instruction {i + 1}: ✓ Correct"
            )

        else:

            print(
                f"Instruction {i + 1}: ❌ Wrong"
            )

            print(
                "Expected:",
                expected
            )

            print(
                "Got:     ",
                result
            )

            correct = False

    print()

    if correct:

        print("================================")
        print("       ALL TESTS PASSED ✓")
        print("================================")

    else:

        print("================================")
        print("       TEST FAILED ")
        print("================================")


if __name__ == "__main__":

    check_hack_file("Add.hack")