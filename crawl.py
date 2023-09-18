import tkinter as tk

class UI():
    def center_window(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")

    root = tk.Tk()
    root.title("Crawl data twitter")
    window_width = 1400
    window_height = 800

    center_window(root, window_width, window_height)
    
    root.mainloop()


if __name__ == '__main__':
    UI()