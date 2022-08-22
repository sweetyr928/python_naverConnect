guest_book ="""김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

f = open("guestbook.txt", 'w')
f.write(guest_book)
f.close()

f = open("guestbook.txt", 'r')
read = f.read()
for line in fhand:
    line = line.rstrip()
split = read.split(",")
split = split.rstrip()
a=split
print(a)

# for line in split:
#     print(line)
