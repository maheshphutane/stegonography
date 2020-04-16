from PIL import Image
import stepic

def encode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img)

    data = input("Enter data to be encoded : ")

    if (len(data) == 0):
        raise ValueError('Data is empty')
    
    #converting string to bytes format
    
    data1 = bytes(data, encoding="ascii")
    
    im1 = stepic.encode(image, data1)

    im1.save( input("Enter the name of new image:- "))


def decode():
    img = input("Enter image name(with extension):- ")
    image = Image.open(img)

    data1 = stepic.decode(image)
   
    return data1



def main():

    a = int(input(":: Welcome to Steganography ::\n"
                  "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()

    elif (a == 2):
        print("Decoded word- " + decode())
    else:
        raise Exception("Enter correct input")

    # Driver Code


if __name__ == '__main__':
    # Calling main function
    main()
