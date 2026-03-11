extends CanvasLayer
class_name DebugOverlay

@export var simulation_path: NodePath

@onready var label: Label = $PanelContainer/MarginContainer/StatsLabel

var simulation: SimulationBridge
var selected_tile_info: Dictionary = {}

func _ready() -> void:
	simulation = get_node_or_null(simulation_path)
	if simulation:
		simulation.tick_advanced.connect(_on_tick_advanced)
		simulation.simulation_state_changed.connect(_on_simulation_state_changed)
	_update_text()

func set_selected_tile(tile: Dictionary) -> void:
	selected_tile_info = tile
	_update_text()

func _process(_delta: float) -> void:
	_update_text()

func _on_tick_advanced(_tick: int) -> void:
	_update_text()

func _on_simulation_state_changed(_playing: bool, _speed: float) -> void:
	_update_text()

func _update_text() -> void:
	if simulation == null:
		label.text = "No simulation attached"
		return

	var tile_text := "none"
	if not selected_tile_info.is_empty():
		tile_text = "(%d, %d) %s" % [
			selected_tile_info.get("x", -1),
			selected_tile_info.get("y", -1),
			selected_tile_info.get("terrain", "unknown")
		]

	label.text = "FPS: %d\nSeed: %d\nTick: %d\nSelected: %s\nSpeed: %.1fx\nState: %s" % [
		Engine.get_frames_per_second(),
		simulation.seed,
		simulation.tick,
		tile_text,
		simulation.speed_multiplier,
		"Playing" if simulation.is_playing else "Paused"
	]
