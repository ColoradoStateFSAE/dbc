files = [
    "haltech",
    "tcs",
    "swc",
    "acc",
    "display"
]

for filename in files:
    output = open(f"src/{filename}/{filename}_aliases.h", "w+")

    print("#pragma once", file=output)
    print(f"#include \"{filename}.h\"\n", file=output)

    for line in open(f"src/{filename}/{filename}.h"):
        if(line.startswith("#define")):
            line = line.split(" ")
            if(len(line) == 3):
                line[2] = line[1]
                line[1] = line[1].lower()
                line = ' '.join(line)
                print(line, file=output)
