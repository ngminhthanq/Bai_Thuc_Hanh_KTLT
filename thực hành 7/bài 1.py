print("Nguyen Minh Thắng","nMSSV: 235752021610097")
input_file = open('C:/Users/DELL Inc/OneDrive - vinhuni.edu.vn/Tài liệu/vd.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while (l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
