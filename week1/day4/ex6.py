def make_shirt(size="large", message="I love Python"):
    print("The size of the shirt is", size,
          "and the text is", message)


make_shirt()
make_shirt("medium")
make_shirt("small", "Hello World")

# Bonus: keyword arguments
make_shirt(size="large", message="Python is amazing")