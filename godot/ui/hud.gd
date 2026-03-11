extends CanvasLayer
class_name HUD

@export var simulation_path: NodePath

@onready var control_panel: ControlPanel = $ControlPanel

var simulation: SimulationBridge

func _ready() -> void:
	simulation = get_node_or_null(simulation_path)
	if simulation:
		simulation.simulation_state_changed.connect(_on_simulation_state_changed)
		control_panel.set_playing(simulation.is_playing)

	control_panel.play_pause_toggled.connect(_on_play_pause_toggled)
	control_panel.speed_selected.connect(_on_speed_selected)
	control_panel.save_requested.connect(_on_save_requested)
	control_panel.load_requested.connect(_on_load_requested)

func _on_play_pause_toggled() -> void:
	if simulation:
		simulation.toggle_play_pause()

func _on_speed_selected(multiplier: float) -> void:
	if simulation:
		simulation.set_speed(multiplier)

func _on_save_requested() -> void:
	if simulation:
		simulation.save_world()

func _on_load_requested() -> void:
	if simulation:
		simulation.load_world()

func _on_simulation_state_changed(is_playing: bool, _speed: float) -> void:
	control_panel.set_playing(is_playing)
