import numpy as np

from src.core.logger import Logger
from src.entities import Point, Vector, Plane, ManipulatorData, Line, Axes
from src.use_cases import YamlRobotParser, ForwardKinematics, Graphics, ManipulatorDataGetter, InverseTransformation

def main():
    log = Logger('main')
    
    # Manipulator
    manipulator_data: ManipulatorData = YamlRobotParser.to_manipulator_data('ur3')
    manipulator_data.angles = [np.pi, 0.0, 0.0, 0.0, 0.0, 0.0]
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
    graphics.set_limits(xlim=(-0.5, 0.5),
                    ylim=(-0.5, 0.5),
                    zlim=(0.0,0.5))
    
    # Entities
    target: Point = positions[-1] + Point(0.1, 0.1, 0.1)
    target_axes: Axes = axes_list[-1]
    
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
    
    # 3. z5'
    p5: Point = InverseTransformation.get_position(target, target_axes, a[-1], d[-1], alpha[-1])
    z5: Vector = InverseTransformation.get_z_axis(target, target_axes, alpha[-1])
    plane5: Plane = Plane.from_normal_vector(z5, p5)
     
    graphics.plot_points(positions, style='-o')
    graphics.plot_oriented_point(target, axes_list[-1], color='k')
    graphics.plot_points([p5, target], style='-o')
    graphics.plot_vector(z5, p5)
    graphics.plot_plane(plane5)
    
    graphics.show()
    graphics.clear()
    
    graphics.close()


if __name__ == '__main__':
    main()
    