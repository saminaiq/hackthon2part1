from app.manager import show_menu, handle_choice

def main():
    running = True
    while running:
        show_menu()
        choice = input("Choose an option: ")
        running = handle_choice(choice)

if __name__ == "__main__":
    main()
