import tkinter as tk

# Define the colors
colors = {
    "norm_fg": "#f8f8f2",
    "norm_bg": "#282a36",
    "norm_border": "#44475a",
    "sel_fg": "#f8f8f2",
    "sel_bg": "#bd93f9",
    "sel_border": "#bd93f9",
    "status_fg": "#f8f8f2",
    "status_bg": "#282a36",
    "status_border": "#000000",
    "tags_sel_fg": "#f8f8f2",
    "tags_sel_bg": "#bd93f9",
    "tags_sel_border": "#bd93f9",
    "tags_norm_fg": "#f8f8f2",
    "tags_norm_bg": "#282a36",
    "tags_norm_border": "#282a36",
    "info_sel_fg": "#f8f8f2",
    "info_sel_bg": "#282a36",
    "info_sel_border": "#282a36",
    "info_norm_fg": "#f8f8f2",
    "info_norm_bg": "#282a36",
    "info_norm_border": "#282a36"
}

# Create the main window
root = tk.Tk()
root.title("DWM Demo")
root.geometry("400x300")

# Create the bar at the top
bar = tk.Frame(root, bg=colors["status_bg"], height=30)
bar.pack(fill="x")

# Create the status label on the top bar
status_label = tk.Label(bar, text="Demo Status", bg=colors["status_bg"], fg=colors["status_fg"])
status_label.pack(side="right", padx=10, pady=5)

# Create the tags on the top bar
tags_frame = tk.Frame(bar, bg=colors["status_bg"])
tags_frame.pack(side="left", padx=10, pady=5)

tags = [str(i) for i in range(1, 10)]  # List of tags from 1 to 9

def select_tag(tag_number):
    active_window = tag_number % 2 + 1  # Simulate toggling between window 1 and window 2
    update_window_title(active_window)
    update_tag_borders(tag_number)

def update_window_title(active_window):
    window_title = "Window {}".format(active_window)
    root.title(window_title)

def update_tag_borders(selected_tag):
    for tag_label in tag_labels:
        tag_number = tag_label['text']
        if tag_number == selected_tag:
            tag_label.config(relief="solid", bd=1, borderwidth=2, bg=colors["tags_sel_bg"], fg=colors["tags_sel_fg"])
        else:
            tag_label.config(relief="flat", bd=0, bg=colors["tags_norm_bg"], fg=colors["tags_norm_fg"])

tag_labels = []

for tag in tags:
    tag_label = tk.Label(tags_frame, text=tag, bg=colors["tags_norm_bg"], fg=colors["tags_norm_fg"])
    tag_label.pack(side="left", padx=2)

    def select_tag_callback(event, tag_number=int(tag)):
        select_tag(tag_number)

    tag_label.bind("<Button-1>", select_tag_callback)
    tag_labels.append(tag_label)

# Create the window frames
window1 = tk.Frame(root, bg=colors["norm_bg"], bd=2, relief="solid")
window1.pack(fill="both", expand=True, padx=8, pady=8)
window2 = tk.Frame(root, bg=colors["norm_bg"], bd=2, relief="solid")
window2.pack(fill="both", expand=True, padx=8, pady=8)

# Update the initial window title and tag borders
select_tag(1)

# Start the GUI event loop
root.mainloop()

