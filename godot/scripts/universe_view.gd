extends Node2D

@export var tile_size: int = 24
var bridge: Node
var selected_tile: Dictionary = {}

func set_bridge(sim_bridge: Node) -> void:
	bridge = sim_bridge
	queue_redraw()

func _draw() -> void:
	if bridge == null:
		return
	for tile in bridge.tiles:
		var color := _terrain_color(tile["terrain"])
		draw_rect(Rect2(tile["x"] * tile_size, tile["y"] * tile_size, tile_size, tile_size), color)
		draw_rect(Rect2(tile["x"] * tile_size, tile["y"] * tile_size, tile_size, tile_size), Color.BLACK, false, 1.0)

func _input(event: InputEvent) -> void:
	if bridge == null:
		return
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		var gx: int = int(event.position.x / tile_size)
		var gy: int = int(event.position.y / tile_size)
		selected_tile = bridge.tile_at(gx, gy)
		queue_redraw()

func _terrain_color(terrain: String) -> Color:
	match terrain:
		"water": return Color(0.2, 0.4, 0.9)
		"plains": return Color(0.45, 0.75, 0.3)
		"forest": return Color(0.1, 0.5, 0.2)
		"mountain": return Color(0.5, 0.5, 0.5)
		_: return Color(0.9, 0.8, 0.4)
