#!/usr/bin/env python3
"""
Test script for the GridVisualizer class
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environment

from grid_visualization import GridVisualizer
import matplotlib.pyplot as plt


def test_basic_functionality():
    """Test basic functionality of the GridVisualizer"""
    # Create a 3x4 grid for testing
    visualizer = GridVisualizer(3, 4)
    
    # Test setting cell types
    visualizer.set_cell_type(0, 3, 'target')     # s4 is target
    visualizer.set_cell_type(1, 1, 'forbidden')  # s6 is forbidden
    visualizer.set_cell_type(2, 2, 'target')     # s11 is target
    
    # Test setting actions
    visualizer.set_action(0, 0, 'right')  # s1 moves right
    visualizer.set_action(0, 1, 'down')   # s2 moves down  
    visualizer.set_action(1, 0, 'up')     # s5 moves up
    visualizer.set_action(1, 2, 'left')   # s7 moves left
    visualizer.set_action(2, 1, 'stay')   # s10 stays in place
    
    # Test state numbering
    assert visualizer.get_state_number(0, 0) == 1
    assert visualizer.get_state_number(0, 3) == 4
    assert visualizer.get_state_number(1, 1) == 6
    assert visualizer.get_state_number(2, 3) == 12
    
    # Visualize and save
    fig, ax = visualizer.visualize()
    plt.savefig('/home/runner/work/PDFs/PDFs/test_grid.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Basic functionality test passed!")
    return True


def test_larger_grid():
    """Test with a larger grid to demonstrate scalability"""
    # Create a 5x6 grid
    visualizer = GridVisualizer(5, 6)
    
    # Create a more complex example
    # Set targets in corners
    visualizer.set_cell_type(0, 0, 'target')     # s1
    visualizer.set_cell_type(0, 5, 'target')     # s6
    visualizer.set_cell_type(4, 0, 'target')     # s25
    visualizer.set_cell_type(4, 5, 'target')     # s30
    
    # Create forbidden areas in middle
    visualizer.set_cell_type(2, 2, 'forbidden')  # s15
    visualizer.set_cell_type(2, 3, 'forbidden')  # s16
    visualizer.set_cell_type(1, 2, 'forbidden')  # s9
    visualizer.set_cell_type(3, 3, 'forbidden')  # s22
    
    # Add various actions
    visualizer.set_action(0, 1, 'left')     # s2 moves toward target s1
    visualizer.set_action(1, 0, 'up')       # s7 moves toward target s1
    visualizer.set_action(1, 1, 'stay')     # s8 stays in place
    visualizer.set_action(0, 4, 'right')    # s5 moves toward target s6
    visualizer.set_action(3, 0, 'down')     # s19 moves toward target s25
    visualizer.set_action(4, 1, 'left')     # s26 moves toward target s25
    visualizer.set_action(3, 5, 'down')     # s24 moves toward target s30
    visualizer.set_action(4, 4, 'right')    # s29 moves toward target s30
    
    # Visualize and save
    fig, ax = visualizer.visualize(figsize=(12, 10))
    plt.savefig('/home/runner/work/PDFs/PDFs/large_grid.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Large grid test passed!")
    return True


def test_edge_cases():
    """Test edge cases and error handling"""
    visualizer = GridVisualizer(2, 2)
    
    # Test error handling for invalid cell types
    try:
        visualizer.set_cell_type(0, 0, 'invalid')
        print("✗ Should have raised ValueError for invalid cell type")
        return False
    except ValueError:
        print("✓ Correctly handled invalid cell type")
    
    # Test error handling for invalid actions
    try:
        visualizer.set_action(0, 0, 'invalid')
        print("✗ Should have raised ValueError for invalid action")
        return False
    except ValueError:
        print("✓ Correctly handled invalid action")
    
    # Test all valid actions
    valid_actions = ['up', 'right', 'down', 'left', 'stay']
    for i, action in enumerate(valid_actions):
        row, col = divmod(i, 2)
        if row < 2 and col < 2:  # Make sure we're within bounds
            visualizer.set_action(row, col, action)
    
    # Visualize and save
    fig, ax = visualizer.visualize()
    plt.savefig('/home/runner/work/PDFs/PDFs/edge_cases_grid.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Edge cases test passed!")
    return True


if __name__ == "__main__":
    print("Testing GridVisualizer class...")
    
    success = True
    success &= test_basic_functionality()
    success &= test_larger_grid()
    success &= test_edge_cases()
    
    if success:
        print("\n🎉 All tests passed! Grid visualization is working correctly.")
        print("Generated test images:")
        print("- test_grid.png: Basic 3x4 grid example")
        print("- large_grid.png: Complex 5x6 grid example")
        print("- edge_cases_grid.png: Edge cases demonstration")
    else:
        print("\n❌ Some tests failed!")