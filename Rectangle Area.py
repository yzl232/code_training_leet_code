'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Rectangle Area

Assume that the total area is never beyond the maximum possible value of int.

'''
# inclusion-exclusion principle
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, a, b, c, d, e, f, g, h):
        return (c - a) * (d - b) + (g - e) * (h - f) - max(min(c, g) - max(a, e), 0) * max(min(d, h) - max(b, f), 0)