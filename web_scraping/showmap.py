import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = " ".join(sys.argv[1:])
    print(address)
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.openstreetmap.org/search?query=' + address)