def capitalizer (original, new):
    try:
        with open (original, "r") as original_file, open (new, "w") as new_file:
            for line in original_file:
                caps = line.upper()
                new_file.write (caps)
            print ("Capitalization complete")
            return new_file
            
    except FileNotFoundError:
        print (f"The file /'{original}/' does not exist")
    except Exception as e:
        print (f"An unexpected error {e} occurred")
    finally:
        original_file.close()
        new_file.close()

capitalizer("loremipsum.txt", "try.txt")
file = open("try.txt", "r")
content = file.read()
print (content)