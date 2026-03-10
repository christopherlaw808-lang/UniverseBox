extends CanvasLayer

@onready var label: Label = $Panel/Label
var bridge: Node
var universe_view: Node

func set_targets(sim_bridge: Node, view: Node) -> void:
	bridge = sim_bridge
	universe_view = view

func _process(_delta: float) -> void:
	if bridge == null:
		return
	var selected := universe_view.selected_tile if universe_view != null else {}
	var selected_text := "none"
	if selected.size() > 0:
		selected_text = "%s,%s %s" % [selected.get("x", -1), selected.get("y", -1), selected.get("terrain", "?")]
	label.text = "FPS: %d\nSeed: %d\nTick: %d\nMap: %dx%d\nSpeed: x%d\nSelected: %s" % [Engine.get_frames_per_second(), bridge.seed, bridge.tick, bridge.width, bridge.height, bridge.speed_multiplier, selected_text]
