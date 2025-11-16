def enhance(input_image, image_enhance, background):
    padding = 1
    width = len(input_image[0])

    padded = [[background] * (width + padding * 2) for _ in range(padding)]
    for row in input_image:
        padded.append([background] * padding + row + [background] * padding)
    padded.extend([[background] * (width + padding * 2) for _ in range(padding)])

    # Process ALL pixels
    output_image = []
    for y in range(len(padded)):
        output_row = []
        for x in range(len(padded[0])):
            temp_binary = ""
            for y_i in [-1, 0, 1]:
                for x_i in [-1, 0, 1]:
                    ny, nx = y + y_i, x + x_i
                    # Use background for out-of-bounds
                    if 0 <= ny < len(padded) and 0 <= nx < len(padded[0]):
                        temp_binary += padded[ny][nx]
                    else:
                        temp_binary += background
            int_number = int(temp_binary, 2)
            output_row.append(image_enhance[int_number])
        output_image.append(output_row)

    # Update background
    if background == "0":
        new_background = image_enhance[0]
    else:
        new_background = image_enhance[511]

    return output_image, new_background


file = open("input.txt")
image_enhance = list(file.readline().strip().replace(".", "0").replace("#", "1"))
file.readline()
input_image = []
for row in file:
    input_image.append(list(row.strip().replace(".", "0").replace("#", "1")))


new_background = "0"
for _ in range(50):
    input_image, new_background = enhance(input_image, image_enhance, new_background)


total = sum(row.count("1") for row in input_image)
print(total)
