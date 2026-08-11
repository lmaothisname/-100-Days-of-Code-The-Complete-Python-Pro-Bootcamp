import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT_UI = ("Arial",11,"bold")
class WatermarkApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Interactive Watermark App")  
    self.root.geometry("1280x960")
    
    #Image variables 
    self.origin_image = None # original full-resolution image
    self.preview_image =  None # Scaled image for UI preview
    self.logo_image = None # Load logo image
    self.tk_display = None # Tkinter photoImage reference
    
    # watermark position in percentage (0.0 to 1.0) so it scales accurately to full-res
    self.pos_x = 0.5
    self.pos_y = 0.5
    
    # watermark mode: "text" or "logo"
    self.watermark_type = tk.StringVar(value="text")
    self.setup_ui()
    
  def setup_ui(self):
    # --- Left Control Panel ---
    sidebar = tk.Frame(self.root, width=280, padx=10, pady=10)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)
    
    # 1. Base Image Loader
    tk.Label(sidebar, text="1. Base Image", font=FONT_UI).pack(anchor="w", pady=(0,5))
    tk.Button(sidebar, text="Open Main Image",command=self.load_base_image).pack(fill=tk.X, pady=5)
    
    # 2.Watermark Type Selector
    tk.Label(sidebar, text="2. Watermark Type", font=FONT_UI).pack(anchor="w", pady=(15,5))
    tk.Radiobutton(sidebar, text="Text Watermark", variable=self.watermark_type, value="text", command=self.update_preview).pack(anchor="w")
    tk.Radiobutton(sidebar, text="Logo / Image", variable=self.watermark_type, value="logo", command=self.update_preview).pack(anchor="w")
    
    # 3. Text Controls
    self.text_frame = tk.LabelFrame(sidebar, text="Text Options", padx=5, pady=5)
    self.text_frame.pack(fill=tk.X,pady=10)
    tk.Label(self.text_frame, text="Watermark Text:").pack(anchor="w")
    self.entry_text = tk.Entry(self.text_frame)
    self.entry_text.insert(0,"© My Watermark")
    self.entry_text.pack(fill=tk.X,pady=5)
    self.entry_text.bind("<KeyRelease>", lambda e: self.update_preview())
    
    # 4.Logo controls
    self.logo_frame = tk.LabelFrame(sidebar, text="Logo Options", padx=5, pady=5)
    self.logo_frame.pack(fill=tk.X,pady=10)
    tk.Button(self.logo_frame, text="Select Logo PNG", command=self.load_logo).pack(fill=tk.X, pady=5)
    
    # 5. Instructions & Save
    tk.Label(sidebar, text="Tip: Click / Drag on the image\nto move the watermark!", fg="blue", wraplength=250).pack(pady=15)
    tk.Button(sidebar, text="💾 Save Watermarked Image", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=self.save_image).pack(fill=tk.X, pady=10)
    
    # --- Right Preview Canvas ---
    self.canvas_frame = tk.Frame(self.root, bg="#222")
    self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    self.canvas = tk.Canvas(self.canvas_frame, bg="#333", cursor="cross")
    self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Mouse Drag & Drop events on canvas
    self.canvas.bind("<Button-1>", self.on_mouse_drag)
    self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
    
  def load_base_image(self):
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.webp *.bmp")])
    if file_path:
      self.origin_image = Image.open(file_path).convert("RGBA")
      self.update_preview()
      
  def load_logo(self):
    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if file_path:
      self.logo_image = Image.open(file_path).convert("RGBA")
      self.watermark_type.set("logo")
      self.update_preview()
      
  def on_mouse_drag(self, event):
    """Update watermark coordinates when clicking or dragging on the preview canvas."""
    if not self.preview_image:
      return
    
    # Calculate position as a relative ratio (0.0 to 1.0)
    canvas_w = self.preview_image.width
    canvas_h = self.preview_image.height
    
    self.pos_x = max(0.0, min(1.0, event.x / canvas_w))
    self.pos_y = max(0.0, min(1.0, event.y / canvas_h))
    self.update_preview()
    
  def render_watermark_layer(self, base_img):
    """Draws/pastes the selected watermark onto the given image at (self.pos_x, self.pos_y)."""
    output = base_img.copy()
    w, h = output.size  
    
    # Target X and Y pixel positions
    x = int(self.pos_x * w)
    y = int(self.pos_y * h)
    
    if self.watermark_type.get() == "text":
      text = self.entry_text.get()
      if text:
        overlay = Image.new("RGBA", (w, h), (255, 255, 255, 0)) 
        draw = ImageDraw.Draw(overlay)
        font = ImageFont.load_default()
        draw.text((x + 2, y + 2), text, fill=(0, 0, 0, 150), font=font)
        draw.text((x, y), text, fill=(255, 255, 255, 200), font=font)
        output = Image.alpha_composite(output, overlay)
    elif self.watermark_type.get() == "logo" and self.logo_image:
      # Resize logo relative to base image size
      logo_w = int(w * 0.2)
      logo_h = int(self.logo_image.height * (logo_w / self.logo_image.width))
      logo_resized = self.logo_image.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
      
      # Center logo at the mouse point
      paste_x = max(0, min(w - logo_w, x - logo_w // 2))
      paste_y = max(0, min(h - logo_h, y - logo_h // 2))
      
      output.paste(logo_resized, (paste_x, paste_y), mask=logo_resized)
      
    return output
  
  def update_preview(self):
    """Refreshes the live preview on screen."""
    if not self.origin_image:
      return
    
    # Scale down original image to fit within preview canvas (max 550x550)
    self.preview_image = self.origin_image.copy()
    self.preview_image.thumbnail((550, 550))

    # Render watermark on preview
    preview_with_watermark = self.render_watermark_layer(self.preview_image)
    
    # Update Tkinter canvas
    self.tk_display = ImageTk.PhotoImage(preview_with_watermark)
    self.canvas.config(width=self.preview_image.width, height=self.preview_image.height)
    self.canvas.delete("all")
    self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_display)
    
  def save_image(self):
    """Renders the watermark onto the full original resolution and saves it."""
    if not self.origin_image:
      messagebox.showwarning("Warning", "Please open an image first!")
      return

    save_path = filedialog.asksaveasfilename(
      defaultextension=".png",
      filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")]
    )
    if save_path:
      final_img = self.render_watermark_layer(self.orig_image)
      final_img.convert("RGB").save(save_path)
      messagebox.showinfo("Success", f"Saved successfully to:\n{save_path}")
      
if __name__ == "__main__":
  root = tk.Tk()
  app = WatermarkApp(root)
  root.mainloop()