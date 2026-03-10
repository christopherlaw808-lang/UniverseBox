extends Node

var seed: int = 424242
var width: int = 32
var height: int = 20
var tick: int = 0
var speed_multiplier: int = 1
var tiles: Array = []

func generate_world(in_seed: int, in_width: int, in_height: int) -> void:
	seed = in_seed
	width = in_width
	height = in_height
	tick = 0
	var rng := RandomNumberGenerator.new()
	rng.seed = seed
	tiles.clear()
	for y in range(height):
		for x in range(width):
			var noise: float = rng.randf() + (float(y) / max(1.0, float(height))) * 0.15
			var terrain := "desert"
			if noise < 0.20:
				terrain = "water"
			elif noise < 0.45:
				terrain = "plains"
			elif noise < 0.65:
				terrain = "forest"
			elif noise < 0.85:
				terrain = "mountain"
			var resources := _resources_for_terrain(terrain)
			tiles.append({"x":x, "y":y, "terrain":terrain, "resources":resources})

func step() -> void:
	if speed_multiplier <= 0:
		return
	tick += speed_multiplier

func set_speed(multiplier: int) -> void:
	speed_multiplier = max(multiplier, 0)

func tile_at(x: int, y: int) -> Dictionary:
	var idx := y * width + x
	if idx < 0 or idx >= tiles.size():
		return {}
	return tiles[idx]

func save_state(path: String) -> bool:
	var payload := {
		"seed": seed,
		"width": width,
		"height": height,
		"tick": tick,
		"speed_multiplier": speed_multiplier,
		"tiles": tiles
	}
	var text := JSON.stringify(payload, "\t")
	var file := FileAccess.open(path, FileAccess.WRITE)
	if file == null:
		push_warning("Failed to open save path: %s" % path)
		return false
	file.store_string(text)
	return true

func load_state(path: String) -> bool:
	if not FileAccess.file_exists(path):
		push_warning("No save exists at: %s" % path)
		return false
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return false
	var result := JSON.parse_string(file.get_as_text())
	if typeof(result) != TYPE_DICTIONARY:
		return false
	seed = result.get("seed", seed)
	width = result.get("width", width)
	height = result.get("height", height)
	tick = result.get("tick", tick)
	speed_multiplier = result.get("speed_multiplier", speed_multiplier)
	tiles = result.get("tiles", [])
	return true

func _resources_for_terrain(terrain: String) -> Dictionary:
	match terrain:
		"water":
			return {"food":1, "water":5, "stone":0, "metal":0, "energy":1}
		"plains":
			return {"food":4, "water":2, "stone":1, "metal":0, "energy":1}
		"forest":
			return {"food":3, "water":2, "stone":1, "metal":1, "energy":2}
		"mountain":
			return {"food":0, "water":1, "stone":4, "metal":3, "energy":1}
		_:
			return {"food":0, "water":0, "stone":2, "metal":1, "energy":3}
