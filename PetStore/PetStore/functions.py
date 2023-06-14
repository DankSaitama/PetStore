def handle_uploaded_file(f):
    with open('C:\Pet_Django\PetStore\media\images'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)