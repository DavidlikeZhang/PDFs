# Grid Visualization with Python matplotlib

This repository contains a Python program that creates interactive grid visualizations using matplotlib, designed for state-based representations with customizable cell types and actions.

## Features

- **Grid Creation**: Create m×n grids of any size
- **Cell Types**: Support for three cell types:
  - Normal cells (white background)
  - Target cells (blue background) 
  - Forbidden areas (yellow background)
- **State Numbering**: Sequential state numbering (s1, s2, ...) from left to right, top to bottom
- **Action Visualization**: Five action types with visual representations:
  - `up` (a1): Upward arrow
  - `right` (a2): Rightward arrow  
  - `down` (a3): Downward arrow
  - `left` (a4): Leftward arrow
  - `stay` (a5): Circle (stay in place)

## Requirements

- Python 3.6+
- matplotlib
- numpy

## Installation

Install the required dependencies:

```bash
pip install matplotlib numpy
```

## Usage

### Basic Example

```python
from grid_visualization import GridVisualizer

# Create a 4x5 grid
visualizer = GridVisualizer(4, 5)

# Set cell types
visualizer.set_cell_type(0, 4, 'target')     # Top-right corner as target
visualizer.set_cell_type(1, 2, 'forbidden')  # Middle cell as forbidden

# Set actions  
visualizer.set_action(0, 0, 'right')  # s1 moves right
visualizer.set_action(2, 2, 'stay')   # s13 stays in place

# Visualize
fig, ax = visualizer.visualize()
plt.show()  # or plt.savefig('output.png')
```

### Available Methods

#### `GridVisualizer(m, n)`
Create a new grid visualizer with m rows and n columns.

#### `set_cell_type(row, col, cell_type)`
Set the type of a specific cell.
- `row`, `col`: 0-based indices
- `cell_type`: 'normal', 'target', or 'forbidden'

#### `set_action(row, col, action)`
Set the action for a specific cell.
- `row`, `col`: 0-based indices  
- `action`: 'up', 'right', 'down', 'left', or 'stay'

#### `get_state_number(row, col)`
Get the state number for a given cell position.
- Returns: Sequential state number (1-based)

#### `visualize(figsize=(10, 8), show_state_numbers=True, show_actions=True)`
Create and display the grid visualization.
- `figsize`: Figure size tuple
- `show_state_numbers`: Whether to show s1, s2, ... labels
- `show_actions`: Whether to show action arrows/circles

## State Numbering System

States are numbered sequentially from 1, going left to right, top to bottom:

```
s1  s2  s3  s4  s5
s6  s7  s8  s9  s10
s11 s12 s13 s14 s15
s16 s17 s18 s19 s20
```

## Action Encoding

- **a1**: Up arrow (↑)
- **a2**: Right arrow (→)  
- **a3**: Down arrow (↓)
- **a4**: Left arrow (←)
- **a5**: Circle (stay in place)

## Running the Examples

1. **Basic example**: `python3 grid_visualization.py`
2. **Comprehensive tests**: `python3 test_grid.py`

## Output Files

The program generates PNG files showing the grid visualization with:
- Color-coded cells (white/blue/yellow)
- State numbers (s1, s2, ...)
- Action indicators (arrows/circles)
- Legend explaining the color coding

## Example Scenarios

### Pathfinding Grid
```python
visualizer = GridVisualizer(5, 5)
# Set start and goal
visualizer.set_cell_type(0, 0, 'normal')  # Start
visualizer.set_cell_type(4, 4, 'target')  # Goal
# Add obstacles
visualizer.set_cell_type(2, 2, 'forbidden')
# Define optimal path actions
visualizer.set_action(0, 0, 'right')
visualizer.set_action(0, 1, 'down')
# ... etc
```

### Game Grid
```python
visualizer = GridVisualizer(3, 3)
# Multiple targets
visualizer.set_cell_type(0, 2, 'target')  # Reward location
visualizer.set_cell_type(2, 0, 'target')  # Another reward
# Hazards
visualizer.set_cell_type(1, 1, 'forbidden')  # Trap
# Agent actions
visualizer.set_action(0, 0, 'up')    # Move towards reward
visualizer.set_action(2, 2, 'stay')  # Stay at safe location
```

This visualization tool is perfect for:
- Reinforcement learning environments
- Pathfinding algorithm demonstrations  
- Game state representations
- Educational grid-world examples