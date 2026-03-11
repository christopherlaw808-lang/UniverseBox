extends Node2D
class_name UniverseView

signal tile_selected(tile_data: Dictionary)

@export var simulation_path: NodePath

var simulation: SimulationBridge
var selected_tile := Vector2i(-1, -1)

func _ready() -> void:
	simulation = get_node_or_null(simulation_path)
	if simulation == null:
		push_warning("UniverseView missing SimulationBridge reference.")
		return
	simulation.world_generated.connect(queue_redraw)
	queue_redraw()

func _draw() -> void:
	if simulation == null or simulation.grid.is_empty():
		return

	for y in simulation.world_height:
		for x in simulation.world_width:
			var terrain := simulation.grid[y][x]
			var color: Color = simulation.TERRAIN_COLORS.get(terrain, Color.WHITE)
			var rect := Rect2(Vector2(x, y) * simulation.TILE_SIZE, Vector2.ONE * simulation.TILE_SIZE)
			draw_rect(rect, color)
			draw_rect(rect, Color(0, 0, 0, 0.1), false)

	if selected_tile.x >= 0:
		var selected_rect := Rect2(Vector2(selected_tile) * simulation.TILE_SIZE, Vector2.ONE * simulation.TILE_SIZE)
		draw_rect(selected_rect, Color(1, 1, 0, 0.5), false, 2.0)

func _input(event: InputEvent) -> void:
	if simulation == null:
		return
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		var grid_pos := Vector2i(event.position / simulation.TILE_SIZE)
		var tile := simulation.get_tile_at_grid(grid_pos)
		if tile.is_empty():
			return
		selected_tile = grid_pos
		emit_signal("tile_selected", tile)
		queue_redraw()
