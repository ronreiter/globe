# Globe Visualization

This interactive 3D globe visualization shows animated arcs connecting different points on Earth. It uses Three.js for rendering and provides various configuration options to adjust performance and visual quality.

## Features

- Interactive 3D Earth with realistic lighting and landmass visualization
- Animated arcs connecting different locations with smooth appearance/disappearance
- Impact effects when arcs reach their destinations
- Mouse controls for rotation and interaction
- Configurable parameters for performance/quality tradeoffs

## Usage

Simply open `index.html` in a modern web browser. The visualization will start automatically.

### Interaction

- **Drag**: Click and drag to rotate the globe
- **Hover**: Hover over land points to see them highlighted

## Configuration Options

At the top of the script in `index.html`, you'll find a `CONFIG` object that controls various aspects of the visualization. Here are the key parameters you can adjust:

### Globe Appearance

- `globeRadius`: Size of the globe (default: 11)
- `globeSegments`: Resolution of the globe (32-128, lower for better performance)

### Land Points

- `numPoints`: Maximum points to generate (3000-10000, lower for better performance)
- `dotSize`: Size of land dots (0.05-0.1)
- `dotSegments`: Land dot geometry segments (4-8, lower for better performance)

### Arcs

- `maxConcurrentArcs`: Maximum concurrent arcs (6-20, lower for better performance)
- `arcFrequency`: How often new arcs appear (higher = less frequent)
- `arcTimingVariation`: Randomness in arc timing (0-1, higher = more random)
- `arcTubeSegments`: Maximum tube segments for arcs (6-16, lower for better performance)
- `arcRadialSegments`: Radial segments for arc tubes (3-8, lower for better performance)
- `arcThickness`: Thickness of arcs (0.04-0.1)
- `arcPointsCount`: Number of points in arc path (20-40, lower for better performance)

### Animation and Behavior

- `rotationSpeed`: Speed of auto-rotation (0.001-0.003)
- `arcGrowDuration`: Base duration for arc growth in seconds (0.5-1.5)
- `arcRetreatDuration`: Base duration for arc retreat in seconds (0.8-2.0)

### Impact Effects

- `impactSize`: Maximum impact size as fraction of globe radius (0.05-0.2)

### Rendering

- `useHighPerformanceMode`: Set true for better performance but lower visual quality
- `skipFrames`: Number of frames to skip when updating (0-2, higher for better performance)

## Performance Optimization

If the visualization runs slowly on your device, you can:

1. Set `useHighPerformanceMode: true` in the CONFIG object
2. Reduce `globeSegments` to 32
3. Reduce `numPoints` to 4000-5000
4. Reduce `maxConcurrentArcs` to 8-10
5. Increase `skipFrames` to 1 or 2

## Customization Examples

### Higher Quality (for powerful devices)

```javascript
const CONFIG = {
    globeRadius: 11,
    globeSegments: 96,
    numPoints: 10000,
    dotSize: 0.07,
    dotSegments: 7,
    maxConcurrentArcs: 20,
    arcFrequency: 0.45,
    arcTimingVariation: 0.3,
    arcTubeSegments: 16,
    arcRadialSegments: 6,
    arcThickness: 0.05,
    arcPointsCount: 40,
    rotationSpeed: 0.0015,
    arcGrowDuration: 0.7,
    arcRetreatDuration: 1.0,
    impactSize: 0.07,
    useHighPerformanceMode: false,
    skipFrames: 0
};
```

### Performance Mode (for lower-end devices)

```javascript
const CONFIG = {
    globeRadius: 11,
    globeSegments: 32,
    numPoints: 3000,
    dotSize: 0.08,
    dotSegments: 4,
    maxConcurrentArcs: 6,
    arcFrequency: 0.8,
    arcTimingVariation: 0.2,
    arcTubeSegments: 8,
    arcRadialSegments: 3,
    arcThickness: 0.06,
    arcPointsCount: 24,
    rotationSpeed: 0.002,
    arcGrowDuration: 0.7,
    arcRetreatDuration: 1.0,
    impactSize: 0.07,
    useHighPerformanceMode: true,
    skipFrames: 2
};
```

## Common Modifications

### Change Globe Color

Find the `globeMaterial` definition and modify the color property:

```javascript
const globeMaterial = new THREE.MeshPhongMaterial({ 
    color: 0x0077be, // Change this hex color
    shininess: 15,
    specular: 0x222233,
    emissive: 0x002244,
});
```

### Change Arc Color

Find the `tubeMaterial` definition and modify the color property:

```javascript
const tubeMaterial = new THREE.MeshBasicMaterial({
    color: 0xccddff, // Change this hex color
    opacity: 0.9,
    transparent: true
});
```

### Change Background Color

Find the scene initialization and modify the background color:

```javascript
scene.background = new THREE.Color(0x000204); // Change this hex color
```

### Adjust Lighting

The lighting setup can be modified by changing the light intensities and positions. Look for the various light definitions (`ambientLight`, `directionalLight`, `backLight`, `rimLight`, `fillLight`) and adjust their parameters.

## Technical Notes

- The world map is represented as a binary bitmap where '1' indicates land and '0' indicates water
- Land points are distributed using a Fibonacci lattice algorithm for even distribution
- Arcs use cubic Bezier curves with tension control for smooth paths
- Impact effects use expanding circles with easing functions for smooth animations
- Performance optimization includes geometry reuse, frame skipping, and dynamic level-of-detail

## Code Structure

- The entire visualization is contained in a single HTML file with embedded JavaScript
- Three.js handles all the 3D rendering and WebGL abstractions
- The code follows a modular approach with separate functions for:
  - Scene setup and initialization
  - Globe creation and surface texturing
  - Land point generation and distribution
  - Arc animation and lifecycle management
  - Impact effect rendering
  - Animation loop and frame updates
- Reusable geometries and materials are created once and shared
- Animation states are tracked using arrays of objects with timestamps
- A requestAnimationFrame loop drives all animations with delta-time calculations