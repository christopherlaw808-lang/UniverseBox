extends Node

@onready var simulation: SimulationBridge = $SimulationBridge
@onready var universe_view: UniverseView = $UniverseView
@onready var debug_overlay: DebugOverlay = $DebugOverlay
@onready var hud: HUD = $HUD

func _ready() -> void:
	universe_view.tile_selected.connect(debug_overlay.set_selected_tile)
	# Keep references alive and explicit for future milestone wiring.
	assert(simulation != null)
	assert(hud != null)
