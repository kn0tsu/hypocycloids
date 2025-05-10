from manim import *
import numpy as np

class NestedHypocycloids(Scene):
    def construct(self):
        # Adjusted parameters for better sizing
        initial_scale = 1.5  # Reduced from 3.0
        scale_factor = 0.75  # More aggressive scaling
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE, ORANGE, PINK, TEAL, MAROON, GOLD, LIGHT_BROWN, DARK_BLUE]
        
        current_scale = initial_scale
        group = VGroup()  # To keep all hypocycloids together
        
        for K in range(3, 15):
            hypocycloid = ParametricFunction(
                lambda t, K=K, s=current_scale: np.array([
                    s * ((K-1) * np.cos(t) + np.cos((K-1) * t)),  # Adjusted formula
                    s * ((K-1) * np.sin(t) - np.sin((K-1) * t)),
                    0
                ]),
                t_range=[0, 2 * PI],
                color=colors[(K-3) % len(colors)],
                stroke_width=1.2
            )
            group.add(hypocycloid)
            current_scale *= scale_factor

        # Center and scale the entire group to fit the screen
        group.scale(0.8).move_to(ORIGIN)
        
        self.play(LaggedStart(*[Create(h) for h in group], lag_ratio=0.3), run_time=8)
        self.wait(3)
