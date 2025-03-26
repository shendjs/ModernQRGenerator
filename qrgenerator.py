import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import os
from datetime import datetime

# Basic appearance settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ModernQRGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern QR Generator")
        self.root.geometry("900x650")
        self.root.minsize(900, 650)
        
        # Main color and design variables
        self.colors = {
            "bg_light": "#ffffff",
            "bg_dark": "#191919",
            "card_light": "#f7f7f7",
            "card_dark": "#2d2d2d",
            "border_light": "#e0e0e0",
            "border_dark": "#3d3d3d",
            "text_light": "#37352f",
            "text_dark": "#e6e6e6",
            "text_secondary_light": "#6b7280",
            "text_secondary_dark": "#9ca3af",
            "accent": "#0070f3",
            "accent_hover": "#0051a8",
            "success": "#10b981",
            "success_hover": "#059669",
            "error": "#ef4444",
            "error_hover": "#dc2626",
            "warning": "#f59e0b",
            "info": "#3b82f6",
            "button_shadow": "0px 1px 2px rgba(0, 0, 0, 0.05)"
        }
        
        self.current_theme = "light"
        self.fonts = {
            "title": ctk.CTkFont(family="Inter", size=28, weight="bold"),
            "subtitle": ctk.CTkFont(family="Inter", size=16, weight="bold"),
            "body": ctk.CTkFont(family="Inter", size=14),
            "button": ctk.CTkFont(family="Inter", size=14, weight="bold"),
            "small": ctk.CTkFont(family="Inter", size=12),
            "tiny": ctk.CTkFont(family="Inter", size=10)
        }
        
        # Main grid configuration
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Main frame
        self.main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color=self.colors["bg_light"])
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        # Header bar
        self.header = ctk.CTkFrame(self.main_frame, corner_radius=0, fg_color=self.colors["bg_light"], height=60)
        self.header.grid(row=0, column=0, sticky="ew")
        self.header.grid_propagate(False)
        self.header.grid_columnconfigure(0, weight=1)
        self.header.grid_columnconfigure(1, weight=0)
        
        self.title_label = ctk.CTkLabel(
            self.header, 
            text="QR Generator", 
            font=self.fonts["title"],
            text_color=self.colors["text_light"]
        )
        self.title_label.grid(row=0, column=0, padx=(30, 0), pady=(15, 15), sticky="w")
        
        # Enhanced theme switcher
        self.theme_container = ctk.CTkFrame(self.header, fg_color="transparent")
        self.theme_container.grid(row=0, column=1, padx=(0, 30), pady=(15, 15), sticky="e")
        
        # Theme icons
        self.light_icon = ctk.CTkLabel(
            self.theme_container,
            text="☀️",
            font=ctk.CTkFont(family="Inter", size=16),
            width=20
        )
        self.light_icon.grid(row=0, column=0, padx=(0, 5))
        
        self.theme_switch = ctk.CTkSwitch(
            self.theme_container,
            text="",
            command=self.toggle_theme,
            switch_width=46,
            switch_height=24,
            onvalue="dark",
            offvalue="light",
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            progress_color=self.colors["accent"] if self.current_theme == "light" else "#555555"
        )
        self.theme_switch.grid(row=0, column=1, padx=0)
        
        self.dark_icon = ctk.CTkLabel(
            self.theme_container,
            text="🌙",
            font=ctk.CTkFont(family="Inter", size=16),
            width=20
        )
        self.dark_icon.grid(row=0, column=2, padx=(5, 0))
        
        # Content area
        self.content_frame = ctk.CTkFrame(self.main_frame, corner_radius=0, fg_color=self.colors["bg_light"])
        self.content_frame.grid(row=1, column=0, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=3)
        self.content_frame.grid_columnconfigure(1, weight=4)
        self.content_frame.grid_rowconfigure(0, weight=1)
        
        # Left panel - Input and settings
        self.left_panel = ctk.CTkFrame(self.content_frame, corner_radius=15, fg_color=self.colors["card_light"])
        self.left_panel.grid(row=0, column=0, padx=(30, 15), pady=30, sticky="nsew")
        self.left_panel.grid_columnconfigure(0, weight=1)
        self.left_panel.grid_rowconfigure(3, weight=1)
        
        # Data input header
        self.input_header = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.input_header.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="ew")
        self.input_header.grid_columnconfigure(0, weight=1)
        
        self.input_label = ctk.CTkLabel(
            self.input_header, 
            text="Content", 
            font=self.fonts["subtitle"],
            text_color=self.colors["text_light"]
        )
        self.input_label.grid(row=0, column=0, sticky="w")
        
        # Subtitle
        self.input_sublabel = ctk.CTkLabel(
            self.left_panel, 
            text="Enter your text or URL here", 
            font=self.fonts["small"],
            text_color=self.colors["text_light"]
        )
        self.input_sublabel.grid(row=1, column=0, padx=20, pady=(5, 10), sticky="w")
        
        # Text input - enhanced visual design
        self.input_container = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent",
            height=120
        )
        self.input_container.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.input_container.grid_columnconfigure(0, weight=1)
        self.input_container.grid_propagate(False)
        
        self.data_input = ctk.CTkTextbox(
            self.input_container, 
            height=120,
            corner_radius=8,
            border_width=1,
            border_color=self.colors["border_light"],
            font=self.fonts["body"],
            fg_color=self.colors["bg_light"] if self.current_theme == "light" else self.colors["bg_dark"],
        )
        self.data_input.grid(row=0, column=0, sticky="nsew")
        
        # Placeholder (watermark) effect
        self.data_input.insert("0.0", "Write your QR code content here...")
        self.data_input.configure(text_color=self.colors["text_secondary_light"])
        
        # Clear placeholder on focus
        def on_entry_focus_in(event):
            if self.data_input.get("0.0", "end-1c").strip() == "Write your QR code content here...":
                self.data_input.delete("0.0", "end")
                self.data_input.configure(text_color=self.colors["text_light"] if self.current_theme == "light" else self.colors["text_dark"])
        
        # Restore placeholder when losing focus if empty
        def on_entry_focus_out(event):
            if not self.data_input.get("0.0", "end-1c").strip():
                self.data_input.delete("0.0", "end")
                self.data_input.insert("0.0", "Write your QR code content here...")
                self.data_input.configure(text_color=self.colors["text_secondary_light"] if self.current_theme == "light" else self.colors["text_secondary_dark"])
        
        self.data_input.bind("<FocusIn>", on_entry_focus_in)
        self.data_input.bind("<FocusOut>", on_entry_focus_out)
        
        # Settings section
        self.settings_frame = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.settings_frame.grid(row=3, column=0, padx=20, pady=0, sticky="nsew")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        
        # Settings title
        self.settings_label = ctk.CTkLabel(
            self.settings_frame, 
            text="Customization", 
            font=self.fonts["subtitle"],
            text_color=self.colors["text_light"]
        )
        self.settings_label.grid(row=0, column=0, pady=(0, 15), sticky="w")
        
        # Size
        self.size_container = ctk.CTkFrame(self.settings_frame, fg_color="transparent")
        self.size_container.grid(row=1, column=0, pady=(0, 15), sticky="ew")
        self.size_container.grid_columnconfigure(1, weight=1)
        
        self.size_label = ctk.CTkLabel(
            self.size_container, 
            text="Size:", 
            font=self.fonts["body"],
            text_color=self.colors["text_light"]
        )
        self.size_label.grid(row=0, column=0, sticky="w")
        
        self.size_value_label = ctk.CTkLabel(
            self.size_container, 
            text="5", 
            font=self.fonts["body"],
            text_color=self.colors["text_light"]
        )
        self.size_value_label.grid(row=0, column=2, padx=(10, 0), sticky="e")
        
        self.size_slider = ctk.CTkSlider(
            self.size_container, 
            from_=1, 
            to=10, 
            number_of_steps=9,
            command=self.update_size_display,
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            progress_color=self.colors["accent"]
        )
        self.size_slider.set(5)
        self.size_slider.grid(row=0, column=1, padx=10, sticky="ew")
        
        # Error correction
        self.error_container = ctk.CTkFrame(self.settings_frame, fg_color="transparent")
        self.error_container.grid(row=2, column=0, pady=(0, 15), sticky="ew")
        self.error_container.grid_columnconfigure(1, weight=1)
        
        self.error_label = ctk.CTkLabel(
            self.error_container, 
            text="Error Correction:", 
            font=self.fonts["body"],
            text_color=self.colors["text_light"]
        )
        self.error_label.grid(row=0, column=0, sticky="w")
        
        self.error_var = tk.StringVar(value="M")
        self.error_menu = ctk.CTkOptionMenu(
            self.error_container,
            values=["L", "M", "Q", "H"],
            variable=self.error_var,
            font=self.fonts["body"],
            dropdown_font=self.fonts["body"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            dropdown_hover_color=self.colors["accent_hover"]
        )
        self.error_menu.grid(row=0, column=1, padx=(10, 0), sticky="e")
        
        # Color
        self.color_container = ctk.CTkFrame(self.settings_frame, fg_color="transparent")
        self.color_container.grid(row=3, column=0, pady=(0, 15), sticky="ew")
        self.color_container.grid_columnconfigure(1, weight=1)
        
        self.fill_label = ctk.CTkLabel(
            self.color_container, 
            text="Fill Color:", 
            font=self.fonts["body"],
            text_color=self.colors["text_light"]
        )
        self.fill_label.grid(row=0, column=0, sticky="w")
        
        self.color_options = {
            "Black": "#000000", 
            "Navy Blue": "#000080", 
            "Dark Green": "#006400", 
            "Dark Red": "#8B0000", 
            "Purple": "#800080"
        }
        
        self.fill_var = tk.StringVar(value="Black")
        self.fill_menu = ctk.CTkOptionMenu(
            self.color_container,
            values=list(self.color_options.keys()),
            variable=self.fill_var,
            font=self.fonts["body"],
            dropdown_font=self.fonts["body"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            dropdown_hover_color=self.colors["accent_hover"]
        )
        self.fill_menu.grid(row=0, column=1, padx=(10, 0), sticky="e")
        
        # Buttons
        self.button_frame = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        self.button_frame.grid(row=4, column=0, padx=20, pady=(20, 20), sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)
        
        # Modern style buttons
        self.generate_button = ctk.CTkButton(
            self.button_frame,
            text="Generate",
            command=self.generate_qr,
            font=self.fonts["button"],
            fg_color=self.colors["success"],
            hover_color=self.colors["success_hover"],
            corner_radius=8,
            height=42,
            border_width=0,
            border_spacing=10,
            text_color=self.colors["bg_light"],
            compound="right",
            anchor="center"
        )
        # Add icon to enrich button appearance (Unicode emoji)
        self.generate_button._text_label.configure(text="✨ Generate")
        self.generate_button.grid(row=0, column=0, padx=(0, 5), sticky="ew")
        
        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Clear",
            command=self.clear_input,
            font=self.fonts["button"],
            fg_color=self.colors["error"],
            hover_color=self.colors["error_hover"],
            corner_radius=8,
            height=42,
            border_width=0,
            border_spacing=10,
            text_color=self.colors["bg_light"],
            compound="right",
            anchor="center"
        )
        # Add icon to enrich button appearance (Unicode emoji)
        self.clear_button._text_label.configure(text="🗑️ Clear")
        self.clear_button.grid(row=0, column=1, padx=(5, 0), sticky="ew")
        
        # Right panel - QR Code image
        self.right_panel = ctk.CTkFrame(self.content_frame, corner_radius=15, fg_color=self.colors["card_light"])
        self.right_panel.grid(row=0, column=1, padx=(15, 30), pady=30, sticky="nsew")
        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)
        
        # QR title
        self.qr_header = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        self.qr_header.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="ew")
        self.qr_header.grid_columnconfigure(0, weight=1)
        self.qr_header.grid_columnconfigure(1, weight=0)
        
        self.qr_label = ctk.CTkLabel(
            self.qr_header, 
            text="Preview", 
            font=self.fonts["subtitle"],
            text_color=self.colors["text_light"]
        )
        self.qr_label.grid(row=0, column=0, sticky="w")
        
        self.save_button = ctk.CTkButton(
            self.qr_header,
            text="Save",
            command=self.save_qr,
            font=self.fonts["button"],
            fg_color=self.colors["accent"],
            hover_color=self.colors["accent_hover"],
            corner_radius=8,
            height=36,
            border_width=0,
            text_color=self.colors["bg_light"],
            compound="right",
            state="disabled"
        )
        # Add icon to enrich button appearance (Unicode emoji)
        self.save_button._text_label.configure(text="💾 Save")
        self.save_button.grid(row=0, column=1, sticky="e")
        
        # QR image area - Made more elegant with shadow and border
        self.qr_display_frame = ctk.CTkFrame(
            self.right_panel, 
            fg_color="transparent"
        )
        self.qr_display_frame.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="nsew")
        self.qr_display_frame.grid_columnconfigure(0, weight=1)
        self.qr_display_frame.grid_rowconfigure(0, weight=1)
        
        # Special display card for QR code
        self.qr_card = ctk.CTkFrame(
            self.qr_display_frame, 
            corner_radius=12,
            fg_color=self.colors["bg_light"] if self.current_theme == "light" else self.colors["bg_dark"],
            border_width=1,
            border_color=self.colors["border_light"] if self.current_theme == "light" else self.colors["border_dark"]
        )
        self.qr_card.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.qr_card.grid_columnconfigure(0, weight=1)
        self.qr_card.grid_rowconfigure(0, weight=1)
        
        self.qr_display = ctk.CTkLabel(
            self.qr_card, 
            text="Your QR code will be displayed here",
            font=self.fonts["small"],
            text_color=self.colors["text_secondary_light"]
        )
        self.qr_display.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
        
        # Footer bar
        self.footer = ctk.CTkFrame(self.main_frame, corner_radius=0, fg_color=self.colors["card_light"], height=40)
        self.footer.grid(row=2, column=0, sticky="ew")
        self.footer.grid_propagate(False)
        self.footer.grid_columnconfigure(0, weight=1)
        self.footer.grid_columnconfigure(1, weight=0)
        
        self.status_label = ctk.CTkLabel(
            self.footer, 
            text="Ready", 
            font=self.fonts["small"],
            text_color=self.colors["text_light"]
        )
        self.status_label.grid(row=0, column=0, padx=30, pady=(0, 0), sticky="w")
        
        # Add "Created by Shend" label in the bottom right corner
        self.creator_label = ctk.CTkLabel(
            self.footer,
            text="Created by Shend",
            font=self.fonts["tiny"],
            text_color=self.colors["text_secondary_light"]
        )
        self.creator_label.grid(row=0, column=1, padx=(0, 30), pady=(0, 0), sticky="e")
        
        # Initialization
        self.qr_image = None
        self.tk_image = None
        
        # Create output folder
        self.output_folder = os.path.join(os.path.expanduser("~"), "QRCodes")
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def update_size_display(self, value):
        self.size_value_label.configure(text=f"{int(value)}")
    
    def toggle_theme(self):
        if self.theme_switch.get() == "dark":
            self.current_theme = "dark"
            ctk.set_appearance_mode("Dark")
            self.update_colors_for_theme("dark")
        else:
            self.current_theme = "light"
            ctk.set_appearance_mode("Light")
            self.update_colors_for_theme("light")
    
    def update_colors_for_theme(self, theme):
        # Color variables
        text_color = self.colors["text_dark"] if theme == "dark" else self.colors["text_light"]
        text_secondary = self.colors["text_secondary_dark"] if theme == "dark" else self.colors["text_secondary_light"]
        bg_color = self.colors["bg_dark"] if theme == "dark" else self.colors["bg_light"]
        card_color = self.colors["card_dark"] if theme == "dark" else self.colors["card_light"]
        border_color = self.colors["border_dark"] if theme == "dark" else self.colors["border_light"]
        
        # Color updates after theme change
        if theme == "dark":
            # Main components
            self.main_frame.configure(fg_color=bg_color)
            self.header.configure(fg_color=bg_color)
            self.title_label.configure(text_color=text_color)
            self.content_frame.configure(fg_color=bg_color)
            self.footer.configure(fg_color=card_color)
            
            # Left panel
            self.left_panel.configure(fg_color=card_color)
            self.input_label.configure(text_color=text_color)
            self.input_sublabel.configure(text_color=text_color)
            self.data_input.configure(border_color=border_color, fg_color=bg_color)
            
            # QR Card
            self.qr_card.configure(fg_color=bg_color, border_color=border_color)
            
            # Settings
            self.settings_label.configure(text_color=text_color)
            self.size_label.configure(text_color=text_color)
            self.size_value_label.configure(text_color=text_color)
            self.error_label.configure(text_color=text_color)
            self.fill_label.configure(text_color=text_color)
            
            # Right panel
            self.right_panel.configure(fg_color=card_color)
            self.qr_label.configure(text_color=text_color)
            
            # Status
            self.status_label.configure(text_color=text_color)
            self.creator_label.configure(text_color=text_secondary)
            
            # Placeholder
            if self.data_input.get("0.0", "end-1c").strip() == "Write your QR code content here...":
                self.data_input.configure(text_color=text_secondary)
        else:
            # Main components
            self.main_frame.configure(fg_color=bg_color)
            self.header.configure(fg_color=bg_color)
            self.title_label.configure(text_color=text_color)
            self.content_frame.configure(fg_color=bg_color)
            self.footer.configure(fg_color=card_color)
            
            # Left panel
            self.left_panel.configure(fg_color=card_color)
            self.input_label.configure(text_color=text_color)
            self.input_sublabel.configure(text_color=text_color)
            self.data_input.configure(border_color=border_color, fg_color=bg_color)
            
            # QR Card
            self.qr_card.configure(fg_color=bg_color, border_color=border_color)
            
            # Settings
            self.settings_label.configure(text_color=text_color) 
            self.size_label.configure(text_color=text_color)
            self.size_value_label.configure(text_color=text_color)
            self.error_label.configure(text_color=text_color)
            self.fill_label.configure(text_color=text_color)
            
            # Right panel
            self.right_panel.configure(fg_color=card_color)
            self.qr_label.configure(text_color=text_color)
            
            # Status
            self.status_label.configure(text_color=text_color)
            self.creator_label.configure(text_color=text_secondary)
            
            # Placeholder
            if self.data_input.get("0.0", "end-1c").strip() == "Write your QR code content here...":
                self.data_input.configure(text_color=text_secondary)
        
    def generate_qr(self):
        data = self.data_input.get("0.0", "end-1c").strip()
        
        # Placeholder check
        if data == "Write your QR code content here...":
            data = ""
        
        if not data:
            # Custom error notification
            self.show_notification("Please enter text or URL to convert to QR code.", "error")
            return
        
        size = int(self.size_slider.get())
        error_level = self.error_var.get()
        fill_color = self.color_options[self.fill_var.get()]
        
        # Error correction level
        error_correction_map = {
            "L": qrcode.constants.ERROR_CORRECT_L,  # 7% error correction
            "M": qrcode.constants.ERROR_CORRECT_M,  # 15% error correction
            "Q": qrcode.constants.ERROR_CORRECT_Q,  # 25% error correction
            "H": qrcode.constants.ERROR_CORRECT_H   # 30% error correction
        }
        
        # Status update
        self.status_label.configure(text="⏳ Generating QR code...")
        self.root.update()
        
        # Loading effect for button
        original_text = self.generate_button._text_label.cget("text")
        self.generate_button._text_label.configure(text="⌛ Processing...")
        self.generate_button.configure(state="disabled")
        self.root.update()
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=error_correction_map[error_level],
                box_size=size * 10,  # Size increase for better visibility
                border=4,
            )
            
            qr.add_data(data)
            qr.make(fit=True)
            
            self.qr_image = qr.make_image(fill_color=fill_color, back_color="white")
            
            # Resize for display
            display_size = min(self.qr_display_frame.winfo_width(), self.qr_display_frame.winfo_height()) - 80
            if display_size < 100:  # If widget hasn't been drawn yet
                display_size = 300
                
            display_img = self.qr_image.copy()
            display_img = display_img.resize((display_size, display_size), Image.LANCZOS)
            
            self.tk_image = ImageTk.PhotoImage(display_img)
            self.qr_display.configure(image=self.tk_image, text="")
            
            # Activate save button
            self.save_button.configure(state="normal")
            
            # Success notification
            self.show_notification("QR code successfully generated!", "success")
            
        except Exception as e:
            self.show_notification(f"QR code generation failed: {str(e)}", "error")
        
        # Restore button state
        self.generate_button._text_label.configure(text=original_text)
        self.generate_button.configure(state="normal")
    
    def show_notification(self, message, type="info"):
        """Show custom visual notification"""
        # Determine icon
        icon = "ℹ️" if type == "info" else "✅" if type == "success" else "❌" if type == "error" else "⚠️"
        
        # Determine color
        color = self.colors["info"] if type == "info" else self.colors["success"] if type == "success" else self.colors["error"] if type == "error" else self.colors["warning"]
        
        # Update status bar
        self.status_label.configure(text=f"{icon} {message}")
        
        # Get window size
        window_width = self.root.winfo_width()
        notification_width = min(400, window_width - 60)
        
        # Also create toast-like modern notification with width set in constructor
        notification = ctk.CTkFrame(
            self.main_frame, 
            corner_radius=10,
            border_width=1,
            border_color=color,
            fg_color=self.colors["bg_light"] if self.current_theme == "light" else self.colors["bg_dark"],
            width=notification_width
        )
        
        # Notification content
        ctk.CTkLabel(
            notification,
            text=icon,
            font=ctk.CTkFont(size=20)
        ).grid(row=0, column=0, padx=(15, 5), pady=15)
        
        ctk.CTkLabel(
            notification,
            text=message,
            font=self.fonts["body"],
            text_color=self.colors["text_light"] if self.current_theme == "light" else self.colors["text_dark"]
        ).grid(row=0, column=1, padx=(0, 15), pady=15, sticky="w")
        
        # Position notification (bottom right corner)
        notification.place(x=window_width - notification_width - 30, y=self.root.winfo_height() - 100)
        
        # Remove notification after 3 seconds
        self.root.after(3000, lambda: notification.destroy())
    
    def save_qr(self):
        if self.qr_image is None:
            self.show_notification("Create a QR code first.", "error")
            return
        
        # Timestamp default filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"QRCode_{timestamp}.png"
        
        file_path = filedialog.asksaveasfilename(
            initialdir=self.output_folder,
            initialfile=default_filename,
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                # Loading effect
                original_text = self.save_button._text_label.cget("text")
                self.save_button._text_label.configure(text="⌛ Saving...")
                self.save_button.configure(state="disabled")
                self.root.update()
                
                self.qr_image.save(file_path)
                
                # Restore button state
                self.save_button._text_label.configure(text=original_text)
                self.save_button.configure(state="normal")
                
                # Success notification
                self.show_notification(f"QR code saved: {os.path.basename(file_path)}", "success")
                
                # Option to open folder
                if messagebox.askyesno("Success", f"QR code saved to:\n{file_path}\n\nDo you want to open the containing folder?"):
                    self.open_folder(os.path.dirname(file_path))
            except Exception as e:
                self.save_button._text_label.configure(text=original_text)
                self.save_button.configure(state="normal")
                self.show_notification(f"Failed to save QR code: {str(e)}", "error")
    
    def clear_input(self):
        # Loading effect for button
        original_text = self.clear_button._text_label.cget("text")
        self.clear_button._text_label.configure(text="⌛ Clearing...")
        self.clear_button.configure(state="disabled")
        self.root.update()
        
        self.data_input.delete("0.0", "end")
        # Restore placeholder
        self.data_input.insert("0.0", "Write your QR code content here...")
        self.data_input.configure(text_color=self.colors["text_secondary_light"] if self.current_theme == "light" else self.colors["text_secondary_dark"])
        
        self.size_slider.set(5)
        self.update_size_display(5)
        self.error_var.set("M")
        self.fill_var.set("Black")
        
        # Clear QR image
        self.qr_display.configure(image="", text="Your QR code will be displayed here")
        self.qr_image = None
        self.save_button.configure(state="disabled")
        
        # Restore button state
        self.clear_button._text_label.configure(text=original_text)
        self.clear_button.configure(state="normal")
        
        # Success notification
        self.show_notification("All information cleared", "info")
    
    def open_folder(self, path):
        """Open folder in file explorer"""
        if os.name == 'nt':  # Windows
            os.startfile(path)
        elif os.name == 'posix':  # macOS and Linux
            import subprocess
            subprocess.call(['open' if os.sys.platform == 'darwin' else 'xdg-open', path])

def main():
    root = ctk.CTk()
    app = ModernQRGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()