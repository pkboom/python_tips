def format(comment):
    result = ""
    count = 0

    for i in range(len(comment)):
        result += comment[i]

        if count > 60 and comment[i] == " ":
            result += "\n"
            count = 0
        else:
            count += 1

    return result


comment = input("Enter comment: ")

formatted_comment = format(comment.strip())

print(f"\nResult: \n{formatted_comment.strip()}")
