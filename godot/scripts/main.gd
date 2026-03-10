extends Node

@onready var simulation_bridge: Node = $SimulationBridge
@onready var universe_view: Node2D = $UniverseView
@onready var debug_overlay: CanvasLayer = $DebugOverlay
@onready var hud: Control = $CanvasLayer/HUD
@onready var control_panel: Control = $CanvasLayer/ControlPanel

var elapsed: float = 0.0
var tick_interval: float = 1.0
const SAVE_PATH := "user://last_save.json"

func _ready() -> void:
	simulation_bridge.generate_world(424242, 32, 20)
	universe_view.set_bridge(simulation_bridge)
	debug_overlay.set_targets(simulation_bridge, universe_view)
	control_panel.set_seed(simulation_bridge.seed)
	_hud_connect()

func _process(delta: float) -> void:
	elapsed += delta
	if elapsed >= tick_interval:
		elapsed = 0.0
		simulation_bridge.step()

func _hud_connect() -> void:
	hud.play_pressed.connect(_on_play)
	hud.pause_pressed.connect(_on_pause)
	hud.speed_pressed.connect(_on_speed)
	hud.save_pressed.connect(_on_save)
	hud.load_pressed.connect(_on_load)

func _on_play() -> void:
	simulation_bridge.set_speed(1)

func _on_pause() -> void:
	simulation_bridge.set_speed(0)

func _on_speed(multiplier: int) -> void:
	simulation_bridge.set_speed(multiplier)

func _on_save() -> void:
	if simulation_bridge.save_state(SAVE_PATH):
		print("Saved world state to ", SAVE_PATH)

func _on_load() -> void:
	if simulation_bridge.load_state(SAVE_PATH):
		print("Loaded world state from ", SAVE_PATH)
		universe_view.queue_redraw()
		control_panel.set_seed(simulation_bridge.seed)
