class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit_page(self, page):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)

        self.current_page = page
        self.forward_stack.clear()

        print("Visited:", self.current_page)

    def go_back(self):
        if not self.back_stack:
            print("No previous page available.")
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()

        print("Moved Back To:", self.current_page)

    def go_forward(self):
        if not self.forward_stack:
            print("No forward page available.")
            return

        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()

        print("Moved Forward To:", self.current_page)

    def show_current_page(self):
        if self.current_page is None:
            print("No page is currently open.")
        else:
            print("Current Page:", self.current_page)

    def show_history(self):
        print("\nBrowsing History:")

        if not self.back_stack and self.current_page is None:
            print("No browsing history available.")
            return

        for page in reversed(self.back_stack):
            print(page)

        if self.current_page is not None:
            print(self.current_page, "<-- Current Page")


def main():
    browser = Browser()

    while True:
        print("\n===== WEB BROWSER =====")
        print("1. Visit New Page")
        print("2. Back")
        print("3. Forward")
        print("4. Show Current Page")
        print("5. Show Browsing History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            page = input("Enter webpage name or URL: ")
            if page.strip():
                browser.visit_page(page.strip())
            else:
                print("Page name cannot be empty.")

        elif choice == "2":
            browser.go_back()

        elif choice == "3":
            browser.go_forward()

        elif choice == "4":
            browser.show_current_page()

        elif choice == "5":
            browser.show_history()

        elif choice == "6":
            print("Browser closed successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()