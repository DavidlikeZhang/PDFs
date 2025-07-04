#!/usr/bin/env python3
"""
Comprehensive demonstration of the GridVisualizer capabilities
Creates multiple examples showing different use cases
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

from grid_visualization import GridVisualizer
import matplotlib.pyplot as plt


def create_pathfinding_example():
    """Create a pathfinding scenario demonstration"""
    print("Creating pathfinding example...")
    
    # Create 6x8 grid for pathfinding
    visualizer = GridVisualizer(6, 8)
    
    # Set start and goal
    visualizer.set_cell_type(0, 0, 'target')  # Start (s1)
    visualizer.set_cell_type(5, 7, 'target')  # Goal (s48)
    
    # Create obstacles/walls
    obstacles = [
        (1, 2), (1, 3), (1, 4), (1, 5),  # Horizontal wall
        (2, 2), (3, 2), (4, 2),          # Vertical wall  
        (3, 5), (3, 6), (4, 5), (4, 6),  # Block obstacle
    ]
    for row, col in obstacles:
        visualizer.set_cell_type(row, col, 'forbidden')
    
    # Define optimal path actions
    path_actions = [
        (0, 0, 'down'),   # s1: go down
        (1, 0, 'down'),   # s9: go down  
        (2, 0, 'down'),   # s17: go down
        (3, 0, 'down'),   # s25: go down
        (4, 0, 'down'),   # s33: go down
        (5, 0, 'right'),  # s41: go right
        (5, 1, 'right'),  # s42: go right
        (5, 2, 'right'),  # s43: go right
        (5, 3, 'right'),  # s44: go right
        (5, 4, 'right'),  # s45: go right
        (5, 5, 'right'),  # s46: go right
        (5, 6, 'right'),  # s47: go right
        (5, 7, 'stay'),   # s48: stay at goal
    ]
    
    for row, col, action in path_actions:
        visualizer.set_action(row, col, action)
    
    # Visualize and save
    fig, ax = visualizer.visualize(figsize=(14, 10))
    plt.title('Pathfinding Example: Navigate from Start to Goal', pad=20, fontsize=16)
    plt.savefig('/home/runner/work/PDFs/PDFs/pathfinding_example.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "pathfinding_example.png"


def create_game_environment():
    """Create a game environment with multiple targets and hazards"""
    print("Creating game environment example...")
    
    # Create 4x6 grid for game environment
    visualizer = GridVisualizer(4, 6)
    
    # Multiple reward locations
    rewards = [(0, 5), (2, 1), (3, 4)]  # s6, s14, s23
    for row, col in rewards:
        visualizer.set_cell_type(row, col, 'target')
    
    # Hazards/traps
    hazards = [(1, 1), (1, 3), (2, 4)]  # s8, s10, s17
    for row, col in hazards:
        visualizer.set_cell_type(row, col, 'forbidden')
    
    # Agent strategies for different positions
    strategies = [
        (0, 0, 'right'),  # s1: move towards reward s6
        (0, 1, 'right'),  # s2: move towards reward s6
        (0, 2, 'right'),  # s3: move towards reward s6
        (0, 3, 'right'),  # s4: move towards reward s6
        (0, 4, 'right'),  # s5: move towards reward s6
        (1, 0, 'down'),   # s7: avoid hazard, go to s14
        (1, 2, 'down'),   # s9: move towards reward s14
        (1, 4, 'down'),   # s11: move towards reward s17
        (1, 5, 'down'),   # s12: safe movement
        (2, 0, 'stay'),   # s13: safe position
        (2, 2, 'left'),   # s15: move towards reward s14
        (2, 3, 'down'),   # s16: move towards reward s23
        (2, 5, 'down'),   # s18: safe movement
        (3, 0, 'right'),  # s19: move towards reward s14
        (3, 1, 'stay'),   # s20: stay at reward
        (3, 2, 'right'),  # s21: move towards reward s23
        (3, 3, 'right'),  # s22: move towards reward s23
        (3, 5, 'left'),   # s24: move towards reward s23
    ]
    
    for row, col, action in strategies:
        visualizer.set_action(row, col, action)
    
    # Visualize and save
    fig, ax = visualizer.visualize(figsize=(12, 8))
    plt.title('Game Environment: Multiple Rewards and Hazards', pad=20, fontsize=16)
    plt.savefig('/home/runner/work/PDFs/PDFs/game_environment.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "game_environment.png"


def create_action_showcase():
    """Create a small grid showcasing all action types"""
    print("Creating action showcase example...")
    
    # Create 3x3 grid to show all actions
    visualizer = GridVisualizer(3, 3)
    
    # Set center as target for reference
    visualizer.set_cell_type(1, 1, 'target')  # s5
    
    # Showcase all action types
    actions_demo = [
        (0, 1, 'up'),     # s2: up arrow (a1)
        (1, 2, 'right'),  # s6: right arrow (a2)  
        (2, 1, 'down'),   # s8: down arrow (a3)
        (1, 0, 'left'),   # s4: left arrow (a4)
        (1, 1, 'stay'),   # s5: circle (a5)
        # Corner actions for variety
        (0, 0, 'right'),  # s1: diagonal example
        (0, 2, 'down'),   # s3: diagonal example
        (2, 0, 'up'),     # s7: diagonal example
        (2, 2, 'left'),   # s9: diagonal example
    ]
    
    for row, col, action in actions_demo:
        visualizer.set_action(row, col, action)
    
    # Visualize and save
    fig, ax = visualizer.visualize(figsize=(8, 8))
    plt.title('Action Types Showcase: All Five Actions (a1-a5)', pad=20, fontsize=16)
    plt.savefig('/home/runner/work/PDFs/PDFs/action_showcase.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "action_showcase.png"


def main():
    """Run all demonstration examples"""
    print("🎯 Creating comprehensive grid visualization examples...\n")
    
    examples = []
    examples.append(create_pathfinding_example())
    examples.append(create_game_environment())
    examples.append(create_action_showcase())
    
    print(f"\n✅ Successfully created {len(examples)} demonstration examples:")
    for i, filename in enumerate(examples, 1):
        print(f"  {i}. {filename}")
    
    print("\n📋 Summary of all generated files:")
    print("  • test_grid.png - Basic functionality test (3×4)")
    print("  • large_grid.png - Complex example test (5×6)")  
    print("  • edge_cases_grid.png - Edge cases test (2×2)")
    print("  • grid_example.png - Main script example (4×5)")
    print("  • pathfinding_example.png - Pathfinding scenario (6×8)")
    print("  • game_environment.png - Game with rewards/hazards (4×6)")
    print("  • action_showcase.png - All action types demo (3×3)")


if __name__ == "__main__":
    main()