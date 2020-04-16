from PIL import Image
import stepic


# Encode data into image
def encode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img)

    data = input("Enter data to be encoded : ")

    if (len(data) == 0):
        raise ValueError('Data is empty')
    res = ''.join(format(ord(i), 'b') for i in data)
    im1 = stepic.encode(image, res)

    im1.save( input("Enter the name of new image(: "))


# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) :")
    image = Image.open(img)

    data1 = stepic.decode(image)
    print(data1)
    return data1

        # Main Function


def main():
    l=b'Mahesh'
    print(l)
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