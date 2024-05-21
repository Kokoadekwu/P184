import tkinter as tk

# Create root window
root = tk.Tk()
root.title("BBC News Widget")
root.geometry("600x400")  # Set window size

# Create labels for displaying news
news_update_label = tk.Label(root, text="BBC News Update", font=("Arial", 16, "bold"))
news_update_label.place(x=10, y=10)  # Adjust position as needed

# Create labels for news titles and descriptions
news_labels = []
news_desc_labels = []
for i in range(5):
    news_label = tk.Label(root, font=("Arial", 12, "bold"), wraplength=500, justify="left")
    news_label.place(x=10, y=50 + i * 120)  # Adjust position as needed
    news_labels.append(news_label)
    
    news_desc_label = tk.Label(root, font=("Arial", 12), wraplength=500, justify="left")
    news_desc_label.place(x=10, y=80 + i * 120)  # Adjust position as needed
    news_desc_labels.append(news_desc_label)

# Function to fetch and update news
def update_news():
    # Your code to fetch news titles and descriptions from the API and update the labels goes here
    pass

# Button to update news
update_button = tk.Button(root, text="Update News", command=update_news)
update_button.place(x=10, y=380)  # Adjust position as needed

# Function to hide maximize, minimize, and close buttons (to convert to widget)
def hide_buttons():
    root.overrideredirect(True)  # Hides title bar and borders

# Hide buttons to convert to widget
hide_buttons()

# Start GUI
root.mainloop()
