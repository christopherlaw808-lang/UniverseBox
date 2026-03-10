extends Control

@onready var seed_label: Label = $SeedLabel

func set_seed(seed: int) -> void:
	seed_label.text = "Seed: %d" % seed
