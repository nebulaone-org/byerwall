import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import os
import subprocess

def add_entry():
    def save_entry():
        name = name_var.get()
        port_range = port_var.get()
        protocol = protocol_var.get()

        if not (name and port_range and protocol):
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        entries_list.insert("", "end", values=(name, port_range, protocol))
        add_window.destroy()

    def add_popular_entry():
        def select_entry():
            selected = popular_entries_box.get(popular_entries_box.curselection())
            name, port, protocol = popular_entries[selected]
            name_var.set(name)
            port_var.set(port)
            protocol_var.set(protocol)
            popular_window.destroy()

        popular_window = tk.Toplevel(add_window)
        popular_window.title("Add from Popular Entries")
        popular_window.geometry("300x400")
        popular_window.resizable(False, False)

        popular_entries_box = tk.Listbox(popular_window)
        popular_entries_box.pack(fill="both", expand=True, padx=10, pady=10)

        for entry in popular_entries:
            popular_entries_box.insert(tk.END, entry)

        tk.Button(popular_window, text="Select", command=select_entry).pack(pady=10)

    popular_entries = {
        "RDP": ("RDP", "3389", "tcp"),
        "Minecraft": ("Minecraft", "25565", "both"),
        "Arma": ("Arma", "2302-2306", "both"),
        "HTTP": ("HTTP", "80", "tcp"),
        "HTTPS": ("HTTPS", "443", "tcp"),
        "FTP": ("FTP", "21", "tcp"),
        "SMTP": ("SMTP", "25", "tcp"),
        "DNS": ("DNS", "53", "udp"),
        "MySQL": ("MySQL", "3306", "tcp"),
        "PostgreSQL": ("PostgreSQL", "5432", "tcp")
    }

    add_window = tk.Toplevel(root)
    add_window.title("Add Entry")
    add_window.geometry("400x300")
    add_window.resizable(False, False)

    tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    name_var = tk.StringVar()
    tk.Entry(add_window, textvariable=name_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Port/Port Range:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    port_var = tk.StringVar()
    tk.Entry(add_window, textvariable=port_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Protocol:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    protocol_var = tk.StringVar(value="tcp")
    ttk.Combobox(add_window, textvariable=protocol_var, values=["tcp", "udp", "both"]).grid(row=2, column=1, padx=10, pady=10)

    tk.Button(add_window, text="Save", command=save_entry).grid(row=3, column=0, pady=20)
    tk.Button(add_window, text="Add from Popular Entries", command=add_popular_entry).grid(row=3, column=1, pady=20)

def remove_entry():
    selected_item = entries_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "No entry selected.")
        return

    for item in selected_item:
        entries_list.delete(item)

def generate_config(run_after=False):
    def save_config():
        server_addr = server_addr_var.get()
        server_port = server_port_var.get()
        if not (server_addr and server_port):
            messagebox.showerror("Error", "Server address and port must be filled out.")
            return

        config_name = f"{random.randint(1000, 9999)}.toml"
        with open(config_name, "w") as f:
            f.write(f"serverAddr = \"{server_addr}\"\n")
            f.write(f"serverPort = {server_port}\n\n")

            for entry in entries_list.get_children():
                name, port_range, protocol = entries_list.item(entry, "values")

                ports = []
                if "-" in port_range:
                    start, end = map(int, port_range.split("-"))
                    ports = list(range(start, end + 1))
                else:
                    ports = [int(port_range)]

                for port in ports:
                    if protocol in ["tcp", "udp"]:
                        f.write(f"[[proxies]]\nname = \"{name}-{protocol}-{port}\"\n")
                        f.write(f"type = \"{protocol}\"\n")
                        f.write(f"localIP = \"127.0.0.1\"\n")
                        f.write(f"localPort = {port}\n")
                        f.write(f"remotePort = {port}\n\n")
                    elif protocol == "both":
                        f.write(f"[[proxies]]\nname = \"{name}-tcp-{port}\"\n")
                        f.write(f"type = \"tcp\"\n")
                        f.write(f"localIP = \"127.0.0.1\"\n")
                        f.write(f"localPort = {port}\n")
                        f.write(f"remotePort = {port}\n\n")

                        f.write(f"[[proxies]]\nname = \"{name}-udp-{port}\"\n")
                        f.write(f"type = \"udp\"\n")
                        f.write(f"localIP = \"127.0.0.1\"\n")
                        f.write(f"localPort = {port}\n")
                        f.write(f"remotePort = {port}\n\n")

        messagebox.showinfo("Success", f"Config file {config_name} generated successfully!")
        generate_window.destroy()

        if run_after:
            frpc_path = os.path.join(os.path.dirname(__file__), "bin_frpc", "frpc")
            output_window = tk.Toplevel(root)
            output_window.title("FRPC Output")
            output_window.geometry("600x400")
            output_window.resizable(False, False)
            output_text = scrolledtext.ScrolledText(output_window, wrap=tk.WORD)
            output_text.pack(fill="both", expand=True)
            try:
                process = subprocess.Popen([frpc_path, "-c", config_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                for line in process.stdout:
                    output_text.insert(tk.END, line)
                    output_text.see(tk.END)
                for line in process.stderr:
                    output_text.insert(tk.END, line)
                    output_text.see(tk.END)
                process.wait()
            except FileNotFoundError:
                messagebox.showerror("Error", "frpc binary not found in bin_frpc folder.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to run frpc: {e}")

    generate_window = tk.Toplevel(root)
    generate_window.title("Generate Config")
    generate_window.geometry("400x200")
    generate_window.resizable(False, False)

    tk.Label(generate_window, text="Server Address:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    server_addr_var = tk.StringVar()
    tk.Entry(generate_window, textvariable=server_addr_var).grid(row=0, column=1, padx=10, pady=10)

    tk.Label(generate_window, text="Server Port:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    server_port_var = tk.StringVar()
    tk.Entry(generate_window, textvariable=server_port_var).grid(row=1, column=1, padx=10, pady=10)

    tk.Button(generate_window, text="Generate", command=save_config).grid(row=2, column=0, columnspan=2, pady=20)

root = tk.Tk()
root.title("ByerWall")
root.geometry("600x400")
root.resizable(False, False)
root.iconbitmap("icon.ico")

frame = tk.Frame(root, borderwidth=5, relief="ridge")
frame.pack(pady=20, fill="both", expand=True)

columns = ("Name", "Port/Port Range", "Protocol")
entries_list = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    entries_list.heading(col, text=col)
    entries_list.column(col, width=150, anchor="center")
entries_list.pack(fill="both", expand=True, side="left", padx=5, pady=5)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=entries_list.yview)
entries_list.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Entry", command=add_entry)
add_button.grid(row=0, column=0, padx=10)

remove_button = tk.Button(button_frame, text="Remove Entry", command=remove_entry)
remove_button.grid(row=0, column=1, padx=10)

generate_button = tk.Button(button_frame, text="Generate Config", command=lambda: generate_config(run_after=False))
generate_button.grid(row=0, column=2, padx=10)

run_button = tk.Button(button_frame, text="Generate & Run", command=lambda: generate_config(run_after=True))
run_button.grid(row=0, column=3, padx=10)

root.mainloop()
