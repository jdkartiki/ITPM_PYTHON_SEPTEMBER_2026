# Library System Project 

books=[]

while True:
    print("=========== LIBRARY SYSTEM ===========")
    print("1. Add Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Available Book")
    print("5. Display All Book")
    print("6. Exit")

    ch=input("Enter Choice from above options :: ")

    # add a book 
    if ch=="1":
        bid=int(input("Enter Book ID :: "))
        bname=input("Enter Book Name :: ")
        author=input("Enter Book Author :: ")

        book={
            "id":bid,
            "name":bname,
            "author":author,
            "issued":False
        }

        books.append(book)
        print("Book Added Successfully ")

    elif ch=="2":
        bid=int(input("Enter Book ID to Issue Book :: "))
        found=False

        for b in books:
            if b["id"]==bid:
                found=True
                if b["issued"]:
                    print("Book is Already Issued ")
                else:
                    b["issued"]=True
                    print("Book is Issued Successfully ")
                    break

            if not found:
                print("Book Not Found")

    # return 
    elif ch=="3":
        bid=int(input("Enter Book ID to Issue Book :: "))
        found=False

        for b in books:
            if b["id"]==bid:
                found=True

                if not b["issued"]:
                    print("Book was not Issued")
                else:
                    b["issued"]=False
                    print("Book Returned Successfully ")
                    break

            if not found:
                print("Book Not Found")

    elif ch=="4":
        print("======== Available Books ============") 
        available=False

        for b in books:
            if not b["issued"]:
                print(f" ID :: {b["id"]}\t Name :: {b["name"]}\t Author :: {b["author"]}") 

                available=True

        if not available:
            print("No Available Books") 

    elif ch=="5":
        print("======== BOOKS ===========")

        if len(books)==0:
            print("No Books Found")
        else:
            for b in books:
                status="Issued" if b["issued"] else "Available"
                print(f" ID :: {b["id"]}\t Name :: {b["name"]}\t Author :: {b["author"]}\t Status :: {status}")

    elif ch=="6":
        print("Thank you for Using Our Library")
        break

    else:
        print("Invalid Choice")



 











