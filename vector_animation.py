"""
######################### Himanshu Tripathi #########################
"""

from manim import *


class LinearAlgebra(Scene):
    def construct(self):
        # Create vectors
        vec1 = Vector([3, 1], color=RED)
        vec2 = Vector([1, 2], color=BLUE)

        # Add vectors
        vec_sum = vec1.copy().shift(vec2.get_end())

        # Create text labels
        vec1_label = Tex("$\\vec{v}_1$", color=RED).next_to(vec1, LEFT)
        vec2_label = Tex("$\\vec{v}_2$", color=BLUE).next_to(vec2, UP)
        vec_sum_label = Tex("$\\vec{v}_1 + \\vec{v}_2$",
                            color=PURPLE).next_to(vec_sum, RIGHT)

        # Draw vectors and labels
        self.play(GrowArrow(vec1), Write(vec1_label))
        self.play(GrowArrow(vec2), Write(vec2_label))
        self.play(GrowArrow(vec_sum), Write(vec_sum_label))

        # Remove labels
        self.play(FadeOut(vec1_label), FadeOut(
            vec2_label), FadeOut(vec_sum_label))

        # Scale vector
        vec1_scaled = vec1.copy().scale(2)

        # Create dot product label
        dot_product_label = Tex(
            "$\\vec{v}_1 \\cdot \\vec{v}_2 = 5$", color=GREEN).next_to(vec_sum, DOWN)

        # Draw scaled vector and dot product label
        self.play(Transform(vec1, vec1_scaled))
        self.play(Write(dot_product_label))

        # Remove dot product label
        self.play(FadeOut(dot_product_label))

        # Rotate vector
        vec2_rotated = vec2.copy().rotate(PI/2)

        # Create cross product label
        cross_product_label = Tex(
            "$\\vec{v}_1 \\times \\vec{v}_2 = -5$", color=YELLOW).next_to(vec2_rotated, LEFT)

        # Draw rotated vector and cross product label
        self.play(Transform(vec2, vec2_rotated))
        self.play(Write(cross_product_label))

        # Remove vectors and label
        self.play(FadeOut(vec1), FadeOut(vec2), FadeOut(
            vec_sum), FadeOut(cross_product_label))
