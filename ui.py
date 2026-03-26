from path import resource_path  # Utility function to correctly load files (like icon) in both .py and .exe environments
import threading  # Used to run background tasks without freezing the UI
import tkinter as tk  # Tkinter library for building the graphical user interface
from ai_module import summarize_local, summarize_online  # Import AI summarization functions
import scraper  # Import the scraping module


def start_ui():
    # ---------- MAIN WINDOW SETUP ----------

    root = tk.Tk()  # Create the main application window
    root.title("AI Web Scraper")  # Set window title
    root.geometry("1000x650")  # Set window size (width x height)

    # Set application icon (works for both .py and .exe using resource_path)
    root.iconbitmap(resource_path("icon.ico"))

    # Set background color of main window
    root.configure(bg="#2b2b3c")


    # ---------- FUNCTIONS (LOGIC) ----------

    # Function to safely update the UI with results (runs in main thread)
    def update_result(result):
        result_text.config(state="normal")  # Enable editing temporarily
        result_text.delete("1.0", tk.END)  # Clear previous content
        result_text.insert(tk.END, result)  # Insert new result text
        result_text.config(state="disabled")  # Disable editing again
        go_button.config(state="normal")  # Re-enable the "Run" button


    # Function that performs the heavy work (scraping + AI)
    # Runs in a separate thread to prevent UI freezing
    def run_task(url, mode, api_key):

        # Scrape the website content
        raw_text = scraper.scrape_website(url)

        # Decide what to do based on selected mode
        if mode == "raw":
            result = raw_text

        elif mode == "local_ai":
            result = summarize_local(raw_text)

        elif mode == "online_ai":
            if not api_key:
                result = "Error: Please provide an API key."
            else:
                result = summarize_online(raw_text, api_key)

        # Use root.after to safely update UI from main thread
        root.after(0, update_result, result)


    # Function triggered when user clicks the "Run" button
    def on_go():
        go_button.config(state="disabled")  # Disable button to prevent multiple clicks

        # Show loading message
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "🔄 Processing...\n\n")
        result_text.config(state="disabled")

        # Create and start a background thread for processing
        thread = threading.Thread(
            target=run_task,
            args=(url_entry.get(), mode_var.get(), api_entry.get())
        )
        thread.start()


    # ---------- LAYOUT STRUCTURE ----------

    # Left panel (sidebar for inputs)
    left_frame = tk.Frame(root, bg="#1e1e2f", width=300)
    left_frame.pack(side="left", fill="y")

    # Right panel (main content area for results)
    right_frame = tk.Frame(root, bg="#2b2b3c")
    right_frame.pack(side="right", expand=True, fill="both")


    # ---------- SIDEBAR CONTENT ----------

    # App title
    title = tk.Label(
        left_frame,
        text="AI Scraper",
        bg="#1e1e2f",
        fg="white",
        font=("Segoe UI", 16, "bold")
    )
    title.pack(pady=20)


    # ---------- URL INPUT ----------

    tk.Label(
        left_frame,
        text="Website URL:",
        bg="#1e1e2f",
        fg="white"
    ).pack(anchor="w", padx=15)

    url_entry = tk.Entry(
        left_frame,
        width=30,
        bg="#2b2b3c",
        fg="white",
        insertbackground="white"  # Cursor color
    )
    url_entry.pack(padx=15, pady=5)


    # ---------- API KEY INPUT ----------

    tk.Label(
        left_frame,
        text="API Key (Online AI):",
        bg="#1e1e2f",
        fg="white"
    ).pack(anchor="w", padx=15, pady=(15, 0))

    api_entry = tk.Entry(
        left_frame,
        width=30,
        bg="#2b2b3c",
        fg="white",
        insertbackground="white"
    )
    api_entry.pack(padx=15, pady=5)


    # ---------- MODE SELECTION ----------

    tk.Label(
        left_frame,
        text="Mode:",
        bg="#1e1e2f",
        fg="white"
    ).pack(anchor="w", padx=15, pady=(15, 0))

    # Variable that stores selected mode
    mode_var = tk.StringVar(value="raw")

    # Radio buttons for selecting operation mode
    tk.Radiobutton(
        left_frame,
        text="Raw",
        variable=mode_var,
        value="raw",
        bg="#1e1e2f",
        fg="white",
        selectcolor="#1e1e2f"
    ).pack(anchor="w", padx=15)

    tk.Radiobutton(
        left_frame,
        text="AI (Local)",
        variable=mode_var,
        value="local_ai",
        bg="#1e1e2f",
        fg="white",
        selectcolor="#1e1e2f"
    ).pack(anchor="w", padx=15)

    tk.Radiobutton(
        left_frame,
        text="AI (Online)",
        variable=mode_var,
        value="online_ai",
        bg="#1e1e2f",
        fg="white",
        selectcolor="#1e1e2f"
    ).pack(anchor="w", padx=15)


    # ---------- RUN BUTTON ----------

    go_button = tk.Button(
        left_frame,
        text="Run",
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        relief="flat",
        command=on_go  # Calls on_go when clicked
    )
    go_button.pack(pady=25, padx=15, fill="x")


    # ---------- RESULT DISPLAY AREA ----------

    result_text = tk.Text(
        right_frame,
        wrap="word",  # Wrap text by words instead of characters
        bg="#2b2b3c",
        fg="white",
        insertbackground="white",
        relief="flat",
        padx=10,
        pady=10
    )
    result_text.pack(expand=True, fill="both")

    # Scrollbar for vertical scrolling
    scrollbar = tk.Scrollbar(
        right_frame,
        command=result_text.yview
    )
    scrollbar.pack(side="right", fill="y")

    # Link scrollbar with text widget
    result_text.config(yscrollcommand=scrollbar.set)

    # Make result text read-only by default
    result_text.config(state="disabled")


    # ---------- START APPLICATION ----------

    root.mainloop()  # Starts the GUI event loop