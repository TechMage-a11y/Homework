trees = "Birch Acacia Oak Cedar"
st = ""
for f in trees:
    if f in " ":
        if st:
            print(st)
            st = ""
    else:
        st += f
if st:
    print(st)