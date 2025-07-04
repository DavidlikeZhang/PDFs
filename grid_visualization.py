#!/usr/bin/env python3
"""
Grid Visualization Program using matplotlib
Creates an m×n grid with states, cell types, and actions visualization
"""

import matplotlib
# Use Agg backend for headless environments, comment out for interactive use
try:
    matplotlib.use('Agg')
except:
    pass

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


class GridVisualizer:
    """
    A class to create and visualize grid-based state representations.
    
    Features:
    - Support for different cell types: target (blue), forbidden (yellow), normal (white)
    - Sequential state numbering: s1, s2, ... from left to right, top to bottom
    - Action visualization: arrows for movement, circles for staying in place
    """
    
    def __init__(self, m, n):
        """
        Initialize the grid visualizer.
        
        Args:
            m (int): Number of rows
            n (int): Number of columns
        """
        self.m = m  # rows
        self.n = n  # columns
        self.grid = np.zeros((m, n), dtype=int)  # 0: normal, 1: target, 2: forbidden
        self.actions = {}  # Dictionary to store actions for each state
        self.fig = None
        self.ax = None
        
    def set_cell_type(self, row, col, cell_type):
        """
        Set the type of a specific cell.
        
        Args:
            row (int): Row index (0-based)
            col (int): Column index (0-based)
            cell_type (str): 'normal', 'target', or 'forbidden'
        """
        type_map = {'normal': 0, 'target': 1, 'forbidden': 2}
        if cell_type in type_map:
            self.grid[row, col] = type_map[cell_type]
        else:
            raise ValueError("cell_type must be 'normal', 'target', or 'forbidden'")
    
    def set_action(self, row, col, action):
        """
        Set the action for a specific cell.
        
        Args:
            row (int): Row index (0-based)
            col (int): Column index (0-based)
            action (str): 'up' (a1), 'right' (a2), 'down' (a3), 'left' (a4), 'stay' (a5)
        """
        state_num = row * self.n + col + 1
        action_map = {'up': 'a1', 'right': 'a2', 'down': 'a3', 'left': 'a4', 'stay': 'a5'}
        if action in action_map:
            self.actions[state_num] = action
        else:
            raise ValueError("action must be 'up', 'right', 'down', 'left', or 'stay'")
    
    def get_state_number(self, row, col):
        """
        Get the state number for a given cell position.
        
        Args:
            row (int): Row index (0-based)
            col (int): Column index (0-based)
            
        Returns:
            int: State number (1-based, sequential from left to right, top to bottom)
        """
        return row * self.n + col + 1
    
    def visualize(self, figsize=(10, 8), show_state_numbers=True, show_actions=True):
        """
        Create and display the grid visualization.
        
        Args:
            figsize (tuple): Figure size (width, height)
            show_state_numbers (bool): Whether to show state numbers (s1, s2, ...)
            show_actions (bool): Whether to show action arrows/circles
        """
        self.fig, self.ax = plt.subplots(1, 1, figsize=figsize)
        
        # Define colors for different cell types
        colors = {0: 'white', 1: 'lightblue', 2: 'yellow'}
        edge_colors = {0: 'black', 1: 'blue', 2: 'orange'}
        
        # Draw the grid
        for row in range(self.m):
            for col in range(self.n):
                cell_type = self.grid[row, col]
                
                # Create rectangle for the cell
                rect = patches.Rectangle(
                    (col, self.m - row - 1), 1, 1,
                    linewidth=2,
                    edgecolor=edge_colors[cell_type],
                    facecolor=colors[cell_type]
                )
                self.ax.add_patch(rect)
                
                # Add state number
                if show_state_numbers:
                    state_num = self.get_state_number(row, col)
                    self.ax.text(
                        col + 0.1, self.m - row - 0.1, f's{state_num}',
                        fontsize=10, fontweight='bold',
                        verticalalignment='top'
                    )
                
                # Add action visualization
                if show_actions:
                    state_num = self.get_state_number(row, col)
                    if state_num in self.actions:
                        self._draw_action(row, col, self.actions[state_num])
        
        # Set up the plot
        self.ax.set_xlim(0, self.n)
        self.ax.set_ylim(0, self.m)
        self.ax.set_aspect('equal')
        self.ax.set_xticks(range(self.n + 1))
        self.ax.set_yticks(range(self.m + 1))
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title(f'Grid Visualization ({self.m}×{self.n})', fontsize=14, fontweight='bold')
        
        # Add legend
        legend_elements = [
            patches.Patch(color='white', label='Normal'),
            patches.Patch(color='lightblue', label='Target'),
            patches.Patch(color='yellow', label='Forbidden'),
        ]
        self.ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1))
        
        plt.tight_layout()
        return self.fig, self.ax
    
    def _draw_action(self, row, col, action):
        """
        Draw action arrow or circle for a specific cell.
        
        Args:
            row (int): Row index (0-based)
            col (int): Column index (0-based)
            action (str): Action type ('up', 'right', 'down', 'left', 'stay')
        """
        # Center of the cell in plot coordinates
        center_x = col + 0.5
        center_y = self.m - row - 0.5
        
        if action == 'stay':
            # Draw circle for stay action
            circle = patches.Circle(
                (center_x, center_y), 0.15,
                linewidth=2, edgecolor='red', facecolor='none'
            )
            self.ax.add_patch(circle)
            # Add action label
            self.ax.text(center_x, center_y - 0.3, 'a5', fontsize=8, 
                        ha='center', va='center', color='red', fontweight='bold')
        else:
            # Draw arrow for movement actions
            arrow_props = {
                'up': (0, 0.25, 'a1'),
                'right': (0.25, 0, 'a2'),
                'down': (0, -0.25, 'a3'),
                'left': (-0.25, 0, 'a4')
            }
            
            if action in arrow_props:
                dx, dy, label = arrow_props[action]
                self.ax.annotate(
                    '', xy=(center_x + dx, center_y + dy), 
                    xytext=(center_x, center_y),
                    arrowprops=dict(arrowstyle='->', lw=2, color='red')
                )
                # Add action label
                label_x = center_x + dx * 1.5
                label_y = center_y + dy * 1.5 - 0.1
                self.ax.text(label_x, label_y, label, fontsize=8, 
                            ha='center', va='center', color='red', fontweight='bold')


def main():
    """
    Example usage of the GridVisualizer class.
    """
    # Create a 4x5 grid
    visualizer = GridVisualizer(4, 5)
    
    # Set some cells as target (blue)
    visualizer.set_cell_type(0, 4, 'target')
    visualizer.set_cell_type(3, 0, 'target')
    
    # Set some cells as forbidden (yellow)
    visualizer.set_cell_type(1, 2, 'forbidden')
    visualizer.set_cell_type(2, 3, 'forbidden')
    
    # Set some actions
    visualizer.set_action(0, 0, 'right')  # s1 moves right
    visualizer.set_action(0, 1, 'down')   # s2 moves down
    visualizer.set_action(1, 0, 'up')     # s6 moves up
    visualizer.set_action(2, 2, 'stay')   # s13 stays in place
    visualizer.set_action(3, 4, 'left')   # s20 moves left
    
    # Visualize the grid
    fig, ax = visualizer.visualize()
    
    # Save the plot (recommended for non-interactive environments)
    plt.savefig('grid_example.png', dpi=300, bbox_inches='tight')
    print("Grid visualization saved as 'grid_example.png'")
    
    # Show the plot (uncomment for interactive environments)
    # plt.show()
    
    return fig, ax


if __name__ == "__main__":
    main()