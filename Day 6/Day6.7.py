def DefangAddress(Address):
    NewAddress = ""
    SplitAddress = Address.split(".")
    Separator = " [.]"
    NewAddress = Separator.join(SplitAddress)
    print(SplitAddress[0])
    return NewAddress

IpAddress = DefangAddress("55.33.22.11")
print(IpAddress)
