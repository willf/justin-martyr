# apology-1-grk.md is a markdown file that contains the text of the apology in greek
# apology-1-eng.md is a markdown file that contains the text of the apology in english
# Each has a tile and a text
# The text is dvided into chapters that start with ## 1, ## 2, ## 3, etc
# The script reads the two files and creates a three column markdown table,
# with the chapter number in the first column, the greek text in the second column and the english text in the third column
# for each chapter

# The first rown contains the header


def devide_by_chapters(text):
    # Initialize the chapter number
    chapter = None
    chapters = []
    lines = []
    # look for first chapter
    for line in text:
        if line.startswith("## "):
            chapter = line.split(" ")[1]
            break
    # add lines until next chapter
    for line in text:
        if line.startswith("## "):
            chapters.append((chapter, "".join(lines)))
            lines = []
            chapter = line.split(" ")[1]
        else:
            lines.append(line.strip())
    # add the last chapter
    chapters.append((chapter, "".join(lines)))
    return chapters


print("| Chapter| Ελληνικά | English |")
print("| :-- | :-- | :-- |")
with open("apology-1-grk.md") as f:
    text1 = f.readlines()
    chapters1 = devide_by_chapters(text1)
with open("apology-1-eng.md") as f:
    text2 = f.readlines()
    chapters2 = devide_by_chapters(text2)
for i, chapter in enumerate(chapters1):
    title, text = chapter
    text2 = chapters2[i][1]
    print("| " + title.strip() + " | " + text.strip() + " | " + text2.strip() + " |")
