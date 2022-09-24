import numpy as np

from src.core.logger import Logger
from src.entities import Point, Vector, Plane, ManipulatorData, Line, Axes
from src.use_cases import YamlRobotParser, ForwardKinematics, Graphics, ManipulatorDataGetter, InverseTransformation

def main():
    log = Logger('main')
    
    # Manipulator
    manipulator_data: ManipulatorData = YamlRobotParser.to_manipulator_data('ur3')
    manipulator_data.angles = [np.pi, 0.0, 0.0, 0.0, 0.0, np.pi/4]
    transformation_matrices: list[np.ndarray] = ForwardKinematics.get(manipulator_data)
    manipulator_data = ManipulatorDataGetter.get(transformation_matrices, manipulator_data)
    manipulator_data.positions.insert(0, Point(0.0,0.0,0.0))
    
    a: list[float] = manipulator_data.a_values.copy()
    d: list[float] = manipulator_data.d_values.copy()
    alpha: list[float] = manipulator_data.alpha_values.copy()
    positions: list[float] = manipulator_data.positions.copy()
    axes_list: list[Axes] = manipulator_data.axes_list.copy()
    
    # Graphics
    graphics: Graphics = Graphics()
    graphics.set_limits(xlim=(-0.1, 0.7),
                    ylim=(-0.1, 0.5),
                    zlim=(0.0,0.3))
    
    # Entities
    target: Point = positions[-1] + Point(0.1, 0.1, 0.1)
    target_axes: Axes = axes_list[-1]
    new_positions: list[Point] = [target]
    
    # 1. Initial configuration
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, target_axes)
    graphics.plot_multiple_axes(axes_list, positions[1:])
    
    graphics.show()
    graphics.clear()
    
    # 2. End effector to target
    positions.pop()
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    
    graphics.show()
    graphics.clear()
    
    # 3. p5'
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    positions.pop()
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    
    graphics.show()
    graphics.clear()
    
    # 3. z5'
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    z5: Vector = InverseTransformation.get_z_axis(target, target_axes, alpha[-1])
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    graphics.plot_vector(z5, p5)
    
    graphics.show()
    graphics.clear()
    
    # 4. plane 5
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    z5: Vector = InverseTransformation.get_z_axis(target, target_axes, alpha[-1])
    plane5: Plane = Plane.from_normal_vector(z5, p5)
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    graphics.plot_vector(z5, p5)
    graphics.plot_plane(plane5, center=p5)
    
    graphics.show()
    graphics.clear()
    
    # 5. line from p4 to p5'
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    z5: Vector = InverseTransformation.get_z_axis(target, target_axes, alpha[-1])
    plane5: Plane = Plane.from_normal_vector(z5, p5)
    line45: Line = Line.from_two_points(positions[-1], p5)
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    graphics.plot_vector(z5, p5)
    graphics.plot_plane(plane5, center=p5)
    graphics.plot_line(line45, style='--', color='tab:gray')
    
    graphics.show()
    graphics.clear()
    
    # 6. projection of line to plane
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    z5: Vector = InverseTransformation.get_z_axis(target, target_axes, alpha[-1])
    plane5: Plane = Plane.from_normal_vector(z5, p5)
    line45: Line = Line.from_two_points(positions[-1], p5)
    line_proj: Line = InverseTransformation.get_projection(plane5, line45, p5)
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    graphics.plot_vector(z5, p5)
    graphics.plot_plane(plane5, center=p5)
    graphics.plot_line(line_proj, style='--', color='tab:gray')
    
    graphics.show()
    graphics.clear()
    
    # 7. p4'
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    z5: Vector = InverseTransformation.get_z_axis(target, target_axes, alpha[-1])
    plane5: Plane = Plane.from_normal_vector(z5, p5)
    line45: Line = Line.from_two_points(positions[-1], p5)
    line_proj: Line = InverseTransformation.get_projection(plane5, line45, p5)
    # p4: Point = 
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    graphics.plot_vector(z5, p5)
    graphics.plot_plane(plane5, center=p5)
    graphics.plot_line(line_proj, style='--', color='tab:gray')
    
    graphics.show()
    graphics.clear()
    
    graphics.close()


if __name__ == '__main__':
    main()
    