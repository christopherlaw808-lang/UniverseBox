extends Node
class_name SimulationBridge

signal world_generated
signal tick_advanced(current_tick: int)
signal simulation_state_changed(is_playing: bool, speed_multiplier: float)

const SAVE_DIR := "user://saves"
const TILE_SIZE := 24
const TERRAIN_TYPES := ["water", "plains", "forest", "mountain", "desert"]
const TERRAIN_COLORS := {
	"water": Color("#3a7bd5"),
	"plains": Color("#89c76f"),
	"forest": Color("#2f8f45"),
	"mountain": Color("#8b8f99"),
	"desert": Color("#d8bc6f")
}

@export var world_width := 32
@export var world_height := 24
@export var seed := 1337

var is_playing := true
var speed_multiplier := 1.0
var tick := 0
var grid: Array = []

var _tick_accumulator := 0.0
var _seconds_per_tick := 0.5

func _ready() -> void:
	_generate_world(seed)
	emit_signal("simulation_state_changed", is_playing, speed_multiplier)

func _process(delta: float) -> void:
	if not is_playing:
		return

	_tick_accumulator += delta * speed_multiplier
	while _tick_accumulator >= _seconds_per_tick:
		_tick_accumulator -= _seconds_per_tick
		tick += 1
		emit_signal("tick_advanced", tick)

func _generate_world(world_seed: int) -> void:
	seed = world_seed
	tick = 0
	grid.clear()

	var rng := RandomNumberGenerator.new()
	rng.seed = seed

	for y in world_height:
		var row: Array = []
		for x in world_width:
			var value := rng.randf()
			var terrain := "plains"
			if value < 0.18:
				terrain = "water"
			elif value < 0.45:
				terrain = "plains"
			elif value < 0.64:
				terrain = "forest"
			elif value < 0.82:
				terrain = "desert"
			else:
				terrain = "mountain"
			row.append(terrain)
		grid.append(row)

	emit_signal("world_generated")
	emit_signal("tick_advanced", tick)

func set_playing(playing: bool) -> void:
	is_playing = playing
	emit_signal("simulation_state_changed", is_playing, speed_multiplier)

func toggle_play_pause() -> void:
	set_playing(not is_playing)

func set_speed(multiplier: float) -> void:
	speed_multiplier = max(0.1, multiplier)
	emit_signal("simulation_state_changed", is_playing, speed_multiplier)

func get_tile_at_grid(grid_pos: Vector2i) -> Dictionary:
	if not _is_in_bounds(grid_pos):
		return {}
	return {
		"x": grid_pos.x,
		"y": grid_pos.y,
		"terrain": grid[grid_pos.y][grid_pos.x]
	}

func _is_in_bounds(grid_pos: Vector2i) -> bool:
	return grid_pos.x >= 0 and grid_pos.y >= 0 and grid_pos.x < world_width and grid_pos.y < world_height

func save_world(save_name := "quick_save") -> bool:
	var dir := DirAccess.open("user://")
	if dir == null:
		return false
	dir.make_dir_recursive("saves")

	var payload := {
		"seed": seed,
		"tick": tick,
		"is_playing": is_playing,
		"speed_multiplier": speed_multiplier,
		"world_width": world_width,
		"world_height": world_height
	}

	var path := "%s/%s.json" % [SAVE_DIR, save_name]
	var file := FileAccess.open(path, FileAccess.WRITE)
	if file == null:
		return false
	file.store_string(JSON.stringify(payload, "\t"))
	return true

func load_world(save_name := "quick_save") -> bool:
	var path := "%s/%s.json" % [SAVE_DIR, save_name]
	if not FileAccess.file_exists(path):
		return false

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return false

	var parsed := JSON.parse_string(file.get_as_text())
	if typeof(parsed) != TYPE_DICTIONARY:
		return false

	seed = int(parsed.get("seed", seed))
	world_width = int(parsed.get("world_width", world_width))
	world_height = int(parsed.get("world_height", world_height))
	_generate_world(seed)
	tick = int(parsed.get("tick", tick))
	is_playing = bool(parsed.get("is_playing", is_playing))
	speed_multiplier = float(parsed.get("speed_multiplier", speed_multiplier))
	emit_signal("tick_advanced", tick)
	emit_signal("simulation_state_changed", is_playing, speed_multiplier)
	return true
