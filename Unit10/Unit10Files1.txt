from pathlib import Path

file_path = Path("test123.txt")
test_file = file_path.open()
test_file_content = test_file.read()


print(test_file_content)
test_file.close()


appended_text = "Python is the best!"
test_file = open(file_path, 'a')
test_file.write(appended_text)
test_file.close()

test_file = open(file_path)
new_content = test_file.read()

print(new_content)
