import dearpygui.dearpygui as dpg

dpg.create_context()

dpg.create_viewport(title="Custom Title", x_pos=0, y_pos=0, width=1200, height=800)
dpg.set_viewport_max_height(800)
dpg.set_viewport_max_width(1200)

with dpg.window(label="Settings", width=400, height=800):
    dpg.add_text("Tree")
    dpg.add_slider_int(label="Number of nodes", min_value=1, max_value=10, default_value=5)
    dpg.add_slider_int(label="Max. node value", min_value=10, max_value=100, default_value=10)
    dpg.add_spacer(height=10)
    dpg.add_button(label="Apply")

with dpg.window(label="Visualization", width=800, height=800, pos=(400, 0)):
    dpg.draw_circle(center=((800-20)/2, (800-20)/2), radius=20, fill=(255, 255, 255, 255))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
