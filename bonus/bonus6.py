contents = ["All good things end",
            "This is the last resort",
            "Get in my belly"]
filenames = ['dox.txt', 'report.txt', 'presentation.txt']
for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)

