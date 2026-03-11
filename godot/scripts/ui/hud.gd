extends Control

signal play_pressed
signal pause_pressed
signal speed_pressed(multiplier)
signal save_pressed
signal load_pressed

func _on_play_button_pressed() -> void:
	emit_signal("play_pressed")

func _on_pause_button_pressed() -> void:
	emit_signal("pause_pressed")

func _on_speed2_button_pressed() -> void:
	emit_signal("speed_pressed", 2)

func _on_speed4_button_pressed() -> void:
	emit_signal("speed_pressed", 4)

func _on_save_button_pressed() -> void:
	emit_signal("save_pressed")

func _on_load_button_pressed() -> void:
	emit_signal("load_pressed")
