import tkinter as tk
import vlc
import sys
import keyboard as kb
from time import sleep

class BorderlessVideoPlayer:
    def __init__(self, root :tk.Tk, filepath):
        self.root = root
        self.root.overrideredirect(True)  # Remove border
        self.root.geometry("800x600")
        
        # Create VLC instance
        self.instance : vlc.Instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        
        # Video display frame
        self.video_panel = tk.Frame(root, bg="black")
        self.video_panel.pack(fill='both', expand=1)
        
        # Embed video
        if sys.platform == "win32":
            self.player.set_hwnd(self.video_panel.winfo_id())
        elif sys.platform.startswith("linux"):
            self.player.set_xwindow(self.video_panel.winfo_id())
        
        # Load and play
        media = self.instance.media_new(filepath)
        self.player.set_media(media)
        self.player.play()
        kb.add_hotkey("x", self.close)

    def close(self):
        self.player.stop()
        self.root.destroy()

# Usage
root = tk.Tk()
player = BorderlessVideoPlayer(root, "video.mp4")
root.mainloop()
sleep(5)
exit()